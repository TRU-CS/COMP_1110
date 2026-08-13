import random

def generate_question():
    """Generates two random numbers for the addition quiz and returns them."""
    num1 = random.randint(100, 999)  # Generate a three-digit number
    num2 = random.randint(100, 999)  # Generate another three-digit number
    return num1, num2

def ask_question(num1, num2):
    """
    Displays the question to the user, takes the user's answer,
    and checks if it is correct or incorrect.
    """
    print(f"   {num1}")
    print(f"+  {num2}")
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Get the student's answer
    student_answer = int(input("Enter your answer: "))
    
    # Check if the answer is correct or incorrect
    if student_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

def math_quiz():
    """Runs the math quiz."""
    print("Welcome to the Math Quiz!")
    num1, num2 = generate_question()  # Generate a random addition question
    ask_question(num1, num2)          # Display question and evaluate response

# Start the quiz
math_quiz()