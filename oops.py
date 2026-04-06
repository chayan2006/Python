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


# --- THE 4 PILLARS OF OOP ---

# 1. Inheritance (Code Reuse)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def drift(self):
        print(f"The {self.brand} is drifting!")

class ElectricCar(Vehicle): # ElectricCar inherits from Vehicle
    def __init__(self, brand, battery_size):
        super().__init__(brand) # super() calls parent class
        self.battery_size = battery_size
    def charge(self):
        print("Charging battery...")

# 2. Encapsulation (Hiding Data)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute (starts with __)
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return f"Balance: {self.__balance}"

# 3. Polymorphism (Multiple Shapes)
# Same method name, different behaviors
class Dog:
    def speak(self): return "Woof!"
class Cat:
    def speak(self): return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) # prints differenly based on class

# 4. Abstraction (Hiding Complexity)
from abc import ABC, abstractmethod
class Shape(ABC): # Abstract class
    @abstractmethod
    def area(self): # Must be implemented by child class
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

# --- SPECIAL DECORATORS ---
class Player:
    def __init__(self, name, score):
        self._name = name # Protected attribute
        self.score = score
    
    @property # Getter (makes function look like attribute)
    def name(self):
        return self._name.upper()

    @staticmethod # No self, doesn't need object
    def intro():
        print("Welcome to the game!")

    @classmethod # Needs access to class (cls)
    def create_from_tuple(cls, data):
        return cls(data[0], data[1])

Player.intro() # static method called on class
player1 = Player.create_from_tuple(("Chayan", 100)) # class method called on class
print(player1.name) # property called like attribute (CHAYAN)
