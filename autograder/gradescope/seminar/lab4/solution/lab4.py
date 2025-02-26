def max_of_three():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    max_value = max(a, b, c)  # Find the maximum value
    print(f"The maximum value is: {max_value}")  # Print the result
    return max_value

if __name__ == "__main__":
    max_of_three()