# COMP 1110 — Lecture Notebooks

Weekly lecture notes for COMP 1110 (Fall 2026), written as Jupyter notebooks that double as
**live, executable slide decks** via RISE.

| File | Week | Dates | Topic |
| :--- | :--- | :--- | :--- |
| `week01_intro.ipynb` | 1 | Thu Sep 10 | Intro: programs, hardware, interpreters, first `print` |
| `week02_variables.ipynb` | 2 | Sep 15, 17 | Values, types, variables, expressions, `input()` |
| `week03_conditionals.ipynb` | 3 | Sep 22, 24 | Booleans, `if`/`elif`/`else`, `try`/`except` · **teams form** |
| `week04_functions.ipynb` | 4 | Sep 29, Oct 1 | Functions, parameters, return values, scope |
| `week05_iteration.ipynb` | 5 | Oct 6, 8 | `while`, `for`, loop patterns |
| `week06_git_and_project.ipynb` | 6 | Oct 13 | Git & GitHub · final project deliverables and how they are graded |
| `week06_midterm1_review.ipynb` | 6 | — | Midterm 1 review — **self-study pack, not a class** (midterm Thu Oct 15) |
| `week07_strings.ipynb` | 7 | Oct 20, 22 | Strings, slicing, methods, f-strings & formatting |
| `week08_files_testing_docs.ipynb` | 8 | Oct 27, 29 | Files (Tue) · testing & documentation (Thu) |
| `week09_lists.ipynb` | 9 | Nov 3, 5 | Lists, mutability, aliasing · **proposal due Thu** |
| `week10_dictionaries.ipynb` | 10 | Nov 10 | Dictionaries, counting patterns *(no Thu class)* |
| `week11_tuples_sets_review.ipynb` | 11 | Nov 17 | Tuples, sets, Midterm 2 review (midterm Thu Nov 19) |
| `week12_oop.ipynb` | 12 | Nov 24, 26 | OOP I: classes, `__init__`, `self` · OOP II: instances, inheritance |
| `week13_style_and_polish.ipynb` | 13 | Dec 1 | PEP 8, linters, project polish checklist |

Week 14 (Dec 8) is project presentations — no lecture notebook.

`SPEC.md` is the authoring spec these notebooks follow. Read it before editing or adding one.

---

## Running a notebook on Binder

Every notebook carries two links to a live copy of itself, both pointing at
[mybinder.org](https://mybinder.org):

- the **launch binder** badge just under the title, and
- an **Open in Binder** entry in the ⬇ download menu at the top of the page on the
  published site.

Both open JupyterLab on Binder with that week's notebook already loaded, so a student can
run and *edit* cells without installing anything. This is the fallback for the in-page
Pyodide kernel configured in `myst.yml` (`jupyter.lite`), which runs cells on the website
itself but cannot save edits.

**Tell students their Binder session is disposable.** It is deleted after ~10 minutes idle
and nothing they type is saved. To keep work, use *File → Download* before leaving.

### The environment

`binder/requirements.txt` and `binder/runtime.txt` at the **repo root** define the image
(`python-3.11`, matching the kernel these notebooks were executed with, so error messages
students see on Binder match the ones printed in the notes). The notebooks import only the
standard library, so the requirements file exists mainly to pin JupyterLab and to install
`jupyterlab-myst`, which renders the MyST frontmatter cell at the top of each notebook as a
frontmatter block instead of raw YAML.

The first launch after a push to `main` rebuilds the image and can take several minutes;
every launch after that is cached and starts in seconds. **Open one Binder session yourself
the morning of a class you plan to use it in** — that pays the build cost before 40 students
hit it at once.

### When a launch fails

mybinder.org is a federation of independent clusters, and each click is load-balanced to a
random one. A broken member fails for every repo on it, so the failures look alarming but
are not caused by anything here. Observed:

- `failed to create fsnotify watcher: too many open files` — inotify exhausted on that
  build node.
- `Could not resolve ref for gh:TRU-CS/COMP_1110/main` — that cluster has burned through
  its anonymous GitHub API quota.

**Both clear on a retry**, which lands on a different member. Tell students to click again
rather than assume the notebook is broken — and do not make a Binder launch the only path
through a class activity.

### The two extra cells

Each notebook starts with two cells that are *not* lecture content, both `slide_type: skip`
so they never appear in the RISE deck:

| Cell id | What it is |
| :--- | :--- |
| `myst-frontmatter` | MyST page frontmatter — the `downloads:` list that puts **Open in Binder** in the site's download menu |
| `binder-badge` | The visible **launch binder** badge and its one-line caption |

Both are generated, and both hard-code the notebook's own filename. **If you rename or add
a notebook, regenerate them** rather than hand-editing the URL:

```bash
python3 add_binder_links.py                 # every week*.ipynb here
python3 add_binder_links.py week14_new.ipynb
```

`add_binder_links.py` rewrites the two cells in place, is safe to run repeatedly, and
touches nothing else in the notebook.

---

## Presenting the notebooks as slides

These notebooks carry RISE slideshow metadata on every cell, so any of them can be presented as a
reveal.js deck **with every code cell still runnable and editable live in front of the class**.

### Install (JupyterLab 4 — what is on this machine)

```bash
pip install jupyterlab_rise
```

> **Which package?** The original `rise` package only works with the *classic* Notebook interface
> (Notebook ≤ 6). This machine has **JupyterLab 4.4.5**, so you need **`jupyterlab_rise`**, which is
> the JupyterLab 4 port. Installing plain `rise` here will appear to do nothing.
>
> If you prefer the classic interface instead, use `pip install notebook==6.5.4 rise` in a separate
> environment — but `jupyterlab_rise` is the simpler path.

### Present

```bash
cd /Users/lnguyen/ADSC_4910_instructors/COMP_1110/notebooks
jupyter lab week01_intro.ipynb
```

Then click the **bar-chart / "Enter slideshow" button** in the toolbar (or press <kbd>Alt</kbd>+<kbd>R</kbd>).

### Driving the deck

| Key | Action |
| :--- | :--- |
| <kbd>Space</kbd> / <kbd>→</kbd> | Next slide or fragment |
| <kbd>↓</kbd> | Next *subslide* (the worked example below the current slide) |
| <kbd>Shift</kbd>+<kbd>Space</kbd> | Back |
| <kbd>Shift</kbd>+<kbd>Enter</kbd> | **Run the current code cell, live** |
| <kbd>Esc</kbd> then <kbd>O</kbd> | Slide overview (jump anywhere) |
| <kbd>,</kbd> | Toggle the chalkboard — draw over a slide to annotate code |
| <kbd>Alt</kbd>+<kbd>R</kbd> | Exit slideshow back to the notebook |

The chalkboard is enabled in every notebook's metadata; it is the fastest way to circle a variable
and trace a loop by hand during class.

### How the slide structure works

Each cell has a `slide_type` in its metadata:

- **`slide`** — a new top-level slide (a new section)
- **`subslide`** — nested *below* the current slide; press <kbd>↓</kbd>. Used for worked examples.
- **`fragment`** — revealed on the same slide with the next click. Used to hide an answer until the
  class has guessed.
- **`skip`** — never shown in the deck. **Live-coding solutions live here** — you get the answer in
  your notebook, students see only the empty problem cell.
- **`notes`** — speaker notes, visible only in the RISE speaker view.

To change a cell's slide type in JupyterLab: open the **Property Inspector** (the ⚙/slider icon in
the right sidebar) → **Common Tools** → **Slide Type**.

---

## Teaching conventions used throughout

- **Predict the output** — a code cell, then a `fragment` revealing and *explaining* the answer.
  These deliberately rehearse the closed-book Moodle midterm format, where students must read code
  without running it.
- **Live coding** — an empty cell with the problem stated in a comment, solved with the class. The
  worked solution sits in the next cell as `skip`, so it stays out of the projected deck.
- **Common errors** — real error messages students will hit that week, and what they mean.
  Cells that raise on purpose are tagged `raises-exception` so batch execution still passes.

## Constraints these notebooks respect

- **Standard library only** — no pandas, numpy, or matplotlib. Students may be on lab machines.
- **No network access**, and **no external data files**: any notebook that reads a file writes that
  file itself first.
- **No blocking `input()`** — input is shown as an assignment with an explanatory comment.
- **Only features already taught** — no f-strings before Week 7, no lists before Week 9, no
  dictionaries before Week 10, no classes before Week 12, and no comprehensions at all.
- **PEP 8 throughout**, since Week 13 grades students on it. The sole exception is Week 13's
  deliberately bad refactoring examples, which are labelled as such.

## Checking a notebook after editing

```bash
/Users/lnguyen/miniforge3/bin/python -c "
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
nbformat.validate(nb)
types = [c.metadata.get('slideshow', {}).get('slide_type') for c in nb.cells]
missing = [i for i, t in enumerate(types) if not t]
assert not missing, f'cells missing slide_type: {missing}'
print('OK —', len(nb.cells), 'cells,',
      sum(1 for t in types if t in ('slide', 'subslide')), 'slides')
" week01_intro.ipynb

/Users/lnguyen/miniforge3/bin/jupyter nbconvert --execute --to notebook \
    --output /tmp/check.ipynb week01_intro.ipynb
```

The first command catches a cell with no slide type (it would silently glue itself onto the previous
slide). The second proves every code cell still runs — worth doing before any class.
