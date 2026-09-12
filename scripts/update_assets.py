"""Give shared CSS/JS content-based URLs, then update both static pages."""

import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ("assets/css/style.css", "assets/js/theme.js")
pages = {name: (ROOT / name).read_text() for name in ("index.html", "pubs/index.html")}

for source in SOURCES:
    path = ROOT / source
    content = path.read_bytes()
    digest = hashlib.sha256(content).hexdigest()[:12]
    generated = path.with_name(f"{path.stem}.{digest}{path.suffix}")
    generated.write_bytes(content)
    pattern = re.escape(path.stem) + r"(?:\.[0-9a-f]{12})?" + re.escape(path.suffix) + r"(?:\?v=[^\"]*)?"
    for name, html in pages.items():
        pages[name] = re.sub(pattern, generated.name, html)

    # Remove only generated copies of this asset from previous releases.
    for old in path.parent.glob(f"{path.stem}.*{path.suffix}"):
        if old != generated and re.fullmatch(f"{re.escape(path.stem)}\\.[0-9a-f]{{12}}{re.escape(path.suffix)}", old.name):
            old.unlink()

for name, html in pages.items():
    (ROOT / name).write_text(html)
    print(f"Updated shared assets in {name}")
