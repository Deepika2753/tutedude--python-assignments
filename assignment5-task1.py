# Assignment 5 - Task 1
# Dictionary of student marks

# Creating the dictionary
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Taking input from user
name = input("Enter the student's name: ")

# Checking and displaying marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")