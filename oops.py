# class Student: # Student is the class 
#     def __init__(self):
#      print("adding new student in database")

#     def __init__(self,name,marks):
#        self.name = name 
#        self.marks = marks
#        print("adding new student in Database..")
    

# s1  = Student("Chayan",82) #  s1 is  the object for that class (Student)
# print(s1.name) #Chayan 

# s2 = Student ("raj",89)
# print(s2.name)#Raj 

# print(s2.marks)#89



class Car:  # Car is the class (blueprint)
    def __init__(self, name, colour):  # __init__ runs when an object is created
        self.name = name    # attribute of the object
        self.colour = colour  # attribute of the object

c1 = Car("BMW", "black")  # c1 is an object (instance of Car)
print(c1.name)    # printing the object's name attribute
print(c1.colour)  # printing the object's colour attribute


Name = input("Enter your name: ")
Language = input("Enter your language: ")
Salary = 0 
if Language == "python":
    Salary += 1000000
elif Language == "java":
    Salary += 1000000000000
elif Language == "c++":
    Salary += 100000000000000000
   
class Employess:
    name = Name 
    language = Language 
    salary = Salary

Employess1 = Employess()

print(Employess1.name,Employess1.language,Employess1.salary)
# if Language == "python":
#         print("salary:30k")
# elif Language == "C++":
#           print("salary:50k")
# elif Language== "java":
#             print("salary:70k")


# more refined code 
