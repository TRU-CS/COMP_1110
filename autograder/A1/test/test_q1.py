# test_exam_ligibility.py
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from questions.q1 import check_exam_eligibility

class TestExamEligibility(unittest.TestCase):
    
    @weight(5)
    @number("1.1")
    def test_full_attendance(self):
        """Test Case 1: Student attended all classes, 100% attendance."""
        with unittest.mock.patch('builtins.input', side_effect=['100', '100']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 100.00%")
                mocked_print.assert_any_call("The student is permitted to take the exam.")
    
    @weight(5)
    @number("1.2")
    def test_exactly_90_percent_attendance(self):
        """Test Case 2: Student has exactly 90% attendance, meets eligibility."""
        with unittest.mock.patch('builtins.input', side_effect=['100', '90']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 90.00%")
                mocked_print.assert_any_call("The student is permitted to take the exam.")
                
    @weight(5)
    @number("1.3")
    def test_below_90_percent_attendance(self):
        """Test Case 3: Student attended below 90%, not eligible for exam."""
        with unittest.mock.patch('builtins.input', side_effect=['100', '80']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 80.00%")
                mocked_print.assert_any_call("The student is not permitted to take the exam.")

    @weight(5)
    @number("1.4")
    def test_zero_classes_held(self):
        """Test Case 4: Zero classes held to handle division by zero gracefully."""
        with unittest.mock.patch('builtins.input', side_effect=['0', '0']):
            with self.assertRaises(ZeroDivisionError):
                check_exam_eligibility()

    @weight(5)
    @number("1.5")
    def test_high_attendance_with_low_classes(self):
        """Test Case 5: Attended more than held (edge case)."""
        with unittest.mock.patch('builtins.input', side_effect=['10', '15']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                # Expect an over-100% result
                mocked_print.assert_any_call("Percentage of classes attended: 150.00%")
                mocked_print.assert_any_call("The student is permitted to take the exam.")


    @weight(5)
    @number("2.1")
    def test_90_percent_attendance_case(self):
        """Test Case 6: Exactly 90% attendance, eligible for the exam."""
        with unittest.mock.patch('builtins.input', side_effect=['100', '90']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 90.00%")
                mocked_print.assert_any_call("The student is permitted to take the exam.")

    @weight(5)
    @number("2.2")
    def test_80_percent_attendance_case(self):
        """Test Case 7: 80% attendance, not eligible for the exam."""
        with unittest.mock.patch('builtins.input', side_effect=['50', '40']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 80.00%")
                mocked_print.assert_any_call("The student is not permitted to take the exam.")

    @weight(5)
    @number("2.3")
    def test_95_percent_attendance_case(self):
        """Test Case 8: 95% attendance, eligible for the exam."""
        with unittest.mock.patch('builtins.input', side_effect=['200', '190']):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                mocked_print.assert_any_call("Percentage of classes attended: 95.00%")
                mocked_print.assert_any_call("The student is permitted to take the exam.")
