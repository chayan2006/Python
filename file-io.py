# 📂 File Input and Output (I/O) in Python

# 1. Opening and Closing Files
# 'r' - Read (default)
# 'w' - Write (overwrites everything)
# 'a' - Append (adds to the end)
# 'r+' - Read and Write

# Always use 'with' statement - it closes the file automatically!
with open("test.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python File I/O is very easy!\n")

# Reading the whole file
with open("test.txt", "r") as file:
    content = file.read()
    print("Full Content:\n", content)

# Reading line by line (Memory efficient)
with open("test.txt", "r") as file:
    for line in file:
        print("Reading line:", line.strip())

# Appending content
with open("test.txt", "a") as file:
    file.write("This line was added later!\n")

# Working with lists and files
lines_to_write = ["First Line\n", "Second Line\n", "Third Line\n"]
with open("test.txt", "w") as file:
    file.writelines(lines_to_write)

# 2. Path Handling (os module)
import os

if os.path.exists("test.txt"):
    print("Found it!")
    # os.remove("test.txt") # Be careful! Deletes file
else:
    print("File not found")

# 3. CSV Files (Built-in csv module)
import csv

# Writing to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Skill"])
    writer.writerow(["Chayan", 18, "Python"])
    writer.writerow(["Deepmind", 10, "AI"])

# Reading from CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Summary of Mode Specifiers
"""
| Mode | Action                                          |
|------|-------------------------------------------------|
| 'r'  | Opens for reading (error if file doesn't exist) |
| 'w'  | Opens for writing (creates/overwrites)          |
| 'a'  | Opens for appending (creates if doesn't exist)  |
| 'rb' | Opens for reading in binary (images/videos)      |
| 'wb' | Opens for writing in binary                     |
"""
