def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask for the student's name
    student_name = input("Enter the student's name: ")

    # Ask for the number of subjects
    num_subjects = int(input("Enter the number of subjects: "))

    # Initialize total score
    total_score = 0

    # Loop to collect scores for each subject
    for i in range(1, num_subjects + 1):
        score = float(input(f"Enter the score for subject {i}: "))
        total_score += score

    # Calculate average score
    average_score = total_score / num_subjects

    # Calculate grade based on average score
    grade = calculate_grade(average_score)

    # Display the results
    print(f"\nStudent: {student_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")

# Run the program
if __name__ == "__main__":
    main()
