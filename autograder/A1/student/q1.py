def check_exam_eligibility():
    # Get the number of classes held and attended from the user
    total_classes = int(input("Enter the number of classes held: "))
    classes_attended = int(input("Enter the number of classes attended: "))
    
    
    # Calculate the percentage of classes attended
    attendance_percentage = (classes_attended / total_classes) * 100
    
    # Print the percentage of classes attended formatted to 2 decimal places
    print(f"Percentage of class attended: {attendance_percentage:.2f}%")
    
    # Check if the student is permitted to take the exam
    if attendance_percentage >= 90:
        print("You are permitted to take exams.")
    else:
        print("You are not permitted to take exams.")

if __name__ == "__main__":

    check_exam_eligibility()