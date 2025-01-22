# Python Programming: Lab Activity 2 Template
# Instructions: Complete the functions by replacing the placeholders with your code.
# Do not modify the function names, parameters, or return statements.

# 1. Calculate Distance Traveled
def calculate_distance():
    """
    Calculates and returns the distance a car travels at a speed of 70 miles per hour
    for 6 hours and 10 hours.
    """
    speed = None  # Replace None with the car's speed (e.g., user input or given value)
    time_6_hours = None  # Replace None with the time for the first calculation (e.g., 6 hours)
    time_10_hours = None  # Replace None with the time for the second calculation (e.g., 10 hours)
    
    # Replace None with the calculated distances
    distance_6_hours = None  # Calculate the distance for 6 hours
    distance_10_hours = None  # Calculate the distance for 10 hours
    
    print("1. Distance Traveled:")
    print(f"The car will travel {distance_6_hours} miles in 6 hours.")
    print(f"The car will travel {distance_10_hours} miles in 10 hours.\n")
    
    return distance_6_hours, distance_10_hours


# 2. Calculate Miles-Per-Gallon (MPG)
def calculate_mpg():
    """
    Calculates and returns the miles-per-gallon (MPG) based on user input for
    miles driven and gallons of gas used.
    """
    print("2. Calculate Miles-Per-Gallon (MPG):")
    miles = None  # Replace None with user input for miles driven
    gallons = None  # Replace None with user input for gallons of gas used
    
    mpg = None  # Replace None with the calculation for MPG (miles / gallons)
    
    print(f"The car's MPG is {mpg}.\n")
    return mpg


# 3. Convert Seconds to Minutes and Seconds
def convert_seconds():
    """
    Converts a given number of seconds into minutes and remaining seconds,
    if the input is greater than or equal to 60 seconds.
    """
    print("3. Convert Seconds to Minutes and Seconds:")
    seconds = None  # Replace None with user input for total seconds
    
    minutes = None  # Replace None with the calculated minutes
    remaining_seconds = None  # Replace None with the remaining seconds
    
    print(f"{seconds} seconds is equal to {minutes} minute(s) and {remaining_seconds} second(s).\n")
    return minutes, remaining_seconds


# 4. Book Club Points System
def book_club_points():
    """
    Calculates and returns the points awarded based on the number of books purchased.
    """
    print("4. Book Club Points System:")
    books_purchased = None  # Replace None with user input for books purchased
    
    points = None  # Replace None with the logic to determine points based on books purchased
    
    print(f"Points awarded: {points}\n")
    return points


# 5. Day of the Week
def day_of_week():
    """
    Determines and returns the day of the week corresponding to a number (1-7) provided by the user.
    """
    print("5. Day of the Week:")
    day_number = None  # Replace None with user input for the day number
 
    
    day_name = ''  # Replace '' with the corresponding day name using the day_number
    
    return day_name.lower()


# Main Program
if __name__ == "__main__":
    # Call each function and store their return values
    distance_results = calculate_distance()
    mpg_result = calculate_mpg()
    time_conversion = convert_seconds()
    book_points = book_club_points()
    weekday = day_of_week()

    # Output summary of returned values (optional for students)
    print("\nSummary of Results:")
    print(f"Distance Traveled: {distance_results}")
    print(f"Car's MPG: {mpg_result}")
    print(f"Time Conversion: {time_conversion}")
    print(f"Book Club Points: {book_points}")
    print(f"Day of the Week: {weekday}")
