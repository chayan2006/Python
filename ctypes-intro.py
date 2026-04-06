# 🚀 Calling C from Python: Using ctypes and Shared Libraries

import ctypes
import os

# 1. Why use ctypes?
# To call fast C code from your Python script without rewriting EVERYTHING.
# Python can LOAD compiled (.dll, .so) libraries!

# 🚀 Concept: Python script -> Ctypes -> C Library (.dll/.so)

# 2. Loading the Standard C Library
if os.name == "nt": # Windows
    libc = ctypes.cdll.msvcrt
else: # Linux/Mac
    libc = ctypes.CDLL("libc.so.6")

# 3. Calling C functions (Example: printf)
# (Warning: This will print directly to the console buffer!)
libc.printf(b"Hello from C! Number: %d\n", 100)

# 4. C Data Types (Mandatory!)
# Python's '10' is not the same as a C 'int' (C integers have fixed sizes).
# Ctypes provides helpers to convert them:
c_int_val = ctypes.c_int(123)
c_float_val = ctypes.c_float(1.23)
c_str_val = ctypes.c_char_p(b"Hello C!")

# 5. Writing and using your own C code?
# 1. Write 'my_math.c'
# 2. Compile it: gcc -shared -o my_math.dll my_math.c
# 3. Load it: my_lib = ctypes.CDLL("./my_math.dll")

# Summary Table
"""
| Ctypes Helper  | Equivalent C Type                     |
|----------------|---------------------------------------|
| c_int          | int                                   |
| c_char_p       | char * (String)                       |
| c_float        | float                                 |
| c_double       | double                                |
| c_void_p       | void * (Generic pointer)              |
| POINTER()      | Used to pass data by reference (&x)  |
"""
