# Python Programming Assignment 3

**General Assignment Instructions:**

- A template code is provided for each file.
- Each file contains some pre-written code along with placeholders for you to add your code.
- Only write code in the designated sections. Avoid modifying the existing code or predefined variables outside these areas.

---

## Exercise 1: Find a Missing Number in a List

**Object Name:**  
You have been provided with a file `q1.py`.

**Input:**  
The program should contain a function called `find_missing_number` that performs the following:
1. Takes a list of numbers (`numbers_list`) as input. The list contains a range of numbers from 0 to `n` with one missing number.

**Expected Output:**  
The program should identify and return the missing number. If no number is missing, return an appropriate message.

**Examples:**  
- Input: `[0, 1, 2, 4, 5]`  
  Output: `The missing number is: 3`

- Input: `[1, 2, 3, 4]`  
  Output: `The missing number is: 0`

- Input: `[0, 1, 2, 3, 4]`  
  Output: `No missing numbers in the list.`

---

## Exercise 2: Split a List into Two Parts

**Object Name:**  
You have been provided with a file `q2.py`.

**Input:**  
The program should contain a function called `split_list` that performs the following:
1. Takes two parameters:
   - `input_list`: The list to be split.
   - `split_length`: The length of the first part of the list (an integer).

**Expected Output:**  
The program should:
1. Split the list into two parts:
   - The first part containing `split_length` elements.
   - The second part containing the remaining elements.
2. Handle cases where `split_length` is greater than the length of the list or less than 0 with an appropriate message.

**Examples:**  
- Input: `[1, 2, 3, 4, 5]`, `split_length = 3`  
  Output:  
  First part: `[1, 2, 3]`  
  Second part: `[4, 5]`

- Input: `[1, 2, 3, 4, 5]`, `split_length = 6`  
  Output: `Invalid input. The split length exceeds the length of the list.`

- Input: `[1, 2, 3, 4, 5]`, `split_length = -1`  
  Output: `Invalid input. The split length cannot be negative.`

---

## Exercise 3: Remove Duplicate Numbers from a List

**Object Name:**  
You have been provided with a file `q3.py`.

**Input:**  
The program should contain a function called `remove_duplicates` that performs the following:
1. Takes a list of numbers (`numbers_list`) as input.

**Expected Output:**  
The program should return a new list with duplicate numbers removed while preserving the original order of elements.

**Examples:**  
- Input: `[1, 2, 2, 3, 4, 4, 5]`  
  Output: `List after removing duplicates: [1, 2, 3, 4, 5]`

- Input: `[10, 10, 10]`  
  Output: `List after removing duplicates: [10]`

- Input: `[]`  
  Output: `List after removing duplicates: []`

---

## Exercise 4: Generate and Return a List of Squares

**Object Name:**  
You have been provided with a file `q4.py`.

**Input:**  
The program should contain a function called `generate_squares` that:
1. Generates a list where the values are the squares of numbers from 1 to 30 (both included).

**Expected Output:**  
The program should return the list of squares.

**Example:**  
Output:  
`[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]`

---

## Exercise 5: Adjusted Average After Dropping the Lowest Score

**Object Name:**  
You have been provided with a file `q5.py`.

**Input:**  
The program should contain a function called `calculate_adjusted_average` that performs the following:
1. Accepts a list of student test scores (`scores`).

**Processing:**  
The program should:
1. Calculate the total of the scores.
2. Find the lowest score.
3. Subtract the lowest score from the total to get the adjusted total.
4. Divide the adjusted total by one less than the number of test scores to compute the average.

**Expected Output:**  
The program should return the calculated average.

**Examples:**  
- Input: `[78, 85, 62, 90]`  
  Output: `84.33`

- Input: `[70, 70, 70, 70]`  
  Output: `70.0`

- Input: `[60, 90]`  
  Output: `90.0`

**Edge Cases:**  
- If there are fewer than two scores, the program should raise a meaningful error: `At least two scores are required to calculate an adjusted average.`