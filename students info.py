students = []

name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

students_record = {"name": name, "marks": marks}
students.append(students_record)

print(f"student (name)'s marks are added successfully")

print("/n All students Data:")
for student in students: 
    print(f"Name: {student['name']}, Marks: {student['marks']}")