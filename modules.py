import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create file paths relative to the script
file1_path = "file.txt"
file2_path = "file.txt2"

f = open(file1_path, "w")
f.write("mio")
f.close() # Good practice to close before re-opening

f = open(file1_path, "r")
print(f.read())
print(f.tell())
f.close()

f = open(file2_path, "w")
f.write("Hello, World!")
f.close()

f = open(file2_path, "r")
print(f.read())
f.close()

f = open(file2_path, "a")
f.write("Hello, World!")
f.close()

f = open(file2_path, "r")
print(f.read())
print(f.tell())
f = open(file2_path, "x ")