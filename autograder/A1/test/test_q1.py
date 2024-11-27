# test_exam_eligibility.py
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from unittest.mock import patch
from q1 import check_exam_eligibility

import unittest
from unittest.mock import patch

class TestExamEligibility(unittest.TestCase):
    
    @weight(5)
    @number("1.1")
    def test_full_attendance(self):
        """Test Case 1: Student attended all classes, 100% attendance."""
        with patch('builtins.input', side_effect=['100', '100']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('100' in call[0][0] for call in mocked_print.call_args_list))
                self.assertTrue(any('are permitted' in call[0][0] for call in mocked_print.call_args_list))
    
    @weight(5)
    @number("1.2")
    def test_exactly_90_percent_attendance(self):
        """Test Case 2: Student has exactly 90% attendance, meets eligibility."""
        with patch('builtins.input', side_effect=['100', '90']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('90.00' in call[0][0] for call in mocked_print.call_args_list))
                self.assertTrue(any('are permitted' in call[0][0] for call in mocked_print.call_args_list))
                
    @weight(5)
    @number("1.3")
    def test_below_90_percent_attendance(self):
        """Test Case 3: Student attended below 90%, not eligible for exam."""
        with patch('builtins.input', side_effect=['100', '80']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('80.00' in call[0][0] for call in mocked_print.call_args_list))
                self.assertTrue(any('not permitted' in call[0][0] for call in mocked_print.call_args_list))

    @weight(5)
    @number("1.4")
    def test_zero_classes_held(self):
        """Test Case 4: Zero classes held to handle validation gracefully."""
        with patch('builtins.input', side_effect=['0', '0']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('The number of total classes must be greater than 0.' in call[0][0] for call in mocked_print.call_args_list))

    @weight(5)
    @number("1.5")
    def test_high_attendance_with_low_classes(self):
        """Test Case 5: Attended more than held (edge case)."""
        with patch('builtins.input', side_effect=['10', '15']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('150.00' in call[0][0] for call in mocked_print.call_args_list))
                self.assertTrue(any('are permitted' in call[0][0] for call in mocked_print.call_args_list))

    @weight(5)
    @number("1.6")
    def test_midrange_attendance_case(self):
        """Test Case 6: 95% attendance, eligible for the exam."""
        with patch('builtins.input', side_effect=['200', '190']):
            with patch('builtins.print') as mocked_print:
                check_exam_eligibility()
                self.assertTrue(any('95.00' in call[0][0] for call in mocked_print.call_args_list))
                self.assertTrue(any('are permitted' in call[0][0] for call in mocked_print.call_args_list))

