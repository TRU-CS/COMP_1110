import unittest
import os
import importlib
from gradescope_utils.autograder_utils.decorators import weight, number


class TestFileAndFunctionExistence(unittest.TestCase):
    @weight(5)
    @number("0.1")
    def test_ans1_q1_exists(self):
        """Test if ans1_q1.py exists."""
        self.assertTrue(os.path.isfile("questions/ans1_q1.py"), "ans1_q1.py is missing!")

    @weight(5)
    @number("0.2")
    def test_ans1_q2_exists(self):
        """Test if ans1_q2.py exists."""
        self.assertTrue(os.path.isfile("questions/ans1_q2.py"), "ans1_q2.py is missing!")

    @weight(5)
    @number("0.3")
    def test_ans1_q3_exists(self):
        """Test if ans1_q3.py exists."""
        self.assertTrue(os.path.isfile("questions/ans1_q3.py"), "ans1_q3.py is missing!")

    @weight(5)
    @number("0.4")
    def test_check_exam_eligibility_function(self):
        """Test if check_exam_eligibility function exists in ans1_q1.py."""
        try:
            module = importlib.import_module("questions.ans1_q1")
            self.assertTrue(
                hasattr(module, "check_exam_eligibility"),
                "Function check_exam_eligibility is missing or incorrectly named in ans1_q1.py!"
            )
        except ModuleNotFoundError:
            self.fail("ans1_q1.py module cannot be imported!")

    @weight(5)
    @number("0.5")
    def test_check_three_digit_function(self):
        """Test if check_three_digit function exists in ans1_q2.py."""
        try:
            module = importlib.import_module("questions.ans1_q2")
            self.assertTrue(
                hasattr(module, "check_three_digit"),
                "Function check_three_digit is missing or incorrectly named in ans1_q2.py!"
            )
        except ModuleNotFoundError:
            self.fail("ans1_q2.py module cannot be imported!")

    @weight(5)
    @number("0.6")
    def test_python_quiz_application_function(self):
        """Test if python_quiz_application function exists in ans1_q3.py."""
        try:
            module = importlib.import_module("questions.ans1_q3")
            self.assertTrue(
                hasattr(module, "python_quiz_application"),
                "Function python_quiz_application is missing or incorrectly named in ans1_q3.py!"
            )
        except ModuleNotFoundError:
            self.fail("ans1_q3.py module cannot be imported!")
