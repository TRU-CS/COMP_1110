# COMP 1110 — Introduction to Computer Programming

Course materials for **COMP 1110, Fall 2026** at Thompson Rivers University, published as a
[MyST / Jupyter Book](https://mystmd.org).

```
COMP_1110/
├── myst.yml                  book config (TOC, theme, metadata)
├── syllabus.md               course outline — the book's landing page
├── pythonlearn.pdf           reference copy of the textbook (NOT distributed — students use the web edition)
└── notebooks/
    ├── SPEC.md               authoring spec for the lecture notebooks (not in the book)
    ├── README.md             RISE slideshow setup and presenting guide (not in the book)
    └── week01..week13.ipynb  13 weekly lecture notebooks
```

The TOC is flat: **`syllabus.md` first — it is the landing page — then the 13 week notebooks**, all at
the same level. `SPEC.md` and `notebooks/README.md` are instructor-facing and deliberately left out
of the published book; they stay on disk for you.

## Building the book

Requires the **MyST** CLI (this is Jupyter Book v2, driven by `myst.yml` — *not* the legacy
Sphinx-based `jupyter-book` 1.x, which uses `_config.yml`/`_toc.yml`).

```bash
cd COMP_1110

# Live preview with hot reload at http://localhost:3000
myst start

# Static site into _build/html
myst build --html
```

Both `myst` and the npm `jupyter-book` v2 CLI read the same `myst.yml`, so
`jupyter-book build --html` also works if you have that installed instead.

## Notebook outputs are committed

The site builds **without a kernel** — every notebook is committed with its outputs already stored,
so readers see results without anything executing at build time.

**This means: after editing any code cell, re-execute before committing**, or the published page will
show stale or missing output.

```bash
cd COMP_1110/notebooks
for f in week*.ipynb; do
  /Users/lnguyen/miniforge3/bin/jupyter nbconvert --execute --inplace --to notebook "$f"
done
```

Cells that raise on purpose are tagged `raises-exception`, so this completes cleanly. Running the
notebooks also regenerates their data files (`grades.txt`, `week09_grades.txt`, …), which are
gitignored — each notebook writes any file it reads.

## Verifying a notebook

```bash
cd COMP_1110/notebooks
/Users/lnguyen/miniforge3/bin/python -c "
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
nbformat.validate(nb)
types = [c.metadata.get('slideshow', {}).get('slide_type') for c in nb.cells]
assert all(types), 'a cell is missing slide_type'
print('OK —', len(nb.cells), 'cells,',
      sum(1 for t in types if t in ('slide', 'subslide')), 'slides')
" week01_intro.ipynb
```

The `slide_type` check matters: a cell missing one silently merges into the previous slide when
presenting. See `notebooks/SPEC.md` for the full authoring rules.

## Two ways these notebooks are used

1. **As a book** — published here for students to read and download.
2. **As live slides** — every notebook carries RISE metadata, so it presents as a deck with runnable
   code cells. Setup and keyboard shortcuts are in [`notebooks/README.md`](notebooks/README.md).

Editing for one does not break the other. RISE reads cell metadata that MyST ignores.

## Deployment note

The repository root holds a **separate** MyST project for ADSC 4910, and
`.github/workflows/deploy.yml` builds only that root project — it does **not** build this book.

To publish COMP 1110 as well, either:

- **Separate site (recommended):** add a second workflow that runs `myst build --html` with
  `working-directory: COMP_1110` and deploys it to its own Pages target or repository; or
- **One combined site:** add COMP 1110's pages to the root `myst.yml` TOC.

Until one of those is done, this book builds locally but is not published.
