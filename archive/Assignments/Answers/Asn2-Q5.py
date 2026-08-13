def find_min_max():
    """
    Asks the user to enter numbers one by one.
    Stops taking input when the user enters 0.
    Prints the smallest and largest numbers entered (ignoring 0).
    """
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))
    
    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))
    
    if numbers:
        print("Smallest number entered:", min(numbers))
        print("Largest number entered:", max(numbers))
    else:
        print("No numbers were entered.")

# Call the function
find_min_max()
