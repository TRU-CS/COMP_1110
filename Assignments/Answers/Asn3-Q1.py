def find_missing_number(nums):
    """
    Finds and returns the missing number in a list of integers from 0 to n.

    Parameters:
    nums (list): A list containing integers from 0 to n with one missing number.

    Returns:
    int: The missing number.
    """
    n = len(nums)  # Since one number is missing, n represents the length of the list
    expected_sum = n * (n + 1) // 2  # Sum of all numbers from 0 to n
    actual_sum = sum(nums)  # Sum of numbers in the input list

    # The difference between the expected sum and the actual sum is the missing number
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage
numbers = [0, 1, 2, 4, 5]  # Example input list with 3 missing
print("Missing number:", find_missing_number(numbers))
