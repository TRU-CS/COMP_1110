def calculate_adjusted_average(scores):
    """
    Calculates the average of test scores after dropping the lowest score.

    Args:
    scores (list): A list of integers representing test scores.

    Returns:
    float: The adjusted average score, rounded to 2 decimal places.
    """


    total = sum(scores)
    lowest_score = min(scores)
    adjusted_total = total - lowest_score
    adjusted_average = adjusted_total / (len(scores) - 1)
    return round(adjusted_average, 2)

if __name__ == "__main__":
    # Example Usage
    scores = list(map(int, input("Enter the test scores separated by spaces: ").split()))
    average = calculate_adjusted_average(scores)
    print(f"Average after dropping the lowest score: {average}")
