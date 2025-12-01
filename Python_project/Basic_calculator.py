     print("4. Division")
     print("5. Power")
     print("6. Modulus")
     print("7. Floor Division")
     print("8. Square Root")
     print("9. Factorial")
     print("10. Sine")
     print("11. Cosine")

# This will take the input form the user that which operation he whould like o do ...
     choice = input("Enter your choice (1-11): ")

     if choice in ['1', '2', '3', '4', '5', '6', '7']:
          num1 = float(input("Enter the first num: "))
          num2 = float(input("Enter the second num: "))
     elif choice in ['8', '9', '10', '11']:
          num1 = float(input("Enter the number: "))
     else:
          print("Invalid choice")
          continue

 # This is th statement where the oparation will hwld according the user that he choice  and it will give the result according to the user 
     if choice == '1':
          print("Result:", num1 + num2)

     elif choice == '2':
          print("Result:", num1 - num2)

     elif choice == '3':
         print("Result:", num1 * num2)

     elif choice == '4':
         if num2 == 0:
             print("Error: Cannot divide by zero!")
         else:
             print("Result:", num1 / num2)
             
     elif choice == '5':
         print("Result:", num1 ** num2)
         
     elif choice == '6':
         print("Result:", num1 % num2)

     elif choice == '7':
         if num2 == 0:
              print("Error: Cannot divide by zero!")
         else:
              print("Result:", num1 // num2)

     elif choice == '8':
         if num1 < 0:
              print("Error: Cannot calculate square root of a negative number")
         else:
              print("Result:", math.sqrt(num1))

     elif choice == '9':
         if num1 < 0:
              print("Error: Factorial does not exist for negative numbers")
         else:
              print("Result:", math.factorial(int(num1)))

     elif choice == '10':
         print("Result:", math.sin(num1))

     elif choice == '11':
         print("Result:", math.cos(num1))

     #Taking the confirmation for the user if the user is want to use the cal agaian or not 
     again = input("Do u want to use the cal again(yes/no): ")
     # if the user want use it again it will run the loop again and start the cal 
     if again.lower() == "yes":
        print("Again welcome to the cal")
        # if the user  do not want the cal it will stop the loop and print the given statmenr
     else:
       print("Thankyou for use the cal ")
       break