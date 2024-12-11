def who_am_i():
    """Determines personality type based on user responses to three yes/no questions."""
    
    # Ask the user the three yes/no questions
    answer1 = input("Do you like being around a lot of people? (yes/no): ").strip().lower()
    answer2 = input("Do you enjoy trying new things? (yes/no): ").strip().lower()
    answer3 = input("Do you prefer to plan things out? (yes/no): ").strip().lower()
    
    # Determine personality based on responses
    if answer1 == "yes" and answer2 == "yes" and answer3 == "yes":
        print("You are adventurous and outgoing!")
    elif answer1 == "no" and answer2 == "no" and answer3 == "no":
        print("You are thoughtful and reserved.")
    else:
        print("You have a balanced personality.")