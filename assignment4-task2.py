# Assignment 4 - Task 2
# Write and append data to a file

filename = "output.txt"

# Write to the file
text = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

# Append to the file
additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    print(file.read())