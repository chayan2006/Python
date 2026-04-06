
# Return Statement 
'''
the return statement is used to exit the current funtion
 that is being executed and to transfer control back to the 
 point where the funtion was called
'''
# Q = Take two interger parameters a and b from the user using input() funtion . Define three functions addavg(), sub and mul to perform average , subtration and multiplication on the given two parameters a and b respectively and print the result  as shown in the example
a = int(input("a: "))
b = int(input("b: "))

def addavg():
    return (a+b/2)

def sub():
    return (a-b )
def mul():
    return ( a*b)

print("average:",addavg())
print("subtraction:",sub())
print("multipication:",mul())

#Parameters & Arguments
'''
Parameters: when you defind a function you list parameters inside the parentheses
parameters act like local variable with the function , holding the value provided by arguments 
Argument: An argument is an expression passed to a function by its caller , enabling the function to perform its task 
'''
# Q .Fill the fuction add()which taes two parameters a and b Inside the function add a , b and retrun thr result.
d = int(input("a: "))
e = int(input("b: "))

def add(a,b):# a and b is the parameters in this function 
    return a+b# perform addition on the passed parameters 
# return the result 
x = add (d,e)# call the add( )fuction   by passing d & e as a argument 
print(x)

def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")

def greeting(name,department):
    print("Welcome "+name)
    print("Welcome to our "+ department +" department")

greeting("Chayan","CSE")
greeting("Amit","CSE")

# print()
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

# type()
print(type("This is a string"))

# str()
number = 12
string_representation = str(number)
print(string_representation)

# sorted 
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)

# max() & min()
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")



def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")
#This code will not have an output. 

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

hint_username("chayan khatua")
# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# --- ADVANCED FUNCTION CONCEPTS ---

# 1. Default Parameters (Used when no value is provided)
def greet_user(name="Guest"):
    print("Welcome, " + name)

greet_user() # prints Welcome, Guest
greet_user("Chayan") # prints Welcome, Chayan

# 2. *args (Pass multiple arguments as a tuple)
def calculate_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(calculate_sum(1, 2, 3, 4, 10)) # Any number of arguments works

# 3. **kwargs (Pass multiple keyword arguments as a dictionary)
def print_user_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_user_details(name="Chayan", role="AI Agent", status="Active")

# 4. Lambda Functions (Short, one-line functions)
# Syntax: lambda parameters : expression
multiply = lambda x, y : x * y
print(multiply(5, 5)) # returns 25

# Combining with sorted()
points = [(1, 2), (4, 1), (5, -1), (2, 3)]
points_sorted = sorted(points, key=lambda x: x[1]) # sort by the second value
print(points_sorted)

# 5. Local vs Global Scope
msg = "I am Global" # Accessible everywhere

def show_scope():
    msg = "I am Local" # Exists only inside the function
    print(msg)

show_scope() # Prints Local
print(msg) # Prints Global


# Expected output:
# Requested web page not found on server