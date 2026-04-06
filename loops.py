# Loops are use to repeat instrutions
'''
Docstring for python_journey.Python.loops
'''
# Loops are two type = while , for 
count = 1 
while count <= 5 :
    print("hello")
    count += 1

'''
count is know as Iterator
and the runing of one full loop is know as Iteration
'''
# Print numbers form 1 to 100 
i = 1
while i <= 100:
    print(i)
    i += 1 
print("Loop ended")


# Print number 100 to 1 
i = 100 
while i >= 1 :
    print(i)
    i -= 1 
print("Loop ended ")

# Print  the multiplication table of a number n . 
n = int(input("Enter the table : "))
i = 1 
while i <= 10 : 
    print(n*i)
    i += 1 
print("Loop ended ")

# Print the element of the following list using a loop :
"""
[1,4,9,16,25,36,49,64,81,100]

"""
nums = [1,4,9,16,25,36,49,64,81,100 ]
idx = 0 
while idx < len(nums):
    print(nums[idx])
    idx +=1


    # Count-Controlled Loops 
product = 1 
for count in range (4):
    product  = product* (count+1)
print(product)
"""
how this upper code works:
product = 1* (0+1)
= 1*1 = 1
now the product will be 1 
and the ;loop will run again 
product = 1 *(1+1)
  = 1*2 = 2 
  now the peoduct will be 2 an t he loop will run again 
  product = 2 *(2+1)
   2 *3
   = 6 
   product = 6*(3+1)
    = 24 
    and the loop will end becoused the cout +1 become 4 


"""

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum  = 0 
for number in range (lower, upper+1):
    theSum = theSum+number

# Updated Loop Concepts
print(theSum)

# --- ADVANCED LOOP CONTROL ---

# 1. Break: Exit the loop instantly
# Find the first number divisible by 7 in range (10, 50)
for num in range(10, 51):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break # Skips all remaining numbers

# 2. Continue: Skip the current iteration but stay in the loop
# Print all odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue # Skips even numbers
    print(i) # Prints only odd numbers

# 3. Pass: A placeholder for empty code (to avoid errors)
def future_function():
    pass # No error even if function does nothing yet

# 4. Enumerate: Get index and value simultaneously
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

# 5. Zip: Loop through two lists at once
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 6. For-Else: Code that runs ONLY if the loop DID NOT break
# Example: Check if a number is prime
check_num = 11
for i in range(2, check_num):
    if check_num % i == 0:
        print(f"{check_num} is not prime.")
        break
else:
    # This only runs if we didn't hit 'break'
    print(f"{check_num} is a prime number!")

