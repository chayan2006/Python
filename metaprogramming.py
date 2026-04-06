# 🧠 Meta-programming: Dynamic Object Manipulation

import inspect

# 1. Introspection: Asking objects about themselves
class Player:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print(f"I am {self.name}")

p = Player("Dev")

# dir(): Get all attributes and methods
# print("dir():", dir(p))

# isinstance(): Check if object IS an instance of a class
print("isinstance(p, Player):", isinstance(p, Player))

# getattr(): Get an attribute value dynamically (at runtime!)
name_val = getattr(p, "name")
print("getattr(p, 'name'):", name_val)

# setattr(): Set an attribute value dynamically
setattr(p, "score", 100)
print("Newly Added Score:", p.score)

# hasattr(): Check if attribute exists
print("hasattr(p, 'score'):", hasattr(p, "score"))

# 2. Inspect module: Analyzing functions and classes
# Useful if you're building Frameworks or APIS
print("Function Source Code:", inspect.getsource(Player.say_hi))

# 3. Dynamic Type Creation (Advanced)
# type(name, bases, dict)
# This creates a class without the 'class' keyword!
DynamicClass = type("DynamicClass", (object,), {"x": 10})
obj = DynamicClass()
print("Object from DynamicClass:", obj.x)

# 4. Descriptors (Advanced Component of Class Properties)
# Use this when you want custom behavior for __get__ and __set__
class Constant:
    def __get__(self, instance, owner):
        return 42

class Science:
    pi = Constant()

s = Science()
print("Descriptor Value (pi):", s.pi)

# Summary Table
"""
| Function       | Purpose                                        |
|----------------|------------------------------------------------|
| type()         | Get class name or CREATE a class dynamicly    |
| dir()          | Show all available methods and attributes      |
| getattr()      | Access an attribute using a string name        |
| setattr()      | Change an attribute using a string name        |
| hasattr()      | Check if attribute exists using a string name   |
| callable()     | Check if object can be called (like function) |
"""
