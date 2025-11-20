print("Welcome to your calculator")
print("choice")
print("1.Adiition")
print("2.Subtraction")
print("3.Multipilcation")
print("4.Division")

choice = input("Enter your choice (1/2/3/4):")

num1 = float(input("Enter the frist num:"))
num2 = float(input("Enter the seconde num:"))

if choice == '1':
    print("Result:",num1+num2)

if choice == '2':
    print("Result",num1-num2)

if choice == '3':
    print("Result",num1*num2)

if choice == '4':
    print("Result",num1/num2)