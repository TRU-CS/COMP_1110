# COMP 1110 — Group Final Project (25%)

---

## 1. The project

### What you are building

Your project is a **Python program of your own**, subject only to the
requirements below. There is no prescribed subject, a game, a tool, a simulation, or a program that works entirely from typed input all qualify.

Build it with the tools of this course. It does **not** need a web server, a database, or a
graphical interface; none of those earn marks by themselves. A plain text program that does one
thing well, survives bad input, and is properly tested will score better than an ambitious app
that is half finished.

### Required files

Your project must be implemented in **Python**. 

- **`project.py`**, in the top-level folder of your repository, containing a **`main` function**.
- **At least nine other functions of your own in `project.py`** — three per team member —
  defined at the **same indentation level as `main`**, not nested inside another function or a
  class.
- **`test_project.py`**, also in the top-level folder, holding a test for each of those nine
  functions, **runnable with `pytest`**. A test is named after the function it tests with
  `test_` in front: `average_mark` is tested by `test_average_mark` *(Week 8)*.
- **`requirements.txt`**, listing any pip-installable library your project needs, one per line,
  so that somebody else can run `pip install -r requirements.txt`. If you use nothing beyond the
  standard library, submit the file empty with a comment saying so.
- **`README.md`** — see [§6, Repository & README](#repository-readme).

You may add as many further files, functions, and classes as you like; those four files are the
minimum, and they are what I run first.

### Required content

- **At least one class of your own design** *(Week 12)*
- Tests written as **`pytest` functions using `assert`** *(Week 8)*
- **A docstring on every function** *(Week 8)*
- **PEP 8-conformant formatting** *(Week 13)*
- **A public GitHub repository** with commits from every member under their own account

### Project layout

```
your-repo/
├── project.py          main() + at least 9 of your own functions
├── test_project.py     test_<name> for each of those functions
├── README.md           your design document, around 500 words
```

Run it with `python3 project.py`, and run your tests with `pytest test_project.py` from the
top-level folder. Every test must pass on a clean checkout of your repository — if a test needs a
data file, that file belongs in the repository too.

And, the two required files look like this in outline:

```python
# project.py
def main():
    ...


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
```

```python
# test_project.py
def test_function_1():
    ...


def test_function_2():
    ...


def test_function_n():
    ...
```

You are welcome to implement additional classes and functions as you see fit beyond the minimum.

---

## 2. Your team

### Forming your team

The final project is a **group build, individually graded**. 

- **Teams of 3** (4 by arrangement). You **self-form** — pick your own teammates.
- If you are not in a team by Thursday Oct 1, I will assign you



### The teamwork contract

**One page**, one document per team, submitted to **Moodle by Sunday, Oct 4, 11:59 PM**. It is
ungraded, but every team has to file one.

Write it **as a team**, answering each question in a sentence or two. One page is the limit, so
keep the answers short.

#### What to write

**1. Team members** — the three (or four) names, and how to reach each of you.

**2. Expectations**

- How many hours per week each of us commits to the project, meetings included.
- How far ahead of a deadline our tasks are finished.
- What we do if someone cannot finish on time — who they tell, and how soon.

**3. Communication**

- When and where we meet in person (a standing weekly slot, not "when we can").
- The one tool we use for day-to-day messages.
- How quickly a message gets a reply on a normal day.

**4. Splitting the work** — how we decide who does what, and how we can tell what is finished.
From Week 6 this moves into GitHub; for now, a shared document is fine.

**5. If the contract is broken** — our agreed **three steps**, in order. Step 3 is normally "we
bring it to the instructor", and steps 1 and 2 are what we try first.

**6. Values** — each member lists **three** personal values they bring to the team (for example
*reliability*, *curiosity*, *honesty*, *patience*, *fairness*, *humour*) with one line saying
what that looks like in practice.

**7. Signatures** — each member types their name and the date.


---

## 3. Milestones

CS50 splits its final project into a series of small checkpoints — a proposal, a status report,
then the implementation — so that a project going off course is caught early. This project is
organised the same way.

### Timeline

| # | Milestone | Due | Graded? |
| :--- | :--- | :--- | :--- |
| 0 | **Team formed + Teamwork Contract** — 1 page, from the team | Thu Oct 1 (names) · Sun Oct 4 (contract) | Required, ungraded |
| 1 | **Project proposal** — 1 page, from the team | **Thu Nov 5** | **3%** |
| 2 | **Status report** — 2 pages max, from the team | Thu Nov 19 | Required, ungraded |
| 3 | **Presentation & Q&A** — your own segment | Thu Dec 3 / Tue Dec 8 | **12%**, individual |
| 4 | **Final submission** — `project.py`, `test_project.py`, `requirements.txt`, `README.md`, video link | **Tue Dec 8, 11:59 PM** | **10%** × peer factor |
| 4b | **Peer assessments** — confidential, individual | Tue Dec 8, 11:59 PM | Sets your peer factor |



### Milestone 1 — the proposal (3%, team)

**One page**, due **Thursday, November 5**, one submission per team:

1. **The problem** you are solving, in a paragraph a non-programmer could follow.
2. **Inputs** — a file? typed input? both? — and **outputs**.
3. **The functions you plan to write** — names and one-line descriptions, 8–15 of them.
4. **Who owns what** — every member's name against the parts they will write.
5. **Your GitHub repository URL** (public).

The ownership plan matters well beyond the 3%: at the end of term I read it next to the commit
history and the peer assessments. Three documents that agree tell a clear story.


### Milestone 2 — the status report (ungraded, required)

**Two pages maximum**, one submission per team, to Moodle on **Thursday, November 19**:

1. What works today.
2. What does not work yet.
3. What has changed since the proposal.
4. Who has pushed commits in the last two weeks.
5. Anything you need from me.

Points 4 and 5 are the reason it exists. There is still time to act on a problem reported in
November; in December there is not.

---

## 4. Grading

### How your individual grade is computed

| Component | Weight of your **final grade** | Team or individual |
| :--- | :--- | :--- |
| **Project proposal** | **3%** | One team submission |
| **Team deliverable** — code, tests, documentation | **10%** | One team mark × **your** peer factor |
| **Presentation & Q&A** | **12%** | **Entirely individual** |
| **Total** | **25%** | |


### The peer factor

At submission, every member confidentially rates each teammate — **and themselves** — on
contribution, reliability, communication, and code quality, with a brief written justification.

Those ratings average into a **peer factor**, normally between **0.75 and 1.10**, applied to your
share of the 10% team deliverable:

| Situation | Factor |
| :--- | :--- |
| Contributed fully | **1.00** |
| Carried substantial extra load | up to **1.10** |
| Repeatedly missed commitments | **0.75** or below |
| Contributed essentially nothing (documented) | may be **0** |

**Ratings are corroborated, not taken at face value.** I check every peer assessment against the
GitHub commit history, the ownership plan in your proposal, and your Q&A performance. Retaliatory
ratings, collusive ones — *"we all give each other 5"* — and ratings with no justification are
**discarded**. Submit no peer assessment and you receive a **1.00** factor yourself and forfeit
any say about your teammates.

---

## 5. Presentation & Q&A

**12% of your final grade, entirely individual.** Each team gets **10 minutes** in class on
**Thu Dec 3** or **Tue Dec 8**: a live demo, a segment from every member, then open Q&A.

### The demo video
- Create a 3 mins video to demonstrate your project in action, as with slides, screenshots, voiceover, and/or live action.
- You can use Microsoft Teams to record your screen and share a link of the recording. 
- Open with a title card giving the
**project title**, **all team members**, and the **date recorded**, then show
the program running.


---

(repository-readme)=
## 6. Repository & README

### GitHub

Every team keeps its code in a **public GitHub repository**, and every member **commits and
pushes their own contributions under their own GitHub account**. Do not have one person push on
everyone's behalf.

**The commit history is the evidence of your contribution** — it is what I check when I
corroborate peer assessments. Commit as you go, in reasonably sized pieces with meaningful
messages, rather than in a single push at the end.

Because every repository is public, you can read other teams' code. **You may not copy from it.**
See [Academic Integrity](syllabus.md#academic-integrity).

### README

README is the project's design document rather than a label on it: several
paragraphs, **around 500 words**, covering what the project is, what each file does, and why you
made the design choices you made. Write it as you build — a README written on Dec 8 reads like
one, and it is worth real marks.

```markdown
# Project title

#### Video demo: <YouTube URL>
#### Team: name, name, name — COMP 1110, Fall 2026
#### Repository: <GitHub URL>

## Description
What the project does, and for whom. Several paragraphs.

## The files
project.py — what main() does, and what each of your functions is for.
test_project.py — what each test checks.
requirements.txt — which libraries, and why you need them.
data/ — what is in it and where it came from.

## Design decisions
Why a dictionary here, why a class there, what you tried first and abandoned.
This is the section I read most closely. Explain your reasoning, not just your
structure.

## How to run it
pip install -r requirements.txt
python3 project.py

## How to run the tests
pytest test_project.py

## Known limitations
What it does not handle yet. Saying so scores better than staying quiet about it.

## Individual contributions
Name — which functions they wrote.

## Sources
Any external code, tutorial, or documentation you drew on, and where it is used.
```

---

*Acknowledgement: the file structure (`project.py`, `test_project.py`, `requirements.txt`), the
README and demo-video requirements, the Good/Better/Best framing, and the
scope–correctness–design–style grading axes are adapted from Harvard University's
[CS50P final project](https://cs50.harvard.edu/python/project/), scaled here to a three-person
team in a first course.*
