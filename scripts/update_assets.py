"""Version shared assets and page links together for a consistent release."""

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

    # Keep older generated assets: cached HTML may still reference them.

# A fixed page query can reopen cached HTML containing an older stylesheet.
# Hash both pages (with old release queries removed) so navigation always stays
# within the same release. Canonical URLs remain the ordinary public URLs.
page_link = re.compile(r'(href="|content="0; url=)(\.{1,2}/(?:pubs/)?)(?:\?v=[^"&#]*)?(#[^"]*)?"')
pages = {name: page_link.sub(lambda match: f'{match[1]}{match[2]}{match[3] or ""}"', html) for name, html in pages.items()}
release = hashlib.sha256("\n".join(pages[name] for name in sorted(pages)).encode()).hexdigest()[:12]
pages = {
    name: page_link.sub(lambda match: f'{match[1]}{match[2]}?v={release}{match[3] or ""}"', html)
    for name, html in pages.items()
}

for name, html in pages.items():
    (ROOT / name).write_text(html)
    print(f"Updated {name} to release {release}")
