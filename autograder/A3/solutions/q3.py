def remove_duplicates(numbers_list):
    """
    Removes duplicate numbers from the list while preserving the original order.

    Args:
    numbers_list (list): A list of numbers that may contain duplicates.

    Returns:
    list: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for num in numbers_list:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

if __name__ == "__main__":
    # Example Usage
    input_list = [1, 2, 2, 3, 4, 4, 5]
    output_list = remove_duplicates(input_list)
    print(f"List after removing duplicates: {output_list}")
