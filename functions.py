
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

