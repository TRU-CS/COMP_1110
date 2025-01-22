# Python Programming: Lab Activity 2 Solutions with Return Values

# 1. Calculate Distance Traveled
def calculate_distance():
    speed = 70  # in miles per hour
    time_6_hours = 6
    time_10_hours = 10
    
    distance_6_hours = speed * time_6_hours
    distance_10_hours = speed * time_10_hours
    
    print("1. Distance Traveled:")
    print(f"The car will travel {distance_6_hours} miles in 6 hours.")
    print(f"The car will travel {distance_10_hours} miles in 10 hours.\n")
    
    return distance_6_hours, distance_10_hours


# 2. Calculate Miles-Per-Gallon (MPG)
def calculate_mpg():
    print("2. Calculate Miles-Per-Gallon (MPG):")
    miles = float(input("Enter the number of miles driven: "))
    gallons = float(input("Enter the gallons of gas used: "))
    
    if gallons > 0:
        mpg = miles / gallons
        print(f"The car's MPG is {mpg:.2f}.\n")
        return mpg
    else:
        print("Gallons of gas used must be greater than 0.\n")
        return None


# 3. Convert Seconds to Minutes and Seconds
def convert_seconds():
    print("3. Convert Seconds to Minutes and Seconds:")
    seconds = int(input("Enter the number of seconds: "))
    
    if seconds >= 60:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        print(f"{seconds} seconds is equal to {minutes} minute(s) and {remaining_seconds} second(s).\n")
        return minutes, remaining_seconds
    else:
        print(f"{seconds} seconds is less than 1 minute.\n")
        return seconds, 0


# 4. Book Club Points System
def book_club_points():
    print("4. Book Club Points System:")
    books_purchased = int(input("Enter the number of books purchased this month: "))
    
    if books_purchased == 0:
        points = 0
    elif books_purchased in [1, 2]:
        points = 5
    elif books_purchased in [3, 4]:
        points = 15
    elif books_purchased in [5, 6]:
        points = 30
    else:
        points = 60
    
    print(f"Points awarded: {points}\n")
    return points


# 5. Day of the Week
def day_of_week():
    print("5. Day of the Week:")
    day_number = int(input("Enter a number (1-7): "))
    
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if day_number in days:
        print(f"The corresponding day is {days[day_number]}.\n")
        return days[day_number].lower()
    else:
        print("Error: Please enter a number between 1 and 7.\n")
        return None


# Main Program
if __name__ == "__main__":
    # Call each function and store their return values
    distance_results = calculate_distance()
    mpg_result = calculate_mpg()
    time_conversion = convert_seconds()
    book_points = book_club_points()
    weekday = day_of_week()

    # Output summary of returned values
    print("\nSummary of Results:")
    print(f"Distance Traveled: 6 hours -> {distance_results[0]} miles, 10 hours -> {distance_results[1]} miles")
    if mpg_result is not None:
        print(f"Car's MPG: {mpg_result:.2f}")
    print(f"Time Conversion: {time_conversion[0]} minutes, {time_conversion[1]} seconds")
    print(f"Book Club Points: {book_points}")
    if weekday is not None:
        print(f"Day of the Week: {weekday}")
