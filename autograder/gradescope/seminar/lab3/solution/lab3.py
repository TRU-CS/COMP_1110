def categorize_age():
    """
    Categorizes a given age into minors, adults, or seniors.
    """
    age = int(input("Enter age: "))
    minors, adults, seniors = 0, 0, 0
    
    if age < 18:
        minors += 1
    elif 18 <= age <= 64:
        adults += 1
    else:
        seniors += 1
    
    print(f"Minors: {minors}, Adults: {adults}, Seniors: {seniors}")
    return minors, adults, seniors


def sum_of_squares():
    """
    Computes the sum of squares of the first 50 counting numbers.
    """
    k, total = 1, 0
    while k <= 50:
        total += k * k
        k += 1
    print(f"Sum of squares: {total}")
    return total


def sum_of_cubes():
    """
    Computes the sum of cubes of the first n counting numbers.
    """
    n = int(input("Enter a positive integer: "))
    k, total = 1, 0
    while k <= n:
        total += k ** 3
        k += 1
    print(f"Sum of cubes: {total}")
    return total


def print_even_numbers():
    """
    Prints all even numbers between two user-entered numbers.
    """
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print("Even numbers:", ", ".join(map(str, even_numbers)))
    return even_numbers


def sum_of_digits_while():
    """
    Computes the sum of the digits of a number using a while loop.
    """
    num = int(input("Enter a number: "))
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    print(f"Sum of digits (while loop): {total}")
    return total


def sum_of_digits_for():
    """
    Computes the sum of the digits of a number using a for loop.
    """
    num = input("Enter a number: ")
    total = sum(int(digit) for digit in num)
    print(f"Sum of digits (for loop): {total}")
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
