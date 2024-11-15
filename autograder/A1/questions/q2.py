def check_three_digit():
    # Ask the user to enter a number
    number = int(input("Enter a number: "))
    
    # Check if the number is a three-digit number
    if 100 <= abs(number) <= 999:
        print("The number is a three-digit number.")
    else:
        print("The number is not a three-digit number.")


if __name__=='__main__':
# Call the function
    check_three_digit()