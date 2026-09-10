#!/usr/bin/env python3
"""Add (or refresh) the two Binder cells at the top of every lecture notebook.

Each notebook gets:

  myst-frontmatter  a MyST frontmatter cell whose `downloads:` list puts an
                    "Open in Binder" entry in the download menu on the site
  binder-badge      a visible "launch binder" badge and caption

Both are `slide_type: skip`, so neither shows up in the RISE deck, and both
hard-code the notebook's own filename. Re-run this after renaming or adding a
notebook; it rewrites the cells in place and is safe to run repeatedly.

    python3 add_binder_links.py            # all notebooks in this directory
    python3 add_binder_links.py week01_intro.ipynb
"""

import json
import os
import sys
from glob import glob

REPO = "TRU-CS/COMP_1110"
REF = "main"  # explicit; the deploy workflow assumes this branch too
PREFIX = "COMP_1110/notebooks"  # this directory's path inside the repo


def binder_url(name):
    return (f"https://mybinder.org/v2/gh/{REPO}/{REF}"
            f"?urlpath=lab/tree/{PREFIX}/{name}")


def frontmatter_cell(name):
    return {
        "cell_type": "markdown",
        "id": "myst-frontmatter",
        "metadata": {"slideshow": {"slide_type": "skip"}},
        "source": [
            "---\n",
            "downloads:\n",
            f"  - file: {name}\n",
            "    title: Notebook (.ipynb)\n",
            f"  - url: {binder_url(name)}\n",
            "    title: Open in Binder\n",
            "---\n",
        ],
    }


def badge_cell(name):
    return {
        "cell_type": "markdown",
        "id": "binder-badge",
        "metadata": {"slideshow": {"slide_type": "skip"}},
        "source": [
            f"[![Open in Binder](https://mybinder.org/badge_logo.svg)]"
            f"({binder_url(name)})\n",
            "\n",
            "*Run this notebook yourself: press the power button at the top of "
            "the page to\n",
            "execute cells right here, or click the badge to open the whole "
            "notebook in\n",
            "JupyterLab on Binder.*\n",
        ],
    }


def place(cells, cell, index):
    """Replace the cell with this id if present, else insert it at `index`."""
    for i, existing in enumerate(cells):
        if existing.get("id") == cell["id"]:
            cells[i] = cell
            return "updated"
    cells.insert(index, cell)
    return "added"


def main(paths):
    for path in paths:
        name = os.path.basename(path)
        nb = json.load(open(path, encoding="utf-8"))
        cells = nb["cells"]
        a = place(cells, frontmatter_cell(name), 0)
        # After the frontmatter cell and the title cell.
        b = place(cells, badge_cell(name), 2)
        # Match the on-disk formatting exactly so diffs stay to the point.
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
        print(f"{name}: frontmatter {a}, badge {b}")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1:] or sorted(glob(os.path.join(here, "week*.ipynb"))))
