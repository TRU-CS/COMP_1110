# Worksheet 11 — Team Repo Lab

| | |
| :--- | :--- |
| **Covers** | Running Python scripts from the terminal · the `if __name__ == "__main__":` guard · testing scripts with `pytest` · clone, commit, pull, push as a team |
| **Reading** | [Week 12 notes](../notebooks/week12_scripts_testing_github.ipynb) · [Final project brief](../final_project.md) §1 · [Get Started — pytest](https://docs.pytest.org/en/stable/getting-started.html) |
| **Released** | Tuesday, November 24 (in class) |
| **Due** | **Thursday, December 3, 11:59 PM** |
| **Worth** | 2% (Pass/Fail) — your best 10 of 11 worksheets count |
| **Where** | **In your team's GitHub repository, on your own laptop.** Not on TRU-Think. |

---

## How this worksheet works

This one is different. There is no notebook and nothing to upload. You work **in your
team's project repository**, and **your commits are your submission**: after the due
date I read what your GitHub account pushed.

- **You need:** a laptop with Python 3, Git, and VS Code; your GitHub account; and
  access to your team's repository (you have accepted the collaborator invitation).
- **Individual work, shared place.** Everyone on the team does every part, in **their
  own folder**, from **their own account**. Help each other with the tools — that is
  what teams are for — but each person writes their own code and answers.
- **Budget:** about 90 minutes. Part A is the part most likely to fight back; start it
  in Thursday's class, where help is in the room.
- **Windows:** where this sheet says `python3`, type `python` (or `py`).

Lines starting with `$` are typed into the **terminal** (VS Code → *Terminal → New
Terminal*). Do not type the `$`.

---

## Part A — Tools and your folder

### A1 — Check your tools

Run each of these. Every one should print a version number, not an error.

```text
$ python3 --version
$ git --version
$ python3 -m pip install pytest
$ python3 -m pytest --version
```

If `git` is missing: install it from [git-scm.com](https://git-scm.com/downloads) and
**restart VS Code**. If `pip install` complains about permissions, add `--user`.

### A2 — Clone your team repository

On GitHub, open your team repository → green **Code** button → copy the HTTPS URL.

```text
$ cd Documents
$ git clone https://github.com/<your-team>/<your-repo>.git
$ cd <your-repo>
$ code .
```

Already cloned it before? Just `cd` into it and run `git pull`.

Then, **once per laptop**:

```text
$ git config --global user.name "Your Name"
$ git config --global user.email "the-email-on-your-github-account"
$ git config --global pull.rebase false
```

The email matters: commits made with an email GitHub does not know **do not show up as
yours** — and your commits are how this worksheet, and the project, are marked.

### A3 — Make your folder, then your first commit

Inside the repository, create a folder `practice/<your-github-username>/` — for example
`practice/amina-chen/`. Everything for Parts A–C goes in there.

In it, create **`RESULTS.md`** with this content, and fill in the A1 part by pasting
what your terminal printed:

````markdown
# Worksheet 11 — <your name> (<your GitHub username>)

## A1 — Tools
```
<paste the output of python3 --version, git --version, python3 -m pytest --version>
```

## B4 — `__name__` experiment

## C3 — The failure report

## D — My project function
- Function:
- Commit link:

## Trace and explain
### Q1
### Q2
### Q3
````

Now commit and push it:

```text
$ git pull
$ git add practice
$ git commit -m "Add Worksheet 11 folder for <your name>"
$ git push
```

The first push asks you to sign in. **Your GitHub password will not work here.** On
Windows a browser window opens — sign in there. In VS Code you can instead push from the
**Source Control** panel and choose *Sign in with GitHub*. If Git keeps asking for a
password, create a *personal access token* on GitHub (Settings → Developer settings →
Personal access tokens) and paste that instead.

✅ **Self-check:** open your repository on GitHub. Your folder is there, and the commit
shows **your** username and avatar.

---

## Part B — Bill Splitter, a real script

Friends at a restaurant want to split the bill, plus tip, evenly. You will finish a script
that asks for the numbers and prints each person's share.

### B1 — Create the script

In your practice folder, create **`bill_splitter.py`** with exactly this, then finish the
three `TODO` functions. Do not change `main` or `ask_amount`.

```python
"""Bill Splitter: share a restaurant bill, plus tip, between friends."""


def main():
    """Ask for the bill, the tip and the group size, then print each share."""
    bill = ask_amount("Bill total ($): ")
    percent = ask_amount("Tip percent: ")
    people = int(ask_amount("How many people? "))
    total = bill + tip_amount(bill, percent)
    print(f"Total with tip: ${total:.2f}")
    print(f"Each person pays: ${share(total, people):.2f}")


def ask_amount(prompt):
    """Keep asking until the user types a number that is zero or more."""
    while True:
        amount = parse_amount(input(prompt))
        if amount is not None:
            return amount
        print("Please type a number, like 42 or 42.50")


def parse_amount(text):
    """Return text as a float, or None if it is not a number of zero or more."""
    # TODO: strip spaces and a leading "$", then convert with float().
    #       Return None if float() raises ValueError, or if the number is negative.


def tip_amount(bill, percent):
    """Return the tip on bill at the given percent, rounded to cents."""
    # TODO: one line. round(..., 2) rounds to cents.


def share(total, people):
    """Return one person's share of total, rounded to cents (0.0 if nobody)."""
    # TODO: return 0.0 when people is 0 or less, otherwise total / people rounded.


if __name__ == "__main__":
    main()
```

*Hint for `parse_amount`:* `" $12.50 ".strip().lstrip("$")` gives `"12.50"`.

### B2 — Run it

From **inside your practice folder** (`cd practice/<your-github-username>`):

```text
$ python3 bill_splitter.py
Bill total ($): 84.50
Tip percent: 18
How many people? four
Please type a number, like 42 or 42.50
How many people? 4
Total with tip: $99.71
Each person pays: $24.93
```

Your numbers must match. Also try `-20` and `$100` as the bill — the first should be
refused, the second accepted.

### B3 — Commit

```text
$ git add bill_splitter.py
$ git commit -m "Finish Bill Splitter functions"
$ git pull
$ git push
```

### B4 — The `__name__` experiment

1. Add this as the **first line** of `bill_splitter.py`:
   `print("bill_splitter.py: __name__ is", __name__)`
2. Run `python3 bill_splitter.py` (then press **Ctrl+C** to stop it at the first
   question).
3. Now run this one-liner, which **imports** the file instead of running it:
   `python3 -c "import bill_splitter"`
4. Paste both outputs under **B4** in `RESULTS.md`, and add one sentence: *why did the
   second command not ask you anything?*
5. **Delete the line you added in step 1.** Save.

---

## Part C — The testing script

### C1 — Create the tests

In the same folder, create **`test_bill_splitter.py`**:

```python
from bill_splitter import parse_amount, share, tip_amount


def test_share():
    assert share(30, 3) == 10.0
    assert share(10, 3) == 3.33       # rounding
    assert share(50, 0) == 0.0        # nobody: no crash


def test_parse_amount():
    # TODO: at least 3 asserts — a plain number, " $12.50 ", and text that is
    #       not a number. Bonus marks from your future self: a negative number.
    ...


def test_tip_amount():
    # TODO: at least 2 asserts — a typical tip, and a 0% tip.
    ...
```

Replace each `...` with your asserts. *Hint:* to check for `None`, write
`assert parse_amount("ten") is None`.

### C2 — Run them

Still inside your practice folder:

```text
$ python3 -m pytest -v
```

✅ **Self-check:** `collected 3 items` and `3 passed`. If you see `collected 0 items`,
a name does not start with `test_`. If you see `OSError: pytest: reading from stdin`,
your `__name__` guard is missing or broken.

> **Run pytest from your own folder,** not from the top of the repository. Your whole team
> has a file called `test_bill_splitter.py`, and pytest refuses to load two test files with
> the same name (`import file mismatch`). At the top level, run only the project's tests:
> `python3 -m pytest test_project.py`.

### C3 — Break it on purpose

1. In `share`, change `round(total / people, 2)` to `total // people`. Save.
2. Run `python3 -m pytest -v` again. One test should fail.
3. Under **C3** in `RESULTS.md`, paste the **`>` line and the `E` line(s)** from the report,
   and write one sentence saying what the function returned and what the test expected.
4. **Undo the change.** Run pytest again: `3 passed`.

### C4 — Commit

```text
$ git add test_bill_splitter.py RESULTS.md
$ git commit -m "Add tests for Bill Splitter"
$ git pull
$ git push
```

✅ **Self-check:** `git status` says `nothing to commit, working tree clean`, and does
**not** list a `__pycache__/` folder. If it does, the repository is missing a `.gitignore`
— see Part D1.

---

## Part D — Your real project

Now the same moves, for marks that matter more than 2%: **one of the three functions you
own in your proposal, plus its test, in your team's real `project.py` and
`test_project.py`** at the top level of the repository.

### D1 — Does the skeleton exist? (one person per team)

If your repository **already has** `project.py` and `test_project.py` at the top level,
skip to D2.

If not, **one** member — agree who in your team chat first — creates them, plus a
`.gitignore`, and pushes them **before** anyone starts D2:

```python
# project.py
def main():
    """Run the program."""
    print("Project coming soon")


if __name__ == "__main__":
    main()
```

```python
# test_project.py
import project
```

```text
# .gitignore
__pycache__/
```

```text
$ git add project.py test_project.py .gitignore
$ git commit -m "Add project and test skeletons"
$ git push
```

Everyone else: `git pull` and check the files appeared.

### D2 — Add your function and its test

1. `git pull` — always first.
2. In `project.py`, add **one function you own**, at the same indentation as `main`,
   **above** the `if __name__` guard, with a **docstring**. It must take parameters and
   **return** a value — no `input()`, no `print()`.
3. In `test_project.py`, import it (`from project import <your_function>`) and add
   **`test_<your_function>`** with at least **two** asserts, one of them an edge case.
4. From the **top level** of the repository, both of these must work:

   ```text
   $ python3 -m pytest test_project.py -v
   $ python3 project.py
   ```

5. Commit, pull, push:

   ```text
   $ git add project.py test_project.py
   $ git commit -m "Add <your_function> and its test"
   $ git pull
   $ git push
   ```

### D3 — If `git pull` reports a conflict

Likely, if your teammates are doing D2 at the same moment:

```text
CONFLICT (content): Merge conflict in project.py
```

1. Open `project.py`. Find the `<<<<<<<`, `=======` and `>>>>>>>` lines.
2. You almost certainly want **both** sides — your function *and* theirs. Delete just the
   three marker lines (or click VS Code's **Accept Both Changes**), leaving two blank lines
   between functions.
3. Run `python3 -m pytest test_project.py` — it must pass.
4. `git add project.py`, `git commit -m "Merge teammate's changes"`, `git push`.

If a full-screen editor appears after `git pull`, Git wants a message for the merge: in
*vim* type `:wq` and press Enter; in *nano* press Ctrl+X.

### D4 — Record it

On GitHub, open your repository → **Commits** → click your D2 commit. Copy its URL into
**D** in `RESULTS.md`, with the function's name. Commit and push `RESULTS.md`.

✅ **Self-check:** on GitHub, `project.py` contains your function, and the commit that
added it shows **your** username.

---

## 🐛 Trace and explain

Answer in `RESULTS.md`, in your own words. No code needs to run for these.

### Q1 — Which lines print?

`helpers.py`:

```python
print("A")


def double(n):
    """Return n doubled."""
    return n * 2


if __name__ == "__main__":
    print("B")
```

`app.py`, in the same folder:

```python
from helpers import double

print("C", double(4))
```

What does `python3 app.py` print, and what does `python3 helpers.py` print? Explain the
difference in one or two sentences.

### Q2 — The suspiciously green test

A teammate's `test_bill_splitter.py` is:

```python
from bill_splitter import share, tip_amount


def test_share():
    share(30, 3) == 10.0


def tip_test():
    assert tip_amount(100, 15) == 15.0
```

pytest reports `1 passed`. Name **two** reasons this is not good news, and fix both.

### Q3 — Rejected

You run `git push` and see:

```text
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
```

What happened, and what two commands do you run next? What must you check **before**
the second one if the first reports `CONFLICT`?

Commit and push `RESULTS.md` when you have answered all three.

---

## ⭐ Bonus — tests that run themselves (0 marks)

GitHub can run your team's tests on **every push** and show a ✅ or ❌ next to each commit.
**One** member creates `.github/workflows/tests.yml` at the top level:

```yaml
name: tests
on: [push, pull_request]
jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m pip install pytest
      - run: python -m pytest test_project.py
```

Push it, then open the **Actions** tab. Now break a test on purpose and push: who gets the ❌?

---

## Checklist — what I look for

All from **your** GitHub account, in your team repository, by **Thu Dec 3, 11:59 PM**:

- ☐ `practice/<your-github-username>/RESULTS.md` — A1, B4, C3, D and Q1–Q3 all filled in.
- ☐ `practice/<your-github-username>/bill_splitter.py` — runs and matches B2.
- ☐ `practice/<your-github-username>/test_bill_splitter.py` — three test functions, all
  passing, at least 8 asserts in total.
- ☐ One of **your** functions, with a docstring, in the top-level `project.py`, and its
  `test_…` in `test_project.py` — passing.
- ☐ At least **four commits** by you, each with a message that says what changed.

**Pass** = all five boxes ticked, with at least 80% of the work correct.

## What's next

Part D is the start of your project, not a one-off. Your other two functions go in the
same way: **pull → write → test → commit → pull → push**. In Week 13 we polish the code
style, and the project is due **Tuesday, December 8**.
