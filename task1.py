"""
Task 1: Perform Basic Mathematical Operations
Module 2: Basic Python Concepts
Platform: Tutedude
"""

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Displaying results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)