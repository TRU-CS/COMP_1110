def split_list(input_list, split_length):
    """
    Splits the input list into two parts based on the split_length.

    Args:
    input_list (list): The list to be split.
    split_length (int): The length of the first part of the list.

    Returns:
    tuple: A tuple containing two lists, or a string message for invalid input.
    """
    if split_length < 0:
        return "Invalid input. The split length cannot be negative."
    if split_length > len(input_list):
        return "Invalid input. The split length exceeds the length of the list."

    first_part = input_list[:split_length]
    second_part = input_list[split_length:]
    return first_part, second_part

if __name__ == "__main__":
    # Example Usage
    input_list = [1, 2, 3, 4, 5]
    split_length = int(input("Enter the split length: "))
    result = split_list(input_list, split_length)

    if isinstance(result, str):
        print(result)
    else:
        print(f"First part: {result[0]}")
        print(f"Second part: {result[1]}")
