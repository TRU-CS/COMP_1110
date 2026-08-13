

## 1. Set up Your Assignment Files Locally

1. **Create your assignment folder structure**  
   - Inside your assignment folder (e.g., `assignment1/`), create:
     - A `student/` folder containing the **template code** (e.g., `q1.py`, `q2.py`, `q3.py`) that students will fill in.
     - A `solutions/` folder containing **solution code** for each question (e.g., `q1_solution.py`, `q2_solution.py`, `q3_solution.py`). This is only for your reference/testing, not distributed to students.
     - A `test/` folder where each test file (e.g., `testq1.py`, `testq2.py`, `testq3.py`) will reside. These tests use Python’s `unittest` framework to check correctness.
     - Other required files at the top level:
       - `requirements.txt`  
       - `setup.sh`  
       - `run_autograder`  
       - `run_tests.py` or `run_test.py` (depending on your naming)
       - `README.md` (documentation for your reference)

   Your folder might look like this:
   ```
   assignment1/
   ├── student/
   │   ├── q1.py
   │   ├── q2.py
   │   └── q3.py
   ├── solutions/
   │   ├── q1_solution.py
   │   ├── q2_solution.py
   │   └── q3_solution.py
   ├── test/
   │   ├── testq1.py
   │   ├── testq2.py
   │   └── testq3.py
   ├── setup.sh
   ├── requirements.txt
   ├── run_autograder
   ├── run_test.py
   └── README.md
   ```

2. **(Optional but recommended) Provide a template code**  
   - Make sure the `student/` folder contains starter code (functions, docstrings, placeholders) so students know where to write their solutions.  
   - This helps ensure consistency between all student submissions.

3. **Write (or finalize) your own solutions**  
   - Store working solutions in `solutions/`, matching the function signatures and approach you expect from students.

---

## 2. Define Your Tests with `unittest`

1. **Create test files** in the `test/` folder, one per question or logical grouping. For example:
   ```python
   # testq1.py
   import unittest
   from gradescope_utils.autograder_utils.decorators import weight
   import q1  # or your function from q1.py

   class TestQ1(unittest.TestCase):
       @weight(10)
       def test_eligibility_case1(self):
           # Example: check if q1 function returns correct result for a sample input
           self.assertEqual(q1.check_exam_eligibility(50), True)

       @weight(10)
       def test_eligibility_case2(self):
           self.assertEqual(q1.check_exam_eligibility(10), False)

       # More test methods...
   ```
   - Decorate each test method with `@weight(…)` indicating the number of points it contributes.
   - Make assertions that test the correctness of student solutions (e.g., `assertEqual`, `assertTrue`, etc.).

2. **Repeat for other files** (`testq2.py`, `testq3.py`) as needed.


## 3. Specify Python Dependencies

1. **requirements.txt**  
   - List all Python packages your autograder code depends on (e.g., `gradescope-utils`, `numpy`, `pandas`, etc.).  
   - For a basic Python assignment, `gradescope-utils` might suffice:
     ```
     gradescope-utils
     ```

2. **setup.sh**  
   - A shell script that installs system-level requirements or other dependencies. For a Python-based autograder, it might look like:
     ```bash
     #!/usr/bin/env bash
     apt-get update
     apt-get install -y python3 python3-pip
     pip3 install -r requirements.txt
     ```

---

## 4. Create the Runner Scripts

1. **run_test.py** (or `run_tests.py`)  
   - A Python script that will be executed to discover and run all tests. It typically:
     1. Imports `unittest` and `gradescope_utils`.
     2. Discovers all tests in the `test/` folder.
     3. Runs them and outputs the results to JSON so Gradescope can display them.  
   - Example:
     ```python
     import unittest
     import json
     import os
     from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

     if __name__ == '__main__':
         # Discover all tests in the 'test' folder
         tests = unittest.defaultTestLoader.discover('test', pattern='test*.py')
         # Run tests and save results
         results_file = os.path.join('/autograder/results/results.json')
         with open(results_file, 'w') as f:
             JSONTestRunner(stream=f, verbosity=2).run(tests)
     ```

2. **run_autograder**  
   - A shell script (no file extension) that Gradescope executes when grading.  
   - It typically:
     1. Copies student submission files into the working directory.
     2. Invokes `run_test.py`.  
   - Example:
     ```bash
     #!/usr/bin/env bash

     # Copy all submitted files from /autograder/submission to /autograder/source
     cp -r /autograder/submission/* /autograder/source

     # Move into the source directory
     cd /autograder/source

     # Run the tests
     python3 run_test.py
     ```

Make sure `run_autograder` is executable (e.g., `chmod +x run_autograder`).

---

## 5. Zip Everything into `autograder.zip`

1. **Include the necessary files**  
   - The zip should contain:
     - `setup.sh`  
     - `requirements.txt`  
     - `run_autograder`  
     - `run_test.py`  
     - The entire `test/` directory  
     - (Optionally) your `README.md` if you want documentation included.  
   - **Do not** include your `solutions/` folder or any large/unnecessary files in this zip. 

2. **Create the ZIP**  
   - From within your assignment folder, you can run (for example):  
     ```bash
     zip -r autograder.zip setup.sh requirements.txt run_autograder run_test.py test/ README.md
     ```

---

## 6. Upload the Autograder to Gradescope

1. **Create or open your course** on Gradescope.
2. **Create a new assignment** (choose “Programming Assignment”).
3. **Name the assignment** (e.g., `Assignment 1`) and set the total number of points (e.g., 80) to match the sum of your test weights in the test files.
4. **Configure the autograder** by clicking “**Upload Autograder.zip**”.  
   - Select the `autograder.zip` you just created.
   - Wait for Gradescope to build the Docker image and install dependencies. Check the logs to ensure no errors occur.

---

## 7. Test and Verify Your Autograder

1. **Click “Test autograder”** (appears after a successful build on Gradescope).
2. **Upload your solution** files (one or more `.py` files) that implement the correct logic.
3. **Wait for Gradescope to run** the tests.  
   - You should see a result page with each test’s name, point value, and pass/fail status.
4. **(Optional) Upload a buggy solution** to confirm that failing tests are caught by the autograder.

---

## 8. Distribute the Assignment to Students

- **Share the `student/` folder** (containing `q1.py`, `q2.py`, `q3.py`, etc.) via:
  1. **Moodle or Blackboard**: Zip the `student/` folder and attach instructions for students to complete the code and upload it to Gradescope.
  2. **GitHub Classroom**: Create a template repository with the `student/` folder. Each student will have their own repo to clone, edit, and submit.

Once students submit their solutions to Gradescope, the autograder will automatically run the tests, assign scores, and display the results.

---

# Summary of Key Files

1. **`setup.sh`**  
   Installs system-level and Python dependencies.
2. **`requirements.txt`**  
   Lists Python packages (including `gradescope-utils`).
3. **`test/`**  
   Contains all the unit test files using `unittest`.
4. **`run_test.py`**  
   Discovers and runs the tests, saving results in the Gradescope-compatible JSON format.
5. **`run_autograder`**  
   Entry point for Gradescope—copies submissions and executes `run_test.py`.
6. **`student/`**  
   Template scripts/questions that students will complete.
7. **`solutions/`**  
   Reference solution scripts for your own verification (not included in `autograder.zip`).
8. **`autograder.zip`**  
   Zipped package containing everything Gradescope needs to run the autograder.

---

## That’s It!

Following these steps will let you build, package, and deploy a Python-based autograder on Gradescope. Good luck with your assignments!