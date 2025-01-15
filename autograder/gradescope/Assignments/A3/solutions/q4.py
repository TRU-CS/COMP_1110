def generate_squares():
    """
    Generates a list of squares of numbers from 1 to 30 (inclusive).

    Returns:
    list: A list containing the squares of numbers from 1 to 30.
    """
    return [x**2 for x in range(1, 31)]

if __name__ == "__main__":
    # Example Usage
    squares = generate_squares()
    print(squares)
