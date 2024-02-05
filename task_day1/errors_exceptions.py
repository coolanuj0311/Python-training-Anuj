'''Errors vs. Exceptions:

Errors are problems that prevent the program from running at all, usually due to syntax mistakes or resource issues.
Exceptions are unexpected events that occur during execution, interrupting the normal flow of the program.
They can be handled to prevent crashes.
Types of Exceptions:

Built-in Exceptions: Python provides several built-in exceptions to handle common errors:
ZeroDivisionError: Dividing by zero
NameError: Using an undefined variable
TypeError: Performing operations on incompatible types
ValueError: Passing invalid arguments to functions
IndexError: Accessing a list or string index out of range
KeyError: Trying to access a missing key in a dictionary
IOError: Errors related to file input/output
OSError: Errors related to the operating system
And more...
Handling Exceptions:

Use try...except blocks to catch and handle exceptions:
try:
    # Code that might raise an exception
except ExceptionType1:
    # Handle ExceptionType1
except ExceptionType2:
    # Handle ExceptionType2
else:
    # Code to execute if no exception occurs
finally:
    # Code to execute always, regardless of exceptions

if condition:
    raise ValueError("Invalid input")'''