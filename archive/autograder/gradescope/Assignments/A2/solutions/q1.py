def convert_to_miles(distance_km: float):  
    """
    Asks the user to enter a distance in kilometers, converts it to miles,
    and displays the result.
    """
    # Ask the user to enter a distance in kilometers
    kilometers = float(input("Enter distance in kilometers: "))
    
    # Convert kilometers to miles using the formula
    miles = kilometers * 0.6214
    
    # Display the result
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

    return miles