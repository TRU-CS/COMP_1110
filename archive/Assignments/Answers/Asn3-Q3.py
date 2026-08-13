def remove_duplicates(numbers):
    """
    This function takes a list of numbers and removes duplicates from it.
    It uses a loop and a set to keep only the unique numbers in the list.
    """
    # Create an empty set to track unique numbers
    unique_numbers = set()
    
    # Loop through the given list and add each number to the set
    for num in numbers:
        unique_numbers.add(num)
    
    # Convert the set back to a list and return
    return list(unique_numbers)

# Example usage
numbers = [10, 20, 20, 30, 40, 10, 50]
result = remove_duplicates(numbers)

print("List after removing duplicates:", result)
