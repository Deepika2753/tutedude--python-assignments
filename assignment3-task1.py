# Assignment 3 - Task 1
# Calculate factorial using a function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
num = int(input("Enter a number: "))

# Calling the function and printing result
print(f"Factorial of {num} is:", factorial(num))