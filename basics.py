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


