print("Hello World")
# This is single line comment 
print("Hello World") # This will print a message 
'''
this is
 multi-line 
 comment 
 in python 
'''


# a variable is like a box which will store the data - number , string , float , boolen etc 
x = 2 # integer
name = "Chayan " #string
pi = 13.4 #float
is_ready = True #boolean


       #Operators ⚙️
 
'''
| Type       | Example                 | Meaning                                                           |
| ---------- | ----------------------- | ----------------------------------------------------------------- |
| Arithmetic | `+  -  *  /  %  **  //` | add, subtract, multiply, divide, remainder, power, floor division |
| Comparison | `==  !=  >  <  >=  <=`  | compare values (True or False)                                    |
| Assignment | `=  +=  -=  *=  /=`     | store or update values                                            |
| Logical    | `and, or, not`          | combine conditions                                                |

'''

# Input from the User 🎯
name = input("Enter your Name: ")
print("Hello",name )
# Output will be = Hello 'User name '

x = int(input("Enter a number: "))
print(x + 5)  # For integer

x = float(input("Enter a decimal number: "))
print(x + 5) # For float 

#✨ Basic string operations
Name = "Chayan "
print(len(Name))
print(Name.upper())
print(Name.lower())
print(Name[0])
print(Name[1:4])


#Variables Annotated by Type#

import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.2
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

#Activity 
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay:" + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types

"""
Logical Operators
Logical operators are used to construct more complex expressions. You can make complex comparisons by joining comparison statements together using the logical operators: and, or, not. Complex comparisons return a Boolean (True or False) result. 

and 

Both sides of the statement being evaluated must be True for the whole statement to be True. 

Example: (5 > 1 and 5 < 10) = True

or 

If either side of the comparison is True, then the whole statement is True. 

Example: (color = "blue" or color = "green") = True

not 

Inverts the Boolean result of the statement immediately following it. So, if a statement evaluates to True, and we put the not operator in front of it, it would become False. 

Example: (not "A" == "A") = False

"""
# Example 1

print((6*3 >= 18) and (9+9 <= 36/2))

# Example 2

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# Define country and city variables
country = "United States"
city = "New York City"

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))  # True or True = True

# False or True returns True
print(country == "New York City" or city == "New York City")  # False or True = True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)  # True or False = True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False
# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

# What happens when you negate a False statement? 
# Click Run when you are ready to check your answer.


today = "Monday"
print(not today == "Tuesday") 


# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means 
# True."


