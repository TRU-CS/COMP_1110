import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from unittest.mock import patch
from io import StringIO
import sys
from unittest.mock import patch


# Import functions from the student's script
from lab1 import (
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
        output = self.held_output.getvalue()

        # Step 1: Normalize and match bare content
        expected_output = """
        Twinkle, twinkle, little star,
            How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
        Twinkle, twinkle, little star,
            How I wonder what you are
        """
        normalized_output = " ".join(output.split())
        normalized_expected = " ".join(expected_output.split())

        # Assert bare content matches
        self.assertEqual(
            normalized_output,
            normalized_expected,
            "Bare content does not match the expected output."
        )

        # Step 2: Check leading whitespace differences if bare content matches
        output_lines = output.strip().split("\n")
        expected_lines = expected_output.strip().split("\n")

        # Count leading spaces in each line
        output_whitespace_counts = [len(line) - len(line.lstrip()) for line in output_lines]
        expected_whitespace_counts = [len(line) - len(line.lstrip()) for line in expected_lines]

        # Calculate differences in leading spaces
        output_whitespace_differences = [
            output_whitespace_counts[i + 1] - output_whitespace_counts[i]
            for i in range(len(output_whitespace_counts) - 1)
        ]
        expected_whitespace_differences = [
            expected_whitespace_counts[i + 1] - expected_whitespace_counts[i]
            for i in range(len(expected_whitespace_counts) - 1)
        ]

        # Assert that spacing differences match
        self.assertEqual(
            output_whitespace_differences,
            expected_whitespace_differences,
            f"Whitespace differences {output_whitespace_differences} do not match expected differences {expected_whitespace_differences}."
        )


    @weight(5)
    @number("1.2")
    def test_display_statement(self):
        """Test Case 1.2: Display Statement Across Two Lines"""
        ## strip whitespaces
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
            output = mock_stdout.getvalue().strip().splitlines()

        ## Add strip here

        # Step 1: Match raw content ignoring spaces and newlines

        ## remove any empty new lines
        expected_output = [
            "    A",
            "   A A",
            "  A A A",
            " A A A A",
            "A A A A A",
        ]

        # Normalize content by removing extra spaces and comparing line by line
        normalized_output = [" ".join(line.split()) for line in output]
        normalized_expected = [" ".join(line.split()) for line in expected_output]

        # Assert that normalized lines match
        self.assertEqual(
            normalized_output,
            normalized_expected,
            "Normalized content does not match the expected content."
        )

        # Step 2: Verify that the difference in leading spaces decrements by 1 as we go down
        output_whitespace_counts = [len(line) - len(line.lstrip()) for line in output]  # Count leading spaces in each line
        whitespace_differences = [
            output_whitespace_counts[i] - output_whitespace_counts[i + 1]
            for i in range(len(output_whitespace_counts) - 1)
        ]

        # Expected difference pattern: 1 for every step
        expected_differences = [1] * (len(output_whitespace_counts) - 1)

        # Assert that the differences in leading spaces match the expected pattern
        self.assertEqual(
            whitespace_differences,
            expected_differences,
            f"Whitespace differences {whitespace_differences} do not match expected differences {expected_differences}."
        )


    @weight(5)
    @number("1.5")
    def test_box_border_pattern(self):
        """Test Case 1.5: Box Border Pattern"""
        box_border_pattern()
        output = self.held_output.getvalue().strip()

        # Expected raw output
        ## match content as well
        expected_output = (
            "O O O O O\n"
            "O       O\n"
            "O       O\n"
            "O       O\n"
            "O O O O O"
        ).strip()

        # Split into lines for line-by-line comparison
        output_lines = [line.strip() for line in output.splitlines()]
        expected_lines = [line.strip() for line in expected_output.splitlines()]

        ## TODO: 
        ### assert len(output_lines)==len(expected_lines)
        self.assertEqual(len(output_lines),len(expected_line))

        # Compare line by line
        for i, (captured_line, expected_line) in enumerate(zip(output_lines, expected_lines), start=1):
            self.assertEqual(
                captured_line,
                expected_line,
                f"Mismatch on line {i}: Captured: '{captured_line}', Expected: '{expected_line}'"
            )



    @weight(5)
    @number("1.6")
    def test_stair_step_pattern(self):
        """Test Case 1.6: Stair-Step Pattern"""
        stair_step_pattern()
        output = self.held_output.getvalue().strip()

        # Expected output
        expected_output = (
            "*\n"
            "* *\n"
            "* * *\n"
            "* * * *\n"
            "* * * * *"
        )

        # Split and strip lines for line-by-line comparison
        output_lines = [line.strip() for line in output.splitlines()]
        expected_lines = [line.strip() for line in expected_output.splitlines()]

        self.assertEqual(len(output_lines),len(expected_line))


        # Compare line by line
        for i, (captured_line, expected_line) in enumerate(zip(output_lines, expected_lines), start=1):
            self.assertEqual(
                captured_line,
                expected_line,
                f"Mismatch on line {i}: Captured: '{captured_line}', Expected: '{expected_line}'"
            )


    @weight(5)
    @number("1.7")
    def test_alphabetic_pyramid(self):
        """Test Case 1.7: Alphabetic Pyramid"""
        alphabetic_pyramid()
        output = self.held_output.getvalue().strip()

        # Expected output
        expected_output = (
            "A\n"
            "B C\n"
            "D E F\n"
            "G H I J\n"
            "K L M N O"
        )

        # Split and strip lines for line-by-line comparison
        output_lines = [line.strip() for line in output.splitlines()]
        expected_lines = [line.strip() for line in expected_output.splitlines()]

        self.assertEqual(len(output_lines),len(expected_line))


        # Compare line by line
        for i, (captured_line, expected_line) in enumerate(zip(output_lines, expected_lines), start=1):
            self.assertEqual(
                captured_line,
                expected_line,
                f"Mismatch on line {i}: Captured: '{captured_line}', Expected: '{expected_line}'"
            )


if __name__ == "__main__":
    unittest.main()
