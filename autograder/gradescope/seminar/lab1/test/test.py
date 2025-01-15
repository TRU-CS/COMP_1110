import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from unittest.mock import patch
from io import StringIO
import sys
from unittest.mock import patch


# Import functions from the student's script
from solution.lab1 import (
    twinkle_twinkle,
    display_statement,
    display_two_methods,
    pyramid_pattern,
    box_border_pattern,
    stair_step_pattern,
    alphabetic_pyramid,
)

class TestPatterns(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout  # Save original stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Reset stdout after the test."""
        sys.stdout = self.original_stdout  # Restore original stdout
        self.held_output.close()

    @weight(5)
    @number("1.1")
    def test_twinkle_twinkle(self):
        """Test Case 1.1: Twinkle Twinkle in Specific Format"""
        twinkle_twinkle()
        output = self.held_output.getvalue().strip()
        expected_output = """Twinkle, twinkle, little star, 
    How I wonder what you are!  
        Up above the world so high,      
        Like a diamond in the sky.  
Twinkle, twinkle, little star,  
    How I wonder what you are"""
        self.assertEqual(output, expected_output)

    @weight(5)
    @number("1.2")
    def test_display_statement(self):
        """Test Case 1.2: Display Statement Across Two Lines"""
        display_statement()
        output = self.held_output.getvalue().strip()
        expected_output = "I am using Python\nIt’s my First Assignment"
        self.assertEqual(output, expected_output)

    @weight(5)
    @number("1.3")
    def test_display_two_methods(self):
        """Test Case 1.3: Statement with Two Methods"""
        display_two_methods()
        output = self.held_output.getvalue().strip()
        expected_output = (
            "ohhh!!!\nPython is so fun!!! && It is Easy! Get Started\n"
            "ohhh!!!\nPython is so fun!!! && It is Easy! Get Started"
        )
        self.assertEqual(output, expected_output)


    @weight(5)
    @number("1.4")
    def test_pyramid_pattern(self):
        """Test Case 1.4: Pyramid Pattern"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pyramid_pattern()
            output = mock_stdout.getvalue().splitlines()

        expected_output = [
            "    A",
            "   A A",
            "  A A A",
            " A A A A",
            "A A A A A",
        ]
        
        # Compare line by line
        for i, (captured_line, expected_line) in enumerate(zip(output, expected_output), start=1):
            self.assertEqual(captured_line, expected_line)




    @weight(5)
    @number("1.5")
    def test_box_border_pattern(self):
        """Test Case 1.5: Box Border Pattern"""
        box_border_pattern()
        output = self.held_output.getvalue().strip()

        # Expected raw output without normalization
        expected_output = (
            "O O O O O\n"
            "O       O\n"
            "O       O\n"
            "O       O\n"
            "O O O O O"
        )
        self.assertEqual(output, expected_output)




    @weight(5)
    @number("1.6")
    def test_stair_step_pattern(self):
        """Test Case 1.6: Stair-Step Pattern"""
        stair_step_pattern()
        output = self.held_output.getvalue().strip()

        # Normalize whitespace in both output and expected
        normalized_output = "\n".join(" ".join(line.split()) for line in output.splitlines())
        expected_output = (
            "*\n"
            "* *\n"
            "* * *\n"
            "* * * *\n"
            "* * * * *"
        )
        normalized_expected = "\n".join(" ".join(line.split()) for line in expected_output.splitlines())

        # # Debugging: Print captured and normalized outputs
        # print("Captured Output (Normalized):")
        # print(repr(normalized_output))
        # print("Expected Output (Normalized):")
        # print(repr(normalized_expected))

        # Compare normalized outputs
        self.assertEqual(normalized_output, normalized_expected)

    @weight(5)
    @number("1.7")
    def test_alphabetic_pyramid(self):
        """Test Case 1.7: Alphabetic Pyramid"""
        alphabetic_pyramid()
        output = self.held_output.getvalue().strip()
        normalized_output = "\n".join(" ".join(line.split()) for line in output.splitlines())

        expected_output = (
            "A\n"
            "B C\n"
            "D E F\n"
            "G H I J\n"
            "K L M N O"
        )
        self.assertEqual(normalized_output, expected_output)

if __name__ == "__main__":
    unittest.main()
