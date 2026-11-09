#File Handling in python

# Input: Reading information from a file into your Python program.
# Output: Writing information from your Python program into a file.

from pathlib import Path

# Approach 1
# file = open("student.txt","w") # open() = Opens a file and returns a file object

# file.write("Good Morning.")
# file.write("\nI am learning Python File I/O Handling")

# file.close()

# Step 1: Write to the file
with open("student.txt", "w") as file:
    file.write("Good Morning.")
    file.write("\nI am learning Python File I/O Handling")

# Step 2: Read from the file
with open("student.txt", "r") as file:
    data = file.readlines()
    print(data)

with open("student.txt","a") as file: # a = append
    file.write("\nIt's easy")

with open("student.txt", "r") as file:
    data = file.readlines()
    print(data)


# The with statement automatically closes the file when its block finishes, even if an exception occurs inside the block.

try:
    with open("missing.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("Sorry, the file does not exist.")

# ------------------------------------------------------------------------------


folder = Path("data") # Path("data") represents a folder path.
folder.mkdir(exist_ok=True) # mkdir(exist_ok=True) creates the folder if it doesn't already exist

file_path = folder / "student.txt" # the / operator joins path components.

with file_path.open("w", encoding="utf-8") as file:
    file.write("Hello Python")

# Encoding determines how text is represented as bytes in the file. UTF-8 handles English, Hindi, Bengali, and many other writing systems.It is a good habit to specify encoding="utf-8" explicitly for text files.

#---------------------------------------------------

import json

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

with open("student.json", "w", encoding="utf-8") as file: #Python automatically creates a file when you open it in "w" (write) mode, if the file doesn't already exist.
    json.dump(student, file, indent=4)

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student["name"])

#"w" mode clears existing file content immediately upon opening, even when you don't write anything afterward.