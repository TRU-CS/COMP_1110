#!/usr/bin/env python3
"""Add (or refresh) the "Open in Colab" cell at the top of every lecture notebook.

Each notebook gets a single `colab-badge` markdown cell holding a Colab badge
that opens that week on https://colab.research.google.com. It is
`slide_type: skip`, so it never shows up in the RISE deck, and it hard-codes the
notebook's own filename. Re-run this after renaming or adding a notebook; it
rewrites the cell in place and is safe to run repeatedly.

    python3 add_colab_links.py            # all notebooks in this directory
    python3 add_colab_links.py week01_intro.ipynb

It also strips the cells left over from the earlier Binder setup, so running it
once cleans up a notebook that still carries them.
"""

import json
import os
import sys
from glob import glob

REPO = "TRU-CS/COMP_1110"
BRANCH = "main"  # the deploy workflow assumes this branch too
PREFIX = "COMP_1110/notebooks"  # this directory's path inside the repo

CELL_ID = "colab-badge"
OBSOLETE_IDS = {"myst-frontmatter", "binder-badge"}


def colab_url(name):
    return (f"https://colab.research.google.com/github/{REPO}"
            f"/blob/{BRANCH}/{PREFIX}/{name}")


def badge_cell(name):
    return {
        "cell_type": "markdown",
        "id": CELL_ID,
        "metadata": {"slideshow": {"slide_type": "skip"}},
        "source": [
            f"[![Open in Colab]"
            f"(https://colab.research.google.com/assets/colab-badge.svg)]"
            f"({colab_url(name)})\n",
            "\n",
            "*Run this notebook yourself: press the power button at the top of "
            "the page to\n",
            "execute cells right here, or click the badge to open an editable "
            "copy in Google\n",
            "Colab (a Google account is required).*\n",
        ],
    }


def main(paths):
    for path in paths:
        name = os.path.basename(path)
        nb = json.load(open(path, encoding="utf-8"))
        cells = nb["cells"]

        removed = [c["id"] for c in cells if c.get("id") in OBSOLETE_IDS]
        cells[:] = [c for c in cells if c.get("id") not in OBSOLETE_IDS]

        cell = badge_cell(name)
        for i, existing in enumerate(cells):
            if existing.get("id") == CELL_ID:
                cells[i] = cell
                action = "updated"
                break
        else:
            cells.insert(1, cell)  # right after the title cell
            action = "added"

        # Match the on-disk formatting exactly so diffs stay to the point.
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
        note = f", removed {', '.join(removed)}" if removed else ""
        print(f"{name}: badge {action}{note}")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1:] or sorted(glob(os.path.join(here, "week*.ipynb"))))
