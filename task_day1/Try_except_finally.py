'''Exceptions:

Unexpected events that disrupt normal program flow.
Handled to prevent crashes and provide informative error messages.

try...except Block:

Encloses code that might raise exceptions.
If an exception occurs, execution jumps to the matching except block.
Structure:

try:
    # Code that might raise exceptions
except ExceptionType1:
    # Handle ExceptionType1
except ExceptionType2:
    # Handle ExceptionType2
    # ... (more except blocks for different exception types)
else:
    # Code to execute if no exception occurs
finally:
    # Code to execute always, regardless of exceptions
'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    with open("file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")



