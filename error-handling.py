# ⚠️ Error and Exception Handling in Python

# Errors are two types: 
# 1. Syntax Errors (Structure is wrong)
# 2. Exceptions (Something wrong during execution)

# The try...except...finally Block
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    # If number is zero
    print("Cannot divide by zero!")
except ValueError:
    # If the user enters a string instead of a number
    print("Invalid input! Please enter a numeric value.")
except Exception as e:
    # Catch-all for any other errors
    print(f"Something went wrong: {e}")
else:
    # Runs ONLY if NO error occurred
    print("Execution successful!")
finally:
    # Runs ALWAYS, no matter what (used for cleanup)
    print("Moving on...")

# Raising Exceptions manually
def withdraw_money(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    withdraw_money(100, 50)
except ValueError as error:
    print(error)

# Custom Exceptions
class CustomError(Exception):
    # This inherits the default Exception class
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Using our Custom Exception
# raise CustomError("This is a manual custom error")

# Summary of Exception Keywords
"""
| Keyword | Purpose                                                              |
|---------|----------------------------------------------------------------------|
| try     | Block of code where you expect an error could happen                 |
| except  | Block of code that handles the error if it happens                   |
| else    | Block of code that runs if no error happens at all                   |
| finally | Always runs (used for closing files or databases)                    |
| raise   | Used to trigger an error on purpose                                  |
| assert  | Checks for a condition; if False, raises an AssertionError          |
"""
