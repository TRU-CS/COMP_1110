import io
import sys
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):
    @points(1)
    @name("Check valid three-digit number")
    def test_1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Feedback.call_user(self.st.check_three_digit, 123)
        sys.stdout = sys.__stdout__
        user_val = captured_output.getvalue().strip()
        correct_val = "123 is a three-digit number."
        Feedback.check_scalar("Output for check_three_digit(123)", correct_val, user_val)

    @points(1)
    @name("Check valid non-three-digit number")
    def test_2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Feedback.call_user(self.st.check_three_digit, 45)
        sys.stdout = sys.__stdout__
        user_val = captured_output.getvalue().strip()
        correct_val = "45 is not a three-digit number."
        Feedback.check_scalar("Output for check_three_digit(45)", correct_val, user_val)

    @points(1)
    @name("Check negative three-digit number")
    def test_3(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Feedback.call_user(self.st.check_three_digit, -999)
        sys.stdout = sys.__stdout__
        user_val = captured_output.getvalue().strip()
        correct_val = "-999 is a three-digit number."
        Feedback.check_scalar("Output for check_three_digit(-999)", correct_val, user_val)

    @points(1)
    @name("Check invalid input")
    def test_4(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Feedback.call_user(self.st.check_three_digit, "abc")
        sys.stdout = sys.__stdout__
        user_val = captured_output.getvalue().strip()
        correct_val = "Invalid input. Please enter a valid integer."
        Feedback.check_scalar("Output for check_three_digit(\"abc\")", correct_val, user_val)
