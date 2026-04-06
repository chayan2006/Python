# 📦 Modules and Packages in Python

# 1. Importing Standard Library
import math
print(math.sqrt(16)) # square root
print(math.pi) # pi constant

import random
print(random.randint(1, 10)) # Random number between 1 and 10
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits)) # Random element from list

import datetime
now = datetime.datetime.now()
print("Current Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 2. Aliasing (Giving modules a shorter name)
import statistics as stats
data = [10, 20, 30, 40, 50]
print("Mean:", stats.mean(data))

# 3. Importing Specific Functions
from os import name, path
print("OS Name:", name) # posix (Mac/Linux) or nt (Windows)

# 4. JSON Module (Data exchange)
import json
person_dict = {"name": "Chayan", "age": 18, "city": "Kolkata"}
json_string = json.dumps(person_dict) # Dictionary to JSON String
print("JSON String:", json_string)
new_dict = json.loads(json_string) # JSON String to Dictionary

# 5. Third-Party Modules (Need 'pip install')
# Example: requests (For HTTP requests)
'''
# Run this in terminal to install:
# pip install requests 

import requests
response = requests.get('https://api.github.com')
print(response.status_code)
'''

# 6. How to create your own Module?
# Save a file as `my_calc.py`:
'''
def add(a, b):
    return a + b
'''
# Then import it in another file:
'''
import my_calc
print(my_calc.add(5, 10))
'''

# 7. Regular Expressions (RE) - Advanced Text Searching
import re
text = "The rain in Spain"
# Search for 'rain' anywhere in the string
match = re.search("^The.*Spain$", text) # Starts with The, ends with Spain
if match:
    print("YES! We have a match!")

# Summary of Imports
"""
| Method                     | Example                         | Recommended? |
|----------------------------|---------------------------------|--------------|
| full import                | import math                     | Best for clarity |
| alias import               | import numpy as np              | Best for short names |
| partial import              | from math import sqrt           | Best for performance |
| wildcard (DON'T USE)       | from math import *              | Bad practice! |
"""