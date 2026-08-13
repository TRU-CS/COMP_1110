# Python Programming Exercises

**General Assignment Instructions:**

- A template code is provided for each file.
- Each file contains some pre-written code along with placeholders for you to add your code.
- Only write code in the designated sections. Avoid modifying the existing code or predefined variables outside these areas.

## Exercise 1: Write a Python program to determine a student's eligibility to sit for an exam based on their attendance.

**Object Name:**
You have been provided with a file `q1.py`

**Input:** The program should contain a function called `check_exam_eligibility` that takes two integers as input from the user:

1. The number of classes held (`total_classes`).
2. The number of classes attended (`classes_attended`).

**Expected Output:** The program should calculate the percentage of classes attended and output:

1. The percentage of classes attended (formatted to 2 decimal places).
2. Whether the student is permitted to take the exam (attendance ≥ 90%) or not permitted.

For example:
If the user inputs `total_classes = 50` and `classes_attended = 45`, the output should be:

```
Percentage of classes attended: 90.00%
You are permitted to take the exam.
```

If the user inputs `total_classes = 50` and `classes_attended = 40`, the output should be:

```
Percentage of classes attended: 80.00%
You are not permitted to take the exam.
```

**Edge cases**

When user inputs the total number of classes less or equal than 0, the program should also print out a meaningful message "The number of total classes must be greater than 0."

---

## Exercise 2: Write a Python program to verify if a number is a three-digit number.

**Object Name:**
You are provided with a file `q2.py`.

**Input:**
The program should contain a function called `check_three_digit` that takes a single integer `num` as input from the user.

**Expected Output:**
The program should output whether the number is a three-digit number or not, along with an appropriate message.

For example:
If the user inputs `123`, the output should be:

```
123 is a three-digit number.
```

If the user inputs `45`, the output should be:

```
45 is not a three-digit number.
```

**Edge cases**

When user inputs non-valid input such as a string instead of a number, the program should catch the `ValueError` exceptions and print out a meaningful message "Invalid input. Please enter a valid integer."

---

## Exercise 3: Write a Python program to create a basic multiple-choice quiz application with three levels of difficulty.

**Object Name:**
You are provided with a file `q3.py`.

**Description:**
This program is a Python quiz application that asks the user multiple-choice questions, checks their answers, and displays the final score. The quiz includes three levels of difficulty: Easy, Average, and Hard.

**Input:** Use a function called `python_quiz_application` that performs the following:

1. The program should first ask for the user's name.
2. The user should then select the difficulty level (Easy, Average, or Hard).
3. For the selected level, the program should display five multiple-choice questions, each with four options. The user will enter the chosen option (e.g., A, B, C, or D) for each question.

**Output:**

1. If the user's answer is correct, the program increments a score variable (`calculateResult`) by 1.
2. If the user's answer is incorrect, display a message like `Invalid choice`.
3. At the end of the quiz, display the user's name and their total score.

For example:
If the user inputs:

```
Name: Alex 
Level: Easy 
Question 1: What is the output of 2 + 2? 
A. 3 
B. 4 
C. 5 
D. 6 
Enter your choice: B
.
.
.
.
(repeats for five questions)
```

The final output should display:

```
Player: Alex 
Your total score is: 4 out of 5
```

**Do NOT change the order of the questions**

### Easy Questions

1. What is the capital of France?

a) Paris
b) London
c) Rome
d) Berlin

> Answer: a

2. What color are bananas?

a) Red
b) Yellow
c) Green
d) Blue

> Answer: b

3. 2 + 2 = ?

a) 3
b) 5
c) 1
d) 4

> Answer: d

4. Which planet is known as the Red Planet?

a) Mars
b) Venus
c) Earth
d) Jupiter

> Answer: a

5. How many days are there in a week?

a) 5
b) 6
c) 7
d) 8

> Answer: c

### Average Questions

1. What is the capital of Canada?

a) Vancouver
b) Montreal
c) Ottawa
d) Toronto

> Answer: c

2. Which is the largest ocean on Earth?

a) Indian
b) Pacific
c) Atlantic
d) Arctic

> Answer: b

3. Which element has the atomic number 1?

a) Hydrogen
b) Oxygen
c) Helium
d) Carbon

> Answer: a

4. How many continents are there?

a) 5
b) 6
c) 7
d) 8

> Answer: c

5. Who wrote 'Hamlet'?

a) Shakespeare
b) Tolstoy
c) Hemingway
d) Dickens

> Answer: a

### Hard Questions

1. What is the square root of 144?

a) 10
b) 11
c) 12
d) 13

> Answer: c

2. What is 10^3?

a) 1000
b) 100
c) 10
d) 10000

> Answer: a

3. In which year did World War I begin?

a) 1923
b) 1914
c) 1900
d) 1939

> Answer: b

4. What is the boiling point of water in Celsius?

a) 0
b) 50
c) 100
d) 212

> Answer: c

5. What is the derivative of x^2?

a) x
b) 2x
c) x^2
d) x^3

> Answer: b
