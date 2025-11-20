# This is my first project And i make the calculator 
while True:
     print("Welcome to your calculator")
     print("choice")
     print("1.Adiition")
     print("2.Subtraction")
     print("3.Multipilcation")
     print("4.Division")
# This will take the input form the user that which operation he whould like o do ...
     choice = input("Enter your choice (1/2/3/4):")
# Thia will take input form the user for the num which num user want in the oparation 
     num1 = float(input("Enter the frist num:"))
     num2 = float(input("Enter the seconde num:"))
 # This is th statement where the oparation will hwld according the user that he choice  and it will give the result according to the user 
     if choice == '1':
          print("Result:",num1+num2)

     if choice == '2':
          print("Result",num1-num2)

     if choice == '3':
         print("Result",num1*num2)

     if choice == '4':
         print("Result",num1/num2)
         #Taking the confirmation for the user if the user is want to use the cal agaian or not 
     again = input("Do u want to use the cal again(yes/no): ")
     # if the user want use it again it will run the loop again and start the cal 
     if again == "yes":
        print("Again welcome to the cal")
        # if the user  do not want the cal it will stop the loop and print the given statmenr
     else:
       print("Thankyou for use the cal ")
     break