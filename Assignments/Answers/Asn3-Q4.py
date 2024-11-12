def square_numbers():
    """
    This function creates a list of squares of numbers from 1 to 30 (inclusive) and prints it.
    """
    # Using list comprehension and the range function to generate the squares of numbers
    squares = [i**2 for i in range(1, 31)]
    
    # Printing the list of squares
    print(squares)

# Calling the function to display the result
square_numbers()
