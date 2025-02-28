# **Python Programming: Lab Activity 4**

**Due Date:** 7/03/2025

## **Objective**
This lab focuses on **Functions, loops, Lists and Modules** in Python. The exercises are designed to enhance your understanding of:
- Defining and using functions to perform specific tasks
- Using loops for repeated actions
- Handling user input and performing basic operations on it
- Working with the random and math module to generate random values
- Creating and manipulating 2D lists (matrices) to represent structured data


## **Assignment Tasks**

### Q1: Find the largest number
- Define a function called `max_of_three()` that prompts users to enter three integer inputs, and return the largest number on the screen. (4 points)

Example output
```
Enter the first number: 12
Enter the second number: 45
Enter the third number: 23

The largest number is: 45
```

### Q2: Check palindrome
- Define a function isPalindrome() that takes an integer num1 from the user and checks whether the number is a palindrome (a number that reads the same forwards and backwards). The function should return `True` if the number is a palindrome, and `False` otherwise. 
- For example, if the input is 121, the output should be True, and if the input is 123, the output should be False (4 points).

Note: Do not print("True") or print("False"). Return a boolean object.

Example output
```
Enter a number: 121
Output: True
```

```
Enter a number: 123
Output: False
```

### Q3: Random number guessing game
- Write a program that generates a random number in the range of 1 through 100, and asks the user to guess what the number is.
- If the user’s guess is higher than the random number, the program should print “Too high, try again”.
- If the user’s guess is lower than the random number, the program should print “Too low, try again”.
- If the user guesses the number, the application should print "Congratulations! You guessed it!". (6 points)

Example output

```
Guess a number between 1 and 100: 50
Too high, try again.

Guess a number between 1 and 100: 30
Too low, try again.

Guess a number between 1 and 100: 40
Congratulations! You guessed it!
```

### Q4: Find the square root
- Write a Python function that takes a number from the user and prints its square root using the math module. If the user enters a negative number, raise a `ValueError` with a message of your choice

(5 points)

Example output
```
Enter a number: 16
4.0
```
```
Enter a number: -3
Traceback (most recent call last):
  File "/Users/.../lab4.py", line 15, in <module>
    calculate_square_root()
  File "/Users/.../lab4.py", line 8, in calculate_square_root
    raise ValueError("Cannot calculate the square root of a negative number.")
ValueError: Cannot calculate the square root of a negative number.

```
### Q5: Create a Matrix
- Write a Python program that creates a 2D list (a list of lists) to represent a matrix. 
- Begin by asking the user to input the number of rows and columns for the matrix. 
- Ensure that the inputs are positive integers. 
- Then, create an empty matrix with the specified number of rows and columns. 
- Use nested loops to fill the matrix by prompting the user to enter values for each cell in the matrix. - After the matrix is filled, print the matrix to display the values in a readable format, where each row appears on a new line (6 points)

Example output
```
Enter the number of rows: 2
Enter the number of columns: 3
Enter value for position (1, 1): 1
Enter value for position (1, 2): 2
Enter value for position (1, 3): 3
Enter value for position (2, 1): 4
Enter value for position (2, 2): 5
Enter value for position (2, 3): 6

The matrix you entered is:
[1, 2, 3]
[4, 5, 6]
```

## **Submission Guidelines**
1. Submit the provided file lab4.py with exsiting template code.
2. **Do not make any changes in the template code provided.** Please only fill the said places in the file
3. Ensure that your program runs correctly before submission.
4. Please do not rename the file.


## **Grading Criteria**
- **Correctness:** Output must match the expected results exactly.
- **Completeness:** All tasks must be completed as per instructions.
- **Efficiency:** Code should be optimized where possible.
- **Readability:** Use proper indentation and comments to explain logic.
- **Originality:** Avoid plagiarism—write your own code.