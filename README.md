# Arielle Rosinski's website

A simple, responsive academic website for GitHub Pages. Plain HTML and CSS with a small JavaScript theme toggle; no build step required. Content remains accessible without JavaScript.

## Preview locally

From this folder, run:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. Publications are at http://localhost:8000/pubs/.

## Edit the site

- `index.html`: home page. Research interests and background are intentionally blank; add text below the corresponding headings.
- `pubs/index.html`: publications, grouped into papers/preprints and conference posters. The asterisks mark equal contributions.
- `assets/css/style.css`: shared layout, typography, responsive styles, and light/dark palettes.
- `assets/js/theme.js`: sun/moon theme toggle. Defaults to the system preference, remembers explicit choices, and synchronizes pages restored from history and other open tabs. If storage is unavailable, internal links carry the theme selection.
- `assets/img/arielle-rosinski.jpg`: supplied profile photograph, copied unchanged.

The profile and navigation appear in both HTML pages; update both when changing those details. Relative links also allow the pages to be opened directly from the filesystem.

After editing either page, the CSS, or the theme script, run `python3 scripts/update_assets.py`. This creates assets with content hashes in their filenames and updates both pages and their navigation links as one release, preventing navigation from reopening an older cached palette. The normal canonical URLs stay unchanged. Older generated assets are retained so cached pages can still load them. Commit the generated files alongside the source files and HTML. No build tools are needed to serve the site.

## Publish with GitHub Pages

Push these files to the `ariellerosinski.github.io` repository. In the repository's **Settings → Pages**, select **Deploy from a branch**, choose the branch containing these files, and select **/ (root)**. The `.nojekyll` file allows GitHub Pages to serve the files directly.

## Content and design references

Profile details and all six publication/poster entries come from the supplied academic information. Publication titles link to arXiv, PMLR, or the preprint DOI where available. Poster titles are plain text until individual poster links are added.

The current visual design takes inspiration from [Apple's website](https://www.apple.com/): a translucent navigation bar, large system typography, neutral surfaces, rounded sections, and blue links. Home and Publications share the same profile header and light/dark palettes. Research interests and background remain intentionally blank.

The original academic layout was inspired by [Eva Yi Xie's website](https://minzsiure.github.io/), and the publication list by [Lior Fox's publications page](https://liorfox.github.io/pubs). The HTML and CSS are written for this site.
