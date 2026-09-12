# Arielle Rosinski's website

A simple, responsive academic website for GitHub Pages. Plain HTML and CSS; no build step or JavaScript required.

## Preview locally

From this folder, run:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. Publications are at http://localhost:8000/pubs/.

## Edit the site

- `index.html`: home page. Research interests and background are intentionally blank; add text below the corresponding headings.
- `pubs/index.html`: publications, grouped into papers/preprints and conference posters. The asterisks mark equal contributions from the CV.
- `assets/css/style.css`: shared layout, typography, and responsive styles.
- `assets/img/arielle-rosinski.jpg`: supplied profile photograph, copied unchanged.
- `assets/docs/arielle-rosinski-cv.pdf`: downloadable CV, copied from `Arielle_CV.pdf`.

The profile and navigation appear in both HTML pages; update both when changing those details. Relative links also allow the pages to be opened directly from the filesystem.

## Publish with GitHub Pages

Push these files to the `ariellerosinski.github.io` repository. In the repository's **Settings → Pages**, select **Deploy from a branch**, choose the branch containing these files, and select **/ (root)**. The `.nojekyll` file allows GitHub Pages to serve the files directly.

## Content and design references

Profile details and all six publication/poster entries come from the supplied CV. Publication titles link to arXiv, PMLR, or the preprint DOI where available. Poster titles are plain text until individual poster links are added.

The layout takes inspiration from [Eva Yi Xie's website](https://minzsiure.github.io/), and the publication list from [Lior Fox's publications page](https://liorfox.github.io/pubs). The HTML and CSS are written for this site.
