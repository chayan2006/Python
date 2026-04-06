# 🔒 Custom Context Managers: Creating Your Own 'with' Statements

from contextlib import contextmanager

# 1. Why use Context Managers?
# To ensure resources (Files, Databases, Sockets) are properly CLOSED
# or CLEANED UP even if an error occurs!

# 🚀 Method 1: Class-based (Best for complex logic)
class MyFileOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print(f"Opening {self.filename}...")
        self.file = open(self.filename, self.mode)
        return self.file # Result of 'as' in 'with ... as f'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}...")
        self.file.close()
        # Returns True to suppress errors, False to let them through!

# Using it:
with MyFileOpen("test_ctx.txt", "w") as f:
    f.write("Hello from custom context manager!")

# 🚀 Method 2: Generator-based (Shorter, easier for simple logic!)
@contextmanager
def simple_timer():
    import time
    start = time.time()
    try:
        # Code inside 'with' happens here:
        yield 
    finally:
        # Cleanup happens after 'with' block:
        end = time.time()
        print(f"Time Taken: {end - start:.5f}s")

# Using it:
with simple_timer():
    # Simulate work
    import time
    time.sleep(0.5)

# Summary Table
"""
| Method         | Function                                       |
|----------------|------------------------------------------------|
| __enter__()    | Code to run at start of 'with' block          |
| __exit__()     | Code to run at end of 'with' block            |
| @contextmanager| Simple generator-based manager                 |
| yield          | Divider between setup and cleanup code         |
| finally        | Ensures cleanup even if code crashes!          |
"""
