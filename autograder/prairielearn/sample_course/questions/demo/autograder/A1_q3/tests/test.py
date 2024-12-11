import numpy as np
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):

    @points(1)
    @name("Check easy level score")
    def test_easy_level(self):
        easy_answers = ['a', 'b', 'd', 'a', 'c']
        student_answers = {
            "level": "1",
            "answers": easy_answers
        }
        user_score = Feedback.call_user(self.st.python_quiz_application, student_answers)
        correct_score = 5
        Feedback.check_scalar("Score for easy level", correct_score, user_score)

    @points(2)
    @name("Check average level score")
    def test_average_level(self):
        average_answers = ['c', 'b', 'a', 'c', 'a']
        student_answers = {
            "level": "2",
            "answers": average_answers
        }
        user_score = Feedback.call_user(self.st.python_quiz_application, student_answers)
        correct_score = 5
        Feedback.check_scalar("Score for average level", correct_score, user_score)

    @points(3)
    @name("Check hard level score")
    def test_hard_level(self):
        hard_answers = ['c', 'a', 'b', 'c', 'b']
        student_answers = {
            "level": "3",
            "answers": hard_answers
        }
        user_score = Feedback.call_user(self.st.python_quiz_application, student_answers)
        correct_score = 5
        Feedback.check_scalar("Score for hard level", correct_score, user_score)

    @points(1)
    @name("Check invalid level")
    def test_invalid_level(self):
        invalid_answers = {
            "level": "4",  # Invalid level choice
            "answers": []
        }
        user_score = Feedback.call_user(self.st.python_quiz_application, invalid_answers)
        correct_score = 0  # Should not proceed with an invalid level
        Feedback.check_scalar("Score for invalid level", correct_score, user_score)

    @points(2)
    @name("Check partial correct answers")
    def test_partial_answers(self):
        partial_answers = {
            "level": "1",
            "answers": ['a', 'b', 'c', 'd', 'a']  # Some correct, some incorrect
        }
        user_score = Feedback.call_user(self.st.python_quiz_application, partial_answers)
        correct_score = 2  # Only two correct answers
        Feedback.check_scalar("Score for partial correct answers", correct_score, user_score)
