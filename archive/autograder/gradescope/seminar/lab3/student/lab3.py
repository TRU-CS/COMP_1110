def categorize_age():
    """
    Categorizes a given age into minors, adults, or seniors.
    """
    # TODO: Get age input from the user
    age = ...
    minors, adults, seniors = 0, 0, 0
    
    # TODO: Use if/elif/else to categorize age
    ...
    
    # TODO: Return the counts of minors, adults, and seniors
    return minors, adults, seniors


def sum_of_squares():
    """
    Computes the sum of squares of the first k=50 counting numbers.
    """
    k, total = 1, 0
    
    # TODO: Use a while loop to calculate the sum of squares
    ...
    
    return total


def sum_of_cubes():
    """
    Computes the sum of cubes of the first n counting numbers.
    """
    # TODO: Get user input for n
    n = ...
    k, total = 1, 0
    
    # TODO: Use a while loop to calculate the sum of cubes
    ...
    
    return total


def print_even_numbers():
    """
    Prints all even numbers between two user-entered numbers.
    """
    # TODO: Get start and end values from the user
    start = ...
    end = ...
    
    # TODO: Use a for loop to find even numbers in the range and store them in a list
    even_numbers = []
    ...
    
    return even_numbers


def sum_of_digits_while():
    """
    Computes the sum of the digits of a number using a while loop.
    """
    # TODO: Get number input from the user
    num = ...
    total = 0
    
    # TODO: Use a while loop to calculate sum of digits
    ...
    
    return total


def sum_of_digits_for():
    """
    Computes the sum of the digits of a number using a for loop.
    """
    # TODO: Get number input from the user
    num = ...
    
    # TODO: Use a for loop to calculate sum of digits
    total = ...
    
    return total


if __name__ == "__main__":
    print("1. Categorize Age Groups")
    categorize_age()
    
    print("\n2. Sum of Squares")
    sum_of_squares()
    
    print("\n3. Sum of Cubes")
    sum_of_cubes()
    
    print("\n4. Print Even Numbers in a Range")
    print_even_numbers()
    
    print("\n5. Sum of Digits (While Loop)")
    sum_of_digits_while()
    
    print("\n6. Sum of Digits (For Loop)")
    sum_of_digits_for()
