def fizz_buzz():
    """Prints numbers from 1 to 20 with substitutions for multiples of 3 and 5."""
    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function
fizz_buzz()
