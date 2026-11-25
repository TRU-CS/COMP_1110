# Group Final Project

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

- **A `main()` guarded by `if __name__ == "__main__":`**, so that `pytest` can import
  `project.py` without running it *(Week 12)*
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
| 3 | **Oral examination** — 5 minutes per member, in your team's time slot; you explain the functions you wrote | Tue Dec 8 / Thu Dec 10 (see [§5](#oral-exam)) | **12%**, marked individually |
| 4 | **Final submission** — `project.py`, `test_project.py`, `requirements.txt`, `README.md`, AI Studio app link | **Tue Dec 8, 11:59 PM** | **10%** × peer factor |
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

#### Setting up your team repository

Do this before you submit the proposal, so the URL in point 5 already works. **One member**
creates the repository; everyone else joins it as a collaborator.

**1. Every member** — have a GitHub account, and send your username to the teammate creating
the repository.

**2. One member creates the repository**

- Sign in to [github.com](https://github.com), click **+** (top right) → **New repository**.

```{image} img/github/repo-create-global-nav-update.png
:alt: The + menu with New repository highlighted
:width: 40%
```

- **Repository name**: something short and descriptive, e.g. `comp1110-budget-tracker`.

```{image} img/github/create-repository-name.png
:alt: The Repository name field
:width: 80%
```

- Set it to **Public**.
- Tick **Add a README file**, so the repository is not empty and can be cloned straight away.
- **Add .gitignore** → choose **Python**.
- Click **Create repository**.

**3. The same member adds the others as collaborators**

- In the repository, open **Settings** → **Collaborators** (under *Access*). GitHub may ask
  for your password again.

```{image} img/github/repo-actions-settings.png
:alt: The repository tabs with Settings highlighted
:width: 100%
```

- Click **Add people**, type a teammate's GitHub username, and click **Add … to this
  repository**. Repeat for each teammate.

**4. Every other member accepts the invitation** — it arrives by email and also appears at
`github.com/<owner>/<repo>/invitations`. Until you accept it, you cannot push. The invitation
expires after 7 days; if it does, ask for a new one.

*Screenshots: [GitHub Docs](https://docs.github.com), CC BY 4.0. Your screen may differ slightly.*


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
| **Oral examination** | **12%** | Team time slot, **marked individually** |
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
GitHub commit history, the ownership plan in your proposal, and your oral examination. Retaliatory
ratings, collusive ones — *"we all give each other 5"* — and ratings with no justification are
**discarded**. Submit no peer assessment and you receive a **1.00** factor yourself and forfeit
any say about your teammates.

---

(oral-exam)=
## 5. Oral examination

**12% of your final grade, marked individually.** There is no team presentation. Instead, each
team has one time slot with **5 minutes per member**: a team of 3 gets 15 minutes, a team of 4
gets 20, and a team of 2 gets 10. The whole team comes in together, and I examine each member in
turn.

### What happens

I open your repository and ask you to **explain the functions you wrote**: the ones your proposal
and README list against your name, and that the commit history shows you committing. Then I ask a
few questions about them, for example:

- What does this line do? Why is it here?
- What happens if the input is empty, negative, or the wrong type?
- Why did you use a dictionary (or list, or loop) here and not something else?
- Which test checks this function, and what does it check? What case does it miss?
- How would you change it to do *X*?

Only **you** answer questions about your functions; your teammates cannot answer for you. If you
cannot explain code that your commits say you wrote, that affects this mark and can affect your
peer factor ([§4](#the-peer-factor)).

### How to prepare

- Know every line of your own functions and their tests well enough to explain them without notes.
- Be ready to run your tests (`pytest test_project.py`) and your program (`python3 project.py`)
  on the spot.
- Read your teammates' functions too, so that you know how yours fit into `main()`.
- If you used AI, a tutorial, or a classmate's help, be ready to explain that code as if you had
  written it yourself, and list it in the README's **Sources** section.

### Rules

- Bring a laptop with your repository cloned and Python and `pytest` installed. I will also have
  your repository open on my screen.
- **Arrive 5 minutes early** and wait outside. Slots run back to back, so a late start cannot run
  over into the next team's time.
- A slot **cannot be swapped or made up** without an approved academic concession. A member who
  misses the team's slot loses this 12%. Teams that want to swap slots with each other must both
  email me **by Thu Dec 3**.

### Schedule

Teams were placed in slots at random. Your group number is your group on Moodle.

**Tuesday, December 8** (9:30–11:20)

| Time | Group |
| :--- | :--- |
| 9:30–9:40 | **Group 10** |
| 9:40–10:00 | **Group 3** |
| 10:00–10:15 | **Group 20** |
| 10:15–10:30 | **Group 19** |
| 10:30–10:45 | **Group 15** |
| 10:45–11:05 | **Group 2** |
| 11:05–11:20 | **Group 18** |

**Thursday, December 10** (9:30–12:20, in the scheduled final exam slot)

| Time | Group |
| :--- | :--- |
| 9:30–9:45 | **Group 7** |
| 9:45–10:00 | **Group 12** |
| 10:00–10:20 | **Group 9** |
| 10:20–10:40 | **Group 11** |
| 10:40–10:55 | **Group 13** |
| 10:55–11:05 | **Group 17** |
| 11:05–11:20 | **Group 8** |
| 11:20–11:35 | **Group 6** |
| 11:35–11:50 | **Group 4** |
| 11:50–12:05 | **Group 16** |
| 12:05–12:20 | **Group 1** |


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

#### Interactive app: <Google AI Studio app URL>
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
Why a dictionary here, why a list there, what you tried first and abandoned.
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

(ai-studio-app)=
## 7. Interactive app (Google AI Studio)

There is **no demo video**. Instead, you turn your program into an **interactive web app** with
[Google AI Studio](https://aistudio.google.com) and put the app's link at the top of your README.
Anyone who opens the link should be able to use your program in a browser without installing
Python.

### What is required

- A working AI Studio app that does **what your `project.py` does**: same inputs, same rules,
  same results. You can give it buttons, menus, and text boxes instead of typed input.
- A link to it on the **`#### Interactive app:`** line of your README (see the template in
  [§6](#repository-readme)). Test the link from a browser where you are **not** signed in, or ask
  a classmate to open it. If I cannot open it, it counts as missing.
- A sentence in the README's **Sources** section saying the app was generated with Google AI
  Studio, and anything you changed by hand.

**`project.py` and `test_project.py` are still what I mark for code, tests, and design.** AI
Studio writes the app in its own language (usually TypeScript), not Python, and that generated
code is not graded. The app is how people use your work; the Python is how you show you can
write it.

### How to build and publish it

One team member does this, signed in with a personal Google (Gmail) account. TRU does not
provide Google accounts, so if nobody on your team has one, create a free one at
[accounts.google.com](https://accounts.google.com).

**1. Open Build mode.** Go to [aistudio.google.com](https://aistudio.google.com) and click
**Build** in the left-hand menu.

**2. Describe the app and give it your code.** In the prompt box, paste a prompt like the one
below, then paste the full contents of your `project.py` underneath it:

```text
Turn the Python program below into a simple interactive web app.
- Keep the exact same logic, rules, and results as the Python code.
  Do not add new features.
- Show the same error messages when the user gives bad input.
- Put the title "<project title>" and the names "<name, name, name>" at the top.

<You can add more customized design prompts here such as make it a vintage game, make the theme starworld, etc...>

<paste project.py here>
```

**3. Check that it behaves like your program.** The app appears in the preview on the right.
Try the same inputs you use in `test_project.py`, including the bad ones, and compare the
results with `python3 project.py`. If something is wrong, tell it in the chat box, e.g.
*"With input 7 the Python prints 49 but the app shows 14. Fix it to match the Python."* Repeat
until they agree.

**4. Publish it.** Click **Publish** (top right). Accept the suggested web address or type your
own (for example `comp1110-budget-tracker`), then click **Publish App**. After a minute or two
you get a public URL. Open it in a private/incognito window to check that it works.

- Publishing is free on AI Studio's **Starter Tier** (up to two apps per account), with no
  credit card. If your account is not offered it, try a teammate's account. **Do not add a
  credit card or billing account for this course.**
- If nobody on your team can publish, use **Share** instead: share the app so that
  *anyone with the link* can view it, and put that link in your README. Tell me in the README
  that it is a share link.

**5. Paste the URL into your README** on the `#### Interactive app:` line, then commit and push.

**6. If you change `project.py` later**, open the app in AI Studio again, paste the new code with
*"Update the app to match this new version"*, check it again, and publish again. The URL stays
the same.

*AI Studio changes often, so a button may have moved or been renamed. Google's own instructions
are [Build apps in Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
and [Deploy apps from AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying).*

---

*Acknowledgement: the file structure (`project.py`, `test_project.py`, `requirements.txt`), the
README requirement, the Good/Better/Best framing, and the
scope–correctness–design–style grading axes are adapted from Harvard University's
[CS50P final project](https://cs50.harvard.edu/python/project/), scaled here to a three-person
team in a first course.*
