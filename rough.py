# from abc import ABC 

# class Animal(ABC):
    
#     def make_sound(self):
#         pass

    
#     def name(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof! Woof!"

#     def name(self):
#         return "Dog"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow..."

#     def name(self):
#         return "Cat"

# class Lion(Animal):
#     def make_sound(self):
#         return "ROAR!!!"

#     def name(self):
#         return "Lion"

# class Duck(Animal):
#     def make_sound(self):
#         return "Quack! Quack!"

#     def name(self):
#         return "Duck"

# class Elephant(Animal):
#     def make_sound(self):
#         return "Pawoo! Pawoo!"

#     def name(self):
#         return "Elephant"

# which_Animal = input("which animal :").strip().lower()
# if which_Animal == "dog":
#     print(Dog().make_sound())
# elif which_Animal == "cat":
#     print(Cat().make_sound())
# elif which_Animal == "lion":
#     print(Lion().make_sound())
# elif which_Animal == "duck":
#     print(Duck().make_sound())
# elif which_Animal == "elephant":
#     print(Elephant().make_sound())
# else:
#     print("Unknown animal!")


# # Emplyoee Mystery Bones : Empoyee have different bonus rules. Comput Bonuses without knowing employee type in loop(polymorphism)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return self.salary * 0.1
# class Bonus(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.2

# employees = [Employee("John", 5000), Bonus("Jane", 6000)]
# for employee in employees:
#     print(employee.calculate_bonus())
class Numbers:
    def __init__(self,num):
        self.num  = num 
    def even(self):
        if self.num % 2 == 0:
            return True
        else:
            return False

    def odd(self):
        if self.num % 2 != 0:
            return True
        else:
            return False
    def prime(self):
        if self.num > 1:
            for i in range(2,self.num):
                if self.num % i == 0:
                    return False
            return True
#now taking input form the user 
numbers = int(input("Num: "))
import re 
s = "marks123 is 90"
print(re.findall(r"c",abcdczy))
 
