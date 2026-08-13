# COMP 1110 Lecture Notebook Spec

Every weekly lecture notebook in this folder MUST follow this spec. It exists so that 13
independently authored notebooks feel like one course.

## 1. Output

One file per week: `weekNN_topic.ipynb` (e.g. `week03_conditionals.ipynb`) in
`/Users/lnguyen/ADSC_4910_instructors/COMP_1110/notebooks/`.

- `nbformat: 4`, `nbformat_minor: 5`
- kernelspec: `python3` / `Python 3` / `language: python`
- Build the notebook with a throwaway Python script using `nbformat` rather than hand-writing JSON.
  Use the interpreter `/Users/lnguyen/miniforge3/bin/python` (it has `nbformat` and `nbclient`).
  Put the build script in the scratchpad, NOT in the course folder.

## 2. RISE slideshow metadata

**Every cell** must carry a slide type. In `nbformat`, set:

```python
cell.metadata["slideshow"] = {"slide_type": "slide"}
```

Valid values and when to use them:

| `slide_type` | Use for |
| :--- | :--- |
| `slide` | A new top-level slide. Use for each major section. |
| `subslide` | A step *down* from the current slide (press ↓). Use for a worked example belonging to the slide above. |
| `fragment` | Content that appears on the *same* slide with the next click. Use to reveal an answer after a question. |
| `skip` | Instructor-only cells never shown in the deck. |
| `notes` | Speaker notes (visible in the RISE speaker view only). |
| `-` | Continues the current slide immediately (no click). |

Notebook-level metadata must include:

```python
nb.metadata["rise"] = {
    "theme": "simple",
    "transition": "none",
    "start_slideshow_at": "selected",
    "scroll": True,
    "enable_chalkboard": True,
    "autolaunch": False,
}
```

**Do not set a `footer`.** Footers eat vertical space that code cells need, and repeat information
already on the title slide. `transition` must be `"none"` — animation between slides adds nothing to
a live-coding lecture and delays the moment a code cell becomes clickable.

**Slide budget:** a 110-minute class = **25–40 slides** (counting `slide` + `subslide`). Do not
exceed 40. A slide must not require scrolling: keep code cells under ~15 lines and markdown
under ~12 lines. Break longer content into `subslide`s.

## 3. Required structure

In order:

1. **Title slide** (`slide`) — course code, week number, topic, date(s) of that week's classes,
   instructor name (Quan Nguyen), room OM 1241.
2. **Where we are** (`slide`) — one line on last week, one line on this week, one on next week.
3. **Today's outcomes** (`slide`) — 3–5 bullets, each tagged with the CLO it serves (e.g. `[CLO 1]`).
4. **Reading** (`slide`) — hyperlink to the exact textbook chapter (see §6).
5. **Body** — concept slides (see §4).
6. **Predict the output** (`subslide` × 3 minimum, spread through the body) — a short program, then
   a `fragment` cell revealing and explaining the answer. These rehearse the closed-book midterm
   format, where students read code without running it.
7. **Live coding** (`slide` × 1–2) — a near-empty code cell with a comment header stating the problem
   to be solved together in class. Include the completed solution in the immediately following cell
   marked `slide_type: "skip"` so the instructor has it but the deck does not show it.
8. **Common errors** (`slide`) — 2–4 mistakes students actually make on this week's material, each
   with the error message they will see and what it means.
9. **Summary** (`slide`) — 4–6 bullets.
10. **This week's worksheet** (`slide`) — what it covers, released Thursday, due Tuesday 9:00 AM.
11. **Next class** (`slide`) — one or two lines.

## 4. Concept slides

Alternate markdown → code → markdown. Each new concept gets:

- a markdown `slide` naming the concept in plain language (why it exists before how it works),
- a runnable code `subslide` demonstrating it in **under 15 lines**,
- where useful, a `fragment` showing a variation or the output explained.

Prefer concrete, non-abstract examples. Use domains a first-year student recognises: grades,
temperatures, shopping totals, text messages, song playlists. Avoid `foo`/`bar`.

## 5. Hard constraints on code

- **The notebook must execute top-to-bottom with no errors** under
  `jupyter nbconvert --execute --to notebook`. Verify before you finish (see §7).
- **Standard library only.** No pandas, numpy, requests, matplotlib. This is a first course and
  students may run these on a lab machine or in a browser.
- **No network access** of any kind.
- **No `input()` calls that block.** To demonstrate input, either assign a variable directly with a
  comment (`name = "Sam"   # imagine the user typed this`) or define a fake `input` in a `skip` cell.
- **No external data files.** If a lesson needs a data file (Week 8 especially), the notebook must
  **write the file itself** in an earlier code cell, then read it back. Clean up is not required.
- **Cells that intentionally raise an exception** (useful for §8 Common errors) must carry the tag
  `raises-exception`, i.e. `cell.metadata["tags"] = ["raises-exception"]`, or `--execute` will fail.
- Code must obey **PEP 8** — this course teaches it in Week 13, so the notebooks must model it from
  Week 1. 4-space indent, `snake_case`, spaces around operators, no line over 88 characters.
- Only use language features already taught. **Check the schedule below**: no f-strings before
  Week 7, no lists before Week 9, no dictionaries before Week 10, no classes before Week 12,
  no comprehensions at all. Week 1–6 code uses only variables, operators, `input`/`print`,
  `if`/`elif`/`else`, `while`/`for`, `range`, and functions.

## 6. Textbook links

Link to the Trinket edition, which is what the syllabus assigns:

| Ch | URL |
| :--- | :--- |
| 1 Introduction | https://books.trinket.io/pfe/01-intro.html |
| 2 Variables | https://books.trinket.io/pfe/02-variables.html |
| 3 Conditionals | https://books.trinket.io/pfe/03-conditional.html |
| 4 Functions | https://books.trinket.io/pfe/04-functions.html |
| 5 Iterations | https://books.trinket.io/pfe/05-iterations.html |
| 6 Strings | https://books.trinket.io/pfe/06-strings.html |
| 7 Files | https://books.trinket.io/pfe/07-files.html |
| 8 Lists | https://books.trinket.io/pfe/08-lists.html |
| 9 Dictionaries | https://books.trinket.io/pfe/09-dictionaries.html |
| 10 Tuples | https://books.trinket.io/pfe/10-tuples.html |
| 14 Objects | https://books.trinket.io/pfe/14-objects.html |

Non-textbook readings:

- Unit testing (Week 8): https://www.dataquest.io/blog/unit-tests-python/
- Documentation (Week 8): https://realpython.com/documenting-python-code/
- Code style (Week 13): https://peps.python.org/pep-0008/

**Chapters 11, 12, 13, 15, 16 are NOT part of this course.** Never reference regular expressions,
networked programs, web services, databases, or data visualization as course content.

## 7. Verification (required before you report done)

Run both, from the notebooks folder:

```bash
/Users/lnguyen/miniforge3/bin/python -c "
import nbformat, sys
nb = nbformat.read('weekNN_topic.ipynb', as_version=4)
nbformat.validate(nb)
types = [c.metadata.get('slideshow', {}).get('slide_type') for c in nb.cells]
missing = [i for i, t in enumerate(types) if not t]
assert not missing, f'cells missing slide_type: {missing}'
n = sum(1 for t in types if t in ('slide', 'subslide'))
print('OK', len(nb.cells), 'cells,', n, 'slides')
assert 20 <= n <= 40, f'slide count {n} outside 25-40 target'
"

/Users/lnguyen/miniforge3/bin/jupyter nbconvert --execute --to notebook \
    --output /tmp/out.ipynb weekNN_topic.ipynb
```

Both must pass. If `--execute` fails, fix the code — do not remove the check.

## 8. Course facts (do not contradict)

- COMP 1110, Fall 2026, Tue & Thu 9:30–11:20, OM 1241, first class Thu Sep 10.
- Instructor: Quan Nguyen. Textbook: *Python for Everybody* (Trinket edition).
- Assessment: 11 worksheets (best 10 × 2% = 20%), Midterm 1 25% (Thu Oct 15), Midterm 2 25%
  (Thu Nov 19), group final project 25% (individually graded), attendance 5%. **No final exam.**
- Midterms are **closed-book, 60 minutes, on Moodle, no running Python**.
- Project teams are formed in **Week 3**; the team proposal is due Thu Nov 5.
- No class Thu Nov 12 (fall mid-term break). Last day of classes Tue Dec 8.

## 9. Weekly assignments

| Week | Dates | Topic | Chapter |
| :--- | :--- | :--- | :--- |
| 1 | Thu Sep 10 | Intro: what a program is, hardware, interpreter, first `print` | 1 |
| 2 | Sep 15, 17 | Values, types, variables, expressions, `input()`, operators | 2 |
| 3 | Sep 22, 24 | Booleans, `if`/`elif`/`else`, nesting, `try`/`except` (+ teams form Thu) | 3 |
| 4 | Sep 29, Oct 1 | Functions, parameters, return values, scope | 4 |
| 5 | Oct 6, 8 | Iteration: `while`, `for`, `break`/`continue`, loop patterns | 5 |
| 6 | Oct 13, 15 | **Midterm 1 review** (Tue); midterm is Thu — notebook covers Tue only | 1–5 |
| 7 | Oct 20, 22 | Strings, slicing, methods + f-strings and output formatting | 6 |
| 8 | Oct 27, 29 | Files (Tue); **testing & documentation** (Thu) | 7 + articles |
| 9 | Nov 3, 5 | Lists, mutability, slices, methods, `split`/`join`, aliasing | 8 |
| 10 | Nov 10 only | Dictionaries, counting patterns, `get`, looping | 9 |
| 11 | Nov 17, 19 | Tuples, `sorted`, `items()`, **sets**; Midterm 2 review (Tue) | 10 |
| 12 | Nov 24, 26 | OOP I: classes, attributes, methods, `__init__` (Tue); OOP II: instances, inheritance (Thu) | 14 |
| 13 | Dec 1 | **Formatting & code style**: PEP 8, naming, layout, linters | PEP 8 |

Week 14 (Dec 8) is project presentations — no lecture notebook.
