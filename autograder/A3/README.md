# Gradescope Autograder

This repository contains all the necessary files to create and test a Gradescope autograder. Follow the instructions below to set up, test, and deploy the autograder for evaluating student submissions.

---

## Repository Structure

Here’s a brief overview of the files and their purpose:

- **`setup.sh`**: A shell script to configure the environment (e.g., installing dependencies) for the autograder.
- **`requirements.txt`**: Lists Python packages required by the autograder, which will be installed during setup.
- **`test`**: A folder containing all test cases written using the `unittest` framework. These test cases are organized to evaluate submissions for correctness, efficiency, and edge-case handling.
- **`run_tests.py`**: A script to locally test the autograder. Use this to verify the behavior of your test cases before uploading to Gradescope.
- **`run_autograder`**: The main entry point for the autograder on Gradescope. Gradescope executes this script to grade student submissions.
- **`README.md`**: This file. Provides documentation for setting up and using the autograder.
- **`autograder.zip`**: A ready-to-upload archive containing all the required files for deploying the autograder on Gradescope (excluding the `solutions` folder).
- **`solutions`**: A folder containing the solutions
- **`student`**: A folder containing the template scripts and assignment instructions in `README.md`
---

## Setting Up the Autograder

To create and upload the autograder to Gradescope:

1. Ensure all the required files are in place (as listed above).
2. Create a ZIP file of all the necessary files for Gradescope. The ZIP file should **include all files and folders except the `solutions` & `student` folders**.
   - The provided `autograder.zip` already contains the correct configuration.
3. Upload the `autograder.zip` file to Gradescope under the "Autograder" section of the assignment setup.

---

## Testing the Autograder 

1. Upload the python scripts in the `solutions` folder to the assignment on Gradescope
2. It should pass all the tests

## Assignment distribution
1. Upload everything in the `student` folder to Moodle and students will download and work on the file locally.
2. Alternatively, use Github classroom to streamline the assignment distribution process so each student will can their own github repo that contains the assignment tempalte