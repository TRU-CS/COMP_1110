# Python_Quiz_Application
# This is a basic Python Quiz application with three levels: Easy, Average, and Hard.
# The application will ask the user questions and display the final score at the end.

def python_quiz_application():
    # Asking for player's name
    player_name = input("Enter your name: ")
    print(f"Welcome to the Python Quiz, {player_name}!")

    # Choosing quiz level
    print("Choose a difficulty level:")
    print("1. Easy\n2. Average\n3. Hard")
    level_choice = input("Enter 1, 2, or 3 for the level you want to play: ")

    # Initializing result counter
    calculate_result = 0

    # Questions for each level
    questions_easy = [
        ("What is the capital of France?", "a", ["a) Paris", "b) London", "c) Rome", "d) Berlin"]),
        ("What color are bananas?", "b", ["a) Red", "b) Yellow", "c) Green", "d) Blue"]),
        ("2 + 2 = ?", "d", ["a) 3", "b) 5", "c) 1", "d) 4"]),
        ("Which planet is known as the Red Planet?", "a", ["a) Mars", "b) Venus", "c) Earth", "d) Jupiter"]),
        ("How many days are there in a week?", "c", ["a) 5", "b) 6", "c) 7", "d) 8"]),
    ]

    questions_average = [
        ("What is the capital of Canada?", "c", ["a) Vancouver", "b) Montreal", "c) Ottawa", "d) Toronto"]),
        ("Which is the largest ocean on Earth?", "b", ["a) Indian", "b) Pacific", "c) Atlantic", "d) Arctic"]),
        ("Which element has the atomic number 1?", "a", ["a) Hydrogen", "b) Oxygen", "c) Helium", "d) Carbon"]),
        ("How many continents are there?", "c", ["a) 5", "b) 6", "c) 7", "d) 8"]),
        ("Who wrote 'Hamlet'?", "a", ["a) Shakespeare", "b) Tolstoy", "c) Hemingway", "d) Dickens"]),
    ]

    questions_hard = [
        ("What is the square root of 144?", "d", ["a) 10", "b) 11", "c) 12", "d) 12"]),
        ("What is 10^3?", "a", ["a) 1000", "b) 100", "c) 10", "d) 10000"]),
        ("In which year did World War I begin?", "b", ["a) 1923", "b) 1914", "c) 1900", "d) 1939"]),
        ("What is the boiling point of water in Celsius?", "c", ["a) 0", "b) 50", "c) 100", "d) 212"]),
        ("What is the derivative of x^2?", "b", ["a) x", "b) 2x", "c) x^2", "d) x^3"]),
    ]

    # Select questions based on level
    if level_choice == '1':
        questions = questions_easy
    elif level_choice == '2':
        questions = questions_average
    elif level_choice == '3':
        questions = questions_hard
    else:
        print("Invalid choice. Exiting the quiz.")
        return

    # Display questions and collect answers
    for question, correct_answer, options in questions:
        print("\n" + question)
        for option in options:
            print(option)
        user_answer = input("Enter the letter of the correct answer: ").lower()

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct!")
            calculate_result += 1
        else:
            print(f"Invalid choice. The correct answer was: {correct_answer}")

    # Display final result
    print(f"Quiz completed! {player_name}, your final score is: {calculate_result}/{len(questions)}")

    return calculate_result

if __name__=='__main__':
    # Run the quiz application
    python_quiz_application()
