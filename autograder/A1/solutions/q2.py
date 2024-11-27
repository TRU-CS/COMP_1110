def check_three_digit():
    try:
        # Ask the user to enter a number
        number = int(input("Enter a number: "))
        
        # Check if the number is a three-digit number
        if 100 <= abs(number) <= 999:
            print(f"{number} is a three-digit number.")
        else:
            print(f"{number} is not a three-digit number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    # Call the function
    check_three_digit()
