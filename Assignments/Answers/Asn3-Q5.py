def calculate_average_with_lowest_dropped():
    """
    This function calculates the average of student test scores after dropping the lowest score.
    The user will input the test scores, and the program will display the average of the scores with the lowest score removed.
    """
    
    # Step 1: Get the student's test scores
    scores = []
    print("Enter the test scores one by one. Enter 0 to stop.")
    
    while True:
        score = float(input("Enter test score: "))
        if score == 0:
            break
        scores.append(score)
    
    # Step 2: Calculate the total of the scores
    total_score = sum(scores)
    
    # Step 3: Find the lowest score
    lowest_score = min(scores)
    
    # Step 4: Subtract the lowest score from the total (adjusted total)
    adjusted_total = total_score - lowest_score
    
    # Step 5: Divide the adjusted total by one less than the number of test scores
    average = adjusted_total / (len(scores) - 1)
    
    # Step 6: Display the average
    print(f"The average score with the lowest score dropped is: {average:.2f}")

# Calling the function
calculate_average_with_lowest_dropped()
