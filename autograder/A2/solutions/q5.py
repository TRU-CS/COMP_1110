def find_min_max():
    """
    Asks the user to enter numbers one by one.
    Stops taking input when the user enters 0.
    Prints the smallest and largest numbers entered (ignoring 0).
    """
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))

    min_num=None
    max_num=None
    
    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))
    
    if numbers:
        min_num= min(numbers)
        max_num= max(numbers)
        print("Smallest number entered:", min_num)
        print("Largest number entered:", max_num)
    else:
        print("No numbers were entered.")

    return min_num, max_num