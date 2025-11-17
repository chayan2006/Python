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

