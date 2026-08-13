# COMP 1110 — Weekly Worksheets

Eleven student-facing worksheets (2% each, best 10 count = 20%), one per release week, as
Jupyter notebooks. Released **Thursday after class**, due the following **Tuesday 9:00 AM** on
Moodle.

| File | WS | Released | Due | Topic (chapter) | The game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `worksheet01_hello_machine.ipynb` | 1 | Thu Sep 10 | Tue Sep 15 | `print`, arithmetic, errors (1) | ASCII name badge + Error Lab |
| `worksheet02_mind_reader.ipynb` | 2 | Thu Sep 17 | Tue Sep 22 | Variables, types, `input` (2) | The Mind Reader number trick |
| `worksheet03_vending_machine.ipynb` | 3 | Thu Sep 24 | Tue Sep 29 | Conditionals, `try`/`except` (3) | Vending machine + RPS judge |
| `worksheet04_dice_dungeon.ipynb` | 4 | Thu Oct 1 | Tue Oct 6 | Functions, scope (4) | Dice Dungeon + Mad Libs |
| `worksheet05_guess_bot.ipynb` | 5 | Thu Oct 8 | **Tue Oct 20** | Iteration (5) | Guess Bot + Collatz race |
| `worksheet06_secret_messages.ipynb` | 6 | Thu Oct 22 | Tue Oct 27 | Strings, f-strings (6) | Caesar cipher + cracking |
| `worksheet07_high_score_vault.ipynb` | 7 | Thu Oct 29 | Tue Nov 3 | Files, testing, docstrings (7 + articles) | High Score Vault + Bug Bounty |
| `worksheet08_tic_tac_toe.ipynb` | 8 | Thu Nov 5 | Tue Nov 10 | Lists, aliasing (8) | Tic-tac-toe referee + bot ladder |
| `worksheet09_lyric_lab.ipynb` | 9 | **Tue Nov 10** | Tue Nov 17 | Dictionaries (9) | Lyric Lab word counts |
| `worksheet10_common_ground.ipynb` | 10 | Thu Nov 19 | Tue Nov 24 | Tuples, sorting, sets (10 + notes) | Common Ground similarity map |
| `worksheet11_robot_arena.ipynb` | 11 | Thu Nov 26 | Tue Dec 1 | OOP (14) | Robot Arena championship |

Two dates are deliberately off the weekly rhythm and are explained inside the worksheets
themselves: **WS5** is due after Midterm 1 (Oct 15), and **WS9** is released on the Tuesday
because there is no class on Thursday Nov 12 (fall mid-term break).

## The shape of every worksheet

Identical structure, so students learn it once:

1. **Header** — covers / reading / released / due / worth, plus name and student-number fields.
2. **How to use this worksheet** — the self-check convention, the collaboration rules, a 60–90
   minute budget.
3. **🔥 Warm-up — Predict the output** — three short programs with a prediction cell *before* the
   runnable cell. This is the closed-book midterm format, every single week.
4. **Part A** — three or four short exercises, each followed by a **✅ Self-check** cell.
5. **The game** — the build, in staged functions that the self-checks test as students go.
6. **🐛 Trace and explain** — one hand-trace table plus a find-the-bug, as the syllabus requires.
7. **🤝 Team Arena** — the interactive part (below).
8. **⭐ Bonus** — explicitly 0 marks, for the students who want more.
9. **Checklist · AI acknowledgement · what's next.**

## How the interaction works

Every worksheet ends with a **Team Arena**: a named Moodle forum thread, plus something that
happens in the following Tuesday's class. The design constraint is the syllabus — students may
discuss approaches but **must not share code** — so what they exchange is never a solution:

| WS | Thread | What is exchanged |
| :--- | :--- | :--- |
| 1 | Error Bounty | error messages they caused on purpose |
| 2 | Trick Swap | number tricks as English recipes, not code |
| 3 | Break My Branch | inputs designed to break each other's vending machines |
| 4 | Spec Swap | function specs, and test cases for each other's specs |
| 5 | Collatz Leaderboard | results; a mismatch pinpoints somebody's bug |
| 6 | Cipher Exchange | ciphertexts to crack |
| 7 | Bug Bounty | deliberately planted bugs; others post failing tests |
| 8 | Referee Disputes | board positions + a live bot tournament in class |
| 9 | The Class Corpus | counts from an identical file — disagreement = bug |
| 10 | Common Ground | favourites sets; the class similarity map on the board |
| 11 | Robot Championship | robot stats and strategies; round-robin in class |

**You need to create the eleven forum threads on Moodle**, named exactly as above prefixed with
the week (e.g. `Week 1 — Error Bounty`), and to reserve ~15 minutes of the Tuesday class for the
in-class half. Several Arenas explicitly promise a class activity: the WS8 bot ladder, the WS10
similarity map, and the WS11 championship are the big ones.

The Arenas from WS4 onward lean on **project teams** (formed Week 3), which is deliberate — the
syllabus asks teams to be study groups from the moment they form.

## Self-checks

Exercises are followed by cells that `assert` the expected behaviour and print
`All checks passed`. Students self-grade before submitting; you can mark by running
**Restart & Run All** and reading which checks survive.

The checks only use language features taught by that week: no f-strings before WS6, no lists
before WS8, no dictionaries before WS9, no classes before WS11, and no comprehensions anywhere —
the same rules `notebooks/SPEC.md` sets for the lectures. That is why the WS1–WS3 checks are
thinner (with no functions, there is nothing to call twice) and why those worksheets lean on
fill-in-the-table testing instead — which WS4 then explicitly pays off when the same tests become
seven asserts in one run.

## Verifying after an edit

The worksheets ship with **empty `# TODO` cells**, so they are not expected to execute top to
bottom as-is — a plain `nbconvert --execute` will fail, by design. What is checked instead is
that every self-check passes against a reference solution:

```bash
/Users/lnguyen/miniforge3/bin/python -c "
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
nbformat.validate(nb)
print('OK -', len(nb.cells), 'cells')
" worksheet04_dice_dungeon.ipynb
```

All 56 self-check cells across WS2–WS11 were run against reference solutions before release; the
build and verification scripts are not kept in the course folder. If you change an exercise,
re-derive its expected values — several checks encode real answers (the Collatz champion under
1000 is **871** at 178 steps; the WS6 ciphertext is a shift of 3; `song.txt` has 28 words, 10
distinct, `round` × 8).

Cells that raise on purpose carry the `raises-exception` tag.

## Files the worksheets create

WS7 and WS9 write the data files they read (`arcade_scores.txt`, `game_log.txt`, `song.txt`), in
the first code cell, following the same convention as the lecture notebooks. Nothing needs to be
downloaded and there is no network access anywhere. Those files are gitignored.

## Not in the book

These are **not** in `myst.yml`'s TOC — they are released weekly on Moodle, and publishing them
in the book would put worksheet 11 in front of students in week 2. If you later want them
published after the term, add them as a second TOC section.

## Answer keys

Not included. The self-checks encode the expected behaviour precisely, which is most of a key;
if you want distributable solution notebooks, the reference implementations used for
verification are the natural starting point and can be regenerated per worksheet.
