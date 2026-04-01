# 📜 List, Dictionaries, Tuples, and Sets in Python

# 1. Lists: Ordered, Mutable, Allows Duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # Adds to the end
fruits.insert(1, "mango") # Adds at index 1
fruits.remove("banana") # Removes specific item
popped = fruits.pop() # Removes and returns last item
fruits.sort() # Sorts the list
fruits.reverse() # Reverses the list

# List Slicing
# list[start:stop:step]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])   # [2, 3, 4]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4, 6, 8] (Even numbers)

# List Comprehension (Elegant way to create lists)
squares = [x**2 for x in range(10)] 
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. Tuples: Ordered, Immutable, Allows Duplicates
# Used for data that shouldn't change
point = (10, 20)
# point[0] = 30 # This would cause an ERROR
print(point.count(10)) # Returns number of times 10 appears
print(point.index(20)) # Returns index of 20

# 3. Dictionaries: Key-Value pairs, Ordered (since Python 3.7+), No duplicate keys
student = {
    "name": "Chayan",
    "age": 18,
    "courses": ["Python", "JavaScript"]
}

print(student["name"])
print(student.get("phone", "Not Found")) # Safer way to access keys

student["phone"] = "555-5555" # Add/Update
student.update({"age": 19, "city": "Kolkata"}) # Update multiple fields

# Dictionary Methods
print(student.keys())
print(student.values())
print(student.items()) # Returns (key, value) tuples

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Sets: Unordered, Mutable, No Duplicates
my_set = {1, 2, 3, 4, 4, 4}
print(my_set) # Result: {1, 2, 3, 4} - duplicates removed

my_set.add(5)
my_set.remove(2)

# Set Operations (Math)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))        # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b)) # {3, 4}
print(set_a.difference(set_b))   # {1, 2}

# Summary Table
"""
| Data Structure | Ordered | Mutable | Duplicates | Syntax |
|----------------|---------|---------|------------|--------|
| List           | Yes     | Yes     | Yes        | []     |
| Tuple          | Yes     | No      | Yes        | ()     |
| Dictionary     | Yes*    | Yes     | No (Keys)  | {k:v}  |
| Set            | No      | Yes     | No         | {}     |
"""
