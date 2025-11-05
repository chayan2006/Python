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