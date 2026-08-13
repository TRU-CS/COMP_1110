def check_exam_eligibility():
    # Get the number of classes held and attended from the user
    classes_held = int(input("Enter the number of classes held: "))
    classes_attended = int(input("Enter the number of classes attended: "))
    
    # Calculate the attendance percentage
    attendance_percentage = (classes_attended / classes_held) * 100
    
    # Display the attendance percentage
    print(f"Percentage of classes attended: {attendance_percentage:.2f}%")
    
    # Determine eligibility
    if attendance_percentage >= 90:
        print("The student is permitted to take the exam.")
    else:
        print("The student is not permitted to take the exam.")

# Call the function
check_exam_eligibility()