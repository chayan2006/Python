# 🛠️ Itertools and Functools: Functional Power in Python

import itertools
import functools

# 1. Itertools: Mastering Iteration
# count(): Infinite sequence from a start number
counter = itertools.count(start=10, step=2)
print("count():", next(counter), next(counter)) # 10, 12

# cycle(): Repeats a sequence infinitely
# cycler = itertools.cycle(["A", "B", "C"])
# print(next(cycler), next(cycler), next(cycler), next(cycler)) # A, B, C, A

# repeat(): Repeats an object
repeater = itertools.repeat("Hello", times=3)
print("repeat():", list(repeater)) # ['Hello', 'Hello', 'Hello']

# combinations(): All possible combinations (order doesn't matter)
letters = ['A', 'B', 'C']
print("Combinations:", list(itertools.combinations(letters, 2))) # [('A','B'), ('A','C'), ('B','C')]

# permutations(): All possible arrangements (order matters)
print("Permutations:", list(itertools.permutations(letters, 2)))

# 2. Functools: Functions for Functions
# lru_cache: Caching results to speed up expensive functions (like Fibonacci)
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print("Cached Fib result:", fib(30))

# reduce(): Apply a function cumulatively to items (e.g. multiply all numbers)
nums = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, nums)
print("Reduce result (product):", product) # 24

# partial(): Create a new function with some arguments pre-filled
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
print("Partial result (square):", square(10)) # 100

# Summary Table
"""
| Module     | Key Tool      | Purpose                                       |
|------------|---------------|-----------------------------------------------|
| itertools  | count/cycle   | Handling infinite or complex iterators        |
| itertools  | combinations  | Finding all ways to pick items from a set     |
| functools  | lru_cache     | Storing results to prevent re-calculating     |
| functools  | partial       | Making shorter versions of existing functions |
"""
