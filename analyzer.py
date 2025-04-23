def collect_student_data():
    students = []
    while True:
        name = input("Enter studnet's name:(or 'exit' to finish)")
        if name.lower() == exit:
            break
        marks = list(map(int,input("Enter the marks separated by space:").split()))
        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = 'A'
        elif average >= 75:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        else:
            grade = 'D'
            student = {
                "Name": name,
                "Marks": marks,
                "Total": total,
                "Average": average,
                "Grade": grade
            }
            students.append(student)
            return students

