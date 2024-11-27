
# Python Programming Exercises

## Exercise 1: Write a Python program to determine a student's eligibility to sit for an exam based on their attendance.
**Object Name:**  
Write a program called `q1.py`

**Input:**  
The program should contain a function called `check_exam_eligibility` that takes two integers as input from the user:  
1. The number of classes held (`total_classes`).  
2. The number of classes attended (`classes_attended`).  

**Expected Output:**  
The program should calculate the percentage of classes attended and output:  
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

---

## Exercise 2: Write a Python program to verify if a number is a three-digit number.
**Object Name:**  
Write a program called `q2.py`.  

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

---

## Exercise 3: Write a Python program to create a basic multiple-choice quiz application with three levels of difficulty.
**Object Name:**  
Write a program called `q3.py`.  

**Description:**  
This program is a Python quiz application that asks the user multiple-choice questions, checks their answers, and displays the final score. The quiz includes three levels of difficulty: Easy, Average, and Hard.

**Input:**  
Use a function called `python_quiz_application` that performs the following:  
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
