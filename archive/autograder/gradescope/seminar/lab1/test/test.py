from gradescope_utils.autograder_utils.decorators import number, weight

from lab1 import (
    alphabetic_pyramid,
    box_border_pattern,
    display_statement,
    display_two_methods,
    pyramid_pattern,
    stair_step_pattern,
    twinkle_twinkle,
)


def _trim_common_indent(lines, anchor_text):
    leading_spaces = None
    for line in lines:
        if line.strip() == anchor_text:
            leading_spaces = len(line) - len(line.lstrip())
            break

    if leading_spaces is None:
        return lines

    return [line[leading_spaces:] if len(line) >= leading_spaces else line for line in lines]


@weight(5)
@number("1.1")
def test_twinkle_twinkle(capsys):
    twinkle_twinkle()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "Twinkle, twinkle, little star,",
        "    How I wonder what you are!",
        "        Up above the world so high,",
        "        Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "    How I wonder what you are",
    ]

    output_lines = _trim_common_indent(output_lines, "Twinkle, twinkle, little star,")
    output_lines = [line.replace("\t", "    ") for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line.rstrip() == expected


@weight(5)
@number("1.2")
def test_display_statement(capsys):
    display_statement()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "I am using Python",
        "It's my First Assignment",
    ]

    output_lines = [line.replace("’", "'") for line in output_lines]
    output_lines = [line.strip() for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line == expected


@weight(5)
@number("1.3")
def test_display_two_methods(capsys):
    display_two_methods()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "ohhh!!!",
        "Python is so fun!!! && It is Easy! Get Started",
    ]

    output_lines = [line.strip() for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line == expected


@weight(5)
@number("1.4")
def test_pyramid_pattern(capsys):
    pyramid_pattern()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "    A",
        "   A A",
        "  A A A",
        " A A A A",
        "A A A A A",
    ]

    output_lines = _trim_common_indent(output_lines, "A A A A A")

    for line, expected in zip(output_lines, expected_output):
        assert line.rstrip() == expected


@weight(5)
@number("1.5")
def test_box_border_pattern(capsys):
    box_border_pattern()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "O O O O O",
        "O       O",
        "O       O",
        "O       O",
        "O O O O O",
    ]

    output_lines = _trim_common_indent(output_lines, "O O O O O")
    output_lines = [line.replace("\t", "       ") for line in output_lines]
    output_lines = [line.replace("o", "O") for line in output_lines]
    output_lines = [line.replace("0", "O") for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line.rstrip() == expected


@weight(5)
@number("1.6")
def test_stair_step_pattern(capsys):
    stair_step_pattern()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "*",
        "* *",
        "* * *",
        "* * * *",
        "* * * * *",
    ]

    output_lines = [line.strip() for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line == expected


@weight(5)
@number("1.7")
def test_alphabetic_pyramid(capsys):
    alphabetic_pyramid()
    output_lines = capsys.readouterr().out.split("\n")

    expected_output = [
        "A",
        "B C",
        "D E F",
        "G H I J",
        "K L M N O",
    ]

    output_lines = [line.strip() for line in output_lines]

    for line, expected in zip(output_lines, expected_output):
        assert line == expected
