def check_exam_eligibility():
    # Get the number of classes held and attended from the user
    total_classes = int(input("Enter the number of classes held: "))
    classes_attended = int(input("Enter the number of classes attended: "))
    
    # Validate input to avoid division by zero
    if total_classes <= 0:
        print("The number of total classes must be greater than 0.")
        return
    
    # Calculate the attendance percentage
    attendance_percentage = (classes_attended / total_classes) * 100
    
    # Display the attendance percentage
    print(f"Percentage of classes attended: {attendance_percentage:.2f}%")
    
    # Determine eligibility
    if attendance_percentage >= 90:
        print("You are permitted to take the exam.")
    else:
        print("You are not permitted to take the exam.")

    return attendance_percentage
