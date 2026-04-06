# 🚀 Abstract Syntax Trees (AST): Analyzing Code as Data

import ast

# 1. Why use AST?
# Because Python can actually read its own code as a tree structure!
# This is how formatters (Black), Linters (Flake8), and IDEs work!

# 🚀 Concept: Code -> AST Tree -> Compiled Bytecode

# 2. Parsing a String into a Tree
code_str = "x = 1 + 2"
tree = ast.parse(code_str)

# 3. Walking through the Tree (Visit all nodes)
# This will print the node types (Assign, Name, Constant, BinOp, etc.)
for node in ast.walk(tree):
    print(f"Node Type: {type(node).__name__}")

# 4. Modifying Code with AST (Advanced!)
# Let's write a simple visitor to count variables
class VarCounter(ast.NodeVisitor):
    def __init__(self):
        self.count = 0
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.count += 1
        self.generic_visit(node)

# Example:
my_script = "a = 10; b = 20; c = a + b"
v = VarCounter()
v.visit(ast.parse(my_script))
print(f"Number of variables defined: {v.count}")

# 5. Safety: Evaluating math safely
# ast.literal_eval() is MUCH safer than eval()
safe_res = ast.literal_eval("{'a': 1, 'b': 2}")
print("Safely Evaluated Dict:", safe_res)

# Summary Table
"""
| Method         | Purpose                                        |
|----------------|------------------------------------------------|
| ast.parse()    | Convert Python source string to a Tree Object  |
| ast.walk()     | Iterate through EVERY part of the code         |
| ast.NodeVisitor| Pattern for reading through code structures     |
| ast.NodeTransformer| Pattern for CHANGING code structures       |
| ast.literal_eval()| SAFELY turn strings into Python Dicts/Lists |
"""
