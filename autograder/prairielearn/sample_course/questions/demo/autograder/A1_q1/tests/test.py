import numpy as np
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):
    @points(1)
    @name("Check total_classes <= 0")
    def test_1(self):
        user_val = Feedback.call_user(self.st.check_exam_eligibility, 0, 10)
        correct_val = None  # Function should return None in this case
        Feedback.check_scalar("Return value for check_exam_eligibility(0, 10)", correct_val, user_val)

    @points(2)
    @name("Check attendance percentage >= 90%")
    def test_2(self):
        user_val = Feedback.call_user(self.st.check_exam_eligibility, 50, 45)
        correct_val = 90.00  # Function should return the percentage
        Feedback.check_scalar("Return value for check_exam_eligibility(50, 45)", correct_val, user_val)

    @points(2)
    @name("Check attendance percentage < 90%")
    def test_3(self):
        user_val = Feedback.call_user(self.st.check_exam_eligibility, 50, 40)
        correct_val = 80.00  # Function should return the percentage
        Feedback.check_scalar("Return value for check_exam_eligibility(50, 40)", correct_val, user_val)

    @points(3)
    @name("Check random valid inputs")
    def test_4(self):
        test_cases = [
            (100, 100, 100.00),
            (80, 70, 87.50),
            (60, 54, 90.00)
        ]
        for total_classes, classes_attended, correct_val in test_cases:
            user_val = Feedback.call_user(self.st.check_exam_eligibility, total_classes, classes_attended)
            Feedback.check_scalar(f"Return value for check_exam_eligibility({total_classes}, {classes_attended})", correct_val, user_val)
