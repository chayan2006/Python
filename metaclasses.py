# 🧠 Metaclasses: The Class of a Class

# 1. Why use Metaclasses?
# To automatically change or validate classes as they are being created.
# This is a very deep, advanced feature (most don't need it daily!)

# 🚀 Concept: Classes ARE objects too! 
# Just like 'int' creates number objects, 'type' creates class objects.

# 2. Basic Example: Customizing Class Creation
class MyMeta(type):
    # __new__ creates the class object
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        # Let's force all attributes to be uppercase! (Example only)
        new_dct = {k.upper() if not k.startswith("__") else k: v for k, v in dct.items()}
        return super().__new__(cls, name, bases, new_dct)

class MyClass(metaclass=MyMeta):
    x = 10
    def say_hi(self):
        print("Hello!")

obj = MyClass()
# print(obj.x) # This will FAIL! 
print(obj.X) # We forced it to be uppercase! (10)

# 3. Practical Use: Enforcing Singleton Pattern
# Singleton ensures ONLY ONE instance of a class ever exists!
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    pass

db1 = Database()
db2 = Database()
print("Is it the same db instance?", db1 is db2) # True!

# Summary Table
"""
| Method         | Purpose                                        |
|----------------|------------------------------------------------|
| __new__()      | Runs BEFORE the class is created (to modify) |
| __init__()     | Runs AFTER the class is created (to setup)    |
| __call__()     | Runs when you try to CREATE an instance (obj) |
| type()         | The default metaclass for all Python classes   |
| metaclass      | Keyword used to link your custom meta-logic    |
"""
