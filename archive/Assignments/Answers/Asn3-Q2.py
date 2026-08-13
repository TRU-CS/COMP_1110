def split_list(lst, n):
    """
    Splits the list into two parts based on the input length n.
    """
    # Slice the list into two parts
    first_part = lst[:n]
    second_part = lst[n:]

    return first_part, second_part

# Example usage
my_list = [10, 20, 30, 40, 50, 60]
n = int(input("Enter the length of the first part: "))
first, second = split_list(my_list, n)

print("First part:", first)
print("Second part:", second)
