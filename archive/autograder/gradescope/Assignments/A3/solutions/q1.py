def find_missing_number(numbers_list):
    """
    Finds the missing number in a list of numbers from 0 to n.
    If no number is missing, it prints a specific message.
    
    Args:
    numbers_list (list): List of integers from 0 to n with one number missing.
    
    Returns:
    int or None: Missing number if found, otherwise None.
    """
    n = len(numbers_list)  # Expected range is 0 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers_list)

    if expected_sum == actual_sum:
        print("No missing numbers in the list.")
        return None

    missing_number = expected_sum - actual_sum
    print(f"The missing number is: {missing_number}")
    return missing_number

if __name__ == "__main__":
    # Example Usage
    test_list = [0, 1, 2, 4, 5]
    find_missing_number(test_list)
