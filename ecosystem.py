# 🐍 Python Ecosystem: Virtual Environments & Package Management

# 1. Why do we need Virtual Environments?
# It isolates project-specific dependencies from your global system.
# This prevents version conflicts between projects!

# 🚀 Terminal Commands to Create and Use venv (Windows):
# 1. Create: python -m venv venv 
# 2. Activate: venv\Scripts\activate 
# 3. Deactivate: deactivate 

# 2. Using PIP (The Python Package Index)
# pip install package_name
# pip install django==4.0 (specific version)
# pip uninstall package_name
# pip list (shows all installed packages)

# 3. Sharing Your Project Dependencies
# Always create a requirements.txt file so others can run your code!
# Save: pip freeze > requirements.txt 
# Install from: pip install -r requirements.txt 

# 4. Standard Coding Conventions (PEP 8)
"""
| Concept             | Standard                             | Example                             |
|---------------------|--------------------------------------|-------------------------------------|
| variables/functions | snake_case                           | my_variable = 10                    |
| classes             | PascalCase                           | MyClass:                            |
| constants           | ALL_CAPS                             | PI = 3.14                           |
| indentation         | EXACTLY 4 spaces (NOT Tabs!)         |                                     |
| docstrings          | Triple-quoted comments under funcs  | def foo(): \n    \"\"\"This does bar\"\"\" |
"""

# 5. Type Hinting (Modern Python)
# Makes your code more readable for you and other developers!
def add_numbers(x: int, y: int) -> int:
    return x + y

# Summary Table
"""
| Module/Tool | Purpose                                         |
|-------------|-------------------------------------------------|
| venv        | Keeps project dependencies isolated             |
| pip         | Downloads and installs code from pypi.org       |
| PEP 8       | The official style guide for Python code        |
| docstrings  | Built-in documentation for classes and functions|
"""
