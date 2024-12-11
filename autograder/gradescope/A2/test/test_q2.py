import unittest
from unittest.mock import patch
from io import StringIO
from student.q2 import math_quiz

class TestMathQuiz(unittest.TestCase):

    @patch('random.randint', side_effect=[123, 456])  # Mock random numbers
    @patch('builtins.input', return_value="579")  # Mock correct user input
    def test_correct_answer(self, mock_input, mock_randint):
        """Test math_quiz with a correct answer."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            correct_answer, student_answer = math_quiz()
            console_output = mock_stdout.getvalue()

        # Validate printed output
        self.assertIn("Welcome to the Math Quiz!", console_output)
        self.assertIn("   123", console_output)
        self.assertIn("+  456", console_output)
        self.assertIn("Congratulations! Your answer is correct.", console_output)

        # Validate return values
        self.assertEqual(correct_answer, 579)
        self.assertEqual(student_answer, 579)

    @patch('random.randint', side_effect=[123, 456])  # Mock random numbers
    @patch('builtins.input', return_value="500")  # Mock incorrect user input
    def test_incorrect_answer(self, mock_input, mock_randint):
        """Test math_quiz with an incorrect answer."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            correct_answer, student_answer = math_quiz()
            console_output = mock_stdout.getvalue()

        # Validate printed output
        self.assertIn("Welcome to the Math Quiz!", console_output)
        self.assertIn("   123", console_output)
        self.assertIn("+  456", console_output)
        self.assertIn("Sorry, that's incorrect. The correct answer is 579.", console_output)

        # Validate return values
        self.assertEqual(correct_answer, 579)
        self.assertEqual(student_answer, 500)

if __name__ == "__main__":
    unittest.main()
