#1. Find the largest number
def max_of_three():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    max_value = max(a, b, c)  # Find the maximum value
    print(f"The maximum value is: {max_value}")  # Print the result
    return max_value
    
    
 
#2. checking palindrome
def isPalindrome():
    # Take integer input from the user
    num1 = int(input("Enter a number: "))
    
    # Implement your palindrome check logic here
    num_str = str(num1)  # Convert the number to string
    if num_str == num_str[::-1]:  # Check if the string is equal to its reverse
        result = True  # print if it's a palindrome
    else:
        result = False  # print if it's not a palindrome 
    print(result)
    return result
 
  

#3. Random number guessing game
import random

def guessing_game():
    number = random.randint(1, 100)  # Generate a random number
    game_active = True  # A flag to control the loop

    while game_active:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed it!")
            number = random.randint(1, 100)  # Generate a new number
            game_active = False  # Set the flag to False to stop the game



    

#4. Square root of a number
import math

def calculate_square_root():
    """Takes a number from the user and returns its square root."""
    num = float(input("Enter a number: "))
    
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    
    num_sqrt =  math.sqrt(num)
    print(f"The square root of {num} is: {num_sqrt}")
    return num_sqrt

  
#5. Create a matrix
def create_matrix():
    """Creates and returns a 2D list (matrix) based on user input."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for position ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)
    print("\nThe matrix you entered is:")
    for row in matrix:
        print(row)
    return matrix
  

if __name__ == "__main__":
    max_of_three()
    isPalindrome()
    guessing_game()
    calculate_square_root()
    create_matrix()