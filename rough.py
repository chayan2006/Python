from abc import ABC 

class Animal(ABC):
    
    def make_sound(self):
        pass

    
    def name(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def name(self):
        return "Dog"

class Cat(Animal):
    def make_sound(self):
        return "Meow..."

    def name(self):
        return "Cat"

class Lion(Animal):
    def make_sound(self):
        return "ROAR!!!"

    def name(self):
        return "Lion"

class Duck(Animal):
    def make_sound(self):
        return "Quack! Quack!"

    def name(self):
        return "Duck"

class Elephant(Animal):
    def make_sound(self):
        return "Pawoo! Pawoo!"

    def name(self):
        return "Elephant"

which_Animal = input("which animal :").strip().lower()
if which_Animal == "dog":
    print(Dog().make_sound())
elif which_Animal == "cat":
    print(Cat().make_sound())
elif which_Animal == "lion":
    print(Lion().make_sound())
elif which_Animal == "duck":
    print(Duck().make_sound())
elif which_Animal == "elephant":
    print(Elephant().make_sound())
else:
    print("Unknown animal!")


# Emplyoee Mystery Bones : Empoyee have different bonus rules. Comput Bonuses without knowing employee type in loop(polymorphism)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1
