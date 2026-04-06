# ⚡ Concurrency in Python: Threads, Processes, and AsyncIO

# 1. Multithreading (Great for I/O bound tasks like downloading files)
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_letters():
    for char in "ABCDE":
        time.sleep(1)
        print(f"Thread 2: {char}")

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads (They run at the same time!)
# t1.start()
# t2.start()

# Wait for both to finish
# t1.join()
# t2.join()

# 2. Multiprocessing (Great for CPU bound tasks like heavy math)
# Bypasses the GIL (Global Interpreter Lock) to use multiple CPU cores
import multiprocessing

def square_numbers():
    for i in range(1000):
        _ = i * i

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    # p1.start()
    # p1.join()

# 3. AsyncIO (Modern way to handle thousands of tasks at once)
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1) # Non-blocking sleep
    print("...World!")

async def main():
    # Run multiple async tasks together
    await asyncio.gather(say_hello(), say_hello(), say_hello())

# To run: asyncio.run(main())

# Summary Table
"""
| Concept          | Best Case                                    | Key Module      |
|------------------|----------------------------------------------|-----------------|
| Multithreading   | Waiting for I/O (API calls, file saving)     | `threading`     |
| Multiprocessing  | Heavy Math / Data Processing                 | `multiprocessing`|
| AsyncIO          | High-concurrency network apps (FastAPI/Web) | `asyncio`       |
"""
