def save_results_to_file(students, filename="student_results.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"Name: {student['Name']}\n")
            file.write(f"Marks: {student['Marks']}\n")
            file.write(f"Total: {student['Total']}\n")
            file.write(f"Average: {student['Average']:.2f}\n")
            file.write(f"Grade: {student['Grade']}\n")
            file.write("-" * 20 + "\n")
