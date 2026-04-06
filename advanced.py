# 🚀 Advanced Python Concepts

# 1. List Comprehensions (Compact syntax)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
squares = [x**2 for x in range(1, 6)]
print("Even numbers:", evens)
print("Square numbers:", squares)

# 2. Dictionary Comprehensions
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print("Dictionary comprehension:", name_lengths)

# 3. Generators (Memory efficient iteration)
# yield returns values one at a time, instead of storing a whole list 
def count_down(n):
    while n > 0:
        yield n # Returns value and pauses function
        n -= 1

counter = count_down(5)
print(next(counter)) # 5
for x in counter:
    print(f"Countdown: {x}") # 4, 3, 2, 1

# 4. Decorators (Functions that modify other functions)
def log_decorator(func):
    def wrapper():
        print("Before function execution...")
        func()
        print("After function execution...")
    return wrapper

@log_decorator
def greet_world():
    print("HELLO WORLD!")

greet_world()

# 5. Iterators (Custom iteration logic)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

my_iter = iter(MyNumbers())
for x in my_iter:
    print("Iterator value:", x)

# 6. Collections Module (Built-in high-performance containers)
from collections import Counter, defaultdict, namedtuple

# Counter: Count item frequency
my_list = ["apple", "apple", "banana", "cherry", "banana"]
counts = Counter(my_list)
print("Counter:", counts) # {'apple': 2, 'banana': 2, 'cherry': 1}

# defaultdict: Handles missing keys automatically
d = defaultdict(int) 
d["missing_key"] += 1
print("DefaultDict:", d)

# namedtuple: Readable tuples (like objects but faster)
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"NamedTuple: x={p.x}, y={p.y}")

# 7. Unit Testing (Built-in testing)
import unittest

def add(a, b): return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# To run tests: unittest.main()

# Summary Table

"""
| Concept             | Use Case                                                    |
|---------------------|-------------------------------------------------------------|
| Comprehensions      | Create new list/dict in one line                            |
| Generators (yield)  | Loop through huge data without using all RAM                |
| Decorators (@)      | Add features to functions without changing their code        |
| Iterators           | Define custom behavior for 'for i in obj' loops             |
| Collections         | Advanced list/dict types for better performance/readability |
"""
