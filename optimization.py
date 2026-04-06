# 🚀 Code Optimization and Profiling: Performance in Python

import timeit
import cProfile

# 1. Timeit Module: Measuring Function Performance
# Use this when you want to measure execution speed (like milleseconds)
# Example: Comparing List vs Generator comprehension
setup = "nums = range(1000)"
list_comp = "list_res = [x**2 for x in nums]"
gen_comp = "gen_res = (x**2 for x in nums)"

list_time = timeit.timeit(list_comp, setup=setup, number=10000)
gen_time = timeit.timeit(gen_comp, setup=setup, number=10000)

print(f"List comprehension time: {list_time:.5f}s")
print(f"Generator comprehension time: {gen_time:.5f}s") 
# Generators are almost ALWAYS faster for creation!

# 2. Memory Optimization (Slots)
# By default, Python uses a dictionary to store instance attributes (__dict__)
# '__slots__' forces a fixed set of attributes, saving HUGE memory!
class Point:
    __slots__ = ("x", "y") # Attributes MUST be pre-declared 
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# p.z = 10 # This would cause an AttributeError (z is not pre-declared)

# 3. Profiling: Finding "Where" your code is slow
# cProfile.run('my_function()') 
# It tells you how many calls each function took and the total time!

# 4. Lazy Evaluation (Generators)
# Always use yield or generator expressions for HUGE datasets!
# Already covered in advanced.py, but essential for optimization!

# Summary Table
"""
| Tool        | Best Case                                         |
|-------------|---------------------------------------------------|
| timeit      | Benchmarking small pieces of code                 |
| cProfile    | Finding bottlenecks in huge applications           |
| __slots__   | Restricting attribute names for memory efficiency |
| generator   | Loop through data without using excessive RAM      |
| map/filter  | Functional way to process items (sometimes faster) |
"""
