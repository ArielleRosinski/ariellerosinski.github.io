# Arielle Rosinski

Personal website: https://ariellerosinski.github.io/

## Preview

```sh
python3 -m http.server 8000
```

Open http://localhost:8000.

## Edit

- `index.html`: biography and publications.
- `pubs/index.html`: redirect to the publications section.
- `assets/css/style.css`: shared styles.
- `assets/js/theme.js`: theme toggle and section navigation.

After editing, run `python3 scripts/update_assets.py` to refresh both pages and their shared assets. Commit and push the updated files to publish through GitHub Pages.
