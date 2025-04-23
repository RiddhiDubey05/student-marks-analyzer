def get_student_data():
    name = input("Enter students name:")
    roll = input("Enter students roll_number:")
    marks = []
    for i in range(5):
                 mark = int(input(f"Enter marks for subject {i+1}:"))
                 marks.append(mark)
    return {"name": name, "roll_number": roll, "marks": marks}#inside the function 


def calculate_average(marks):
    return sum(marks)/len(marks)

def assign_grade (average):
    if average >= 90: 
     return "A+"
    elif average >= 80:
     return "A"
    elif average >= 70:
     return "B"
    elif average >= 60:
     return "C"
    elif average >= 50:
     return "D"
    else:
     return "Fail"

#Driver code

student = get_student_data()
average = calculate_average(student["marks"])
grade = assign_grade(average)
print("\n STUDENT REPORT")
print(f"Name: {student['name']}")
print(f"roll: {student['roll_number']}")
print(f"Marks: {student['marks']}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")

from analyzer import collect_student_data
from file_handler import save_results_to_file

students = collect_student_data()
save_results_to_file(students)




