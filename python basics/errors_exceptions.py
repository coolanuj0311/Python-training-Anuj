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

try:
    """
    the code which can give rise to an exception is written here
    """
    a="hi"
    b=int(a)
except:
    print("Exception caught!")

try:
    a=5
    b=0
    c=a/b
except ZeroDivisionError:
    print("Division by zero is not possible")

try:
    raise TypeError
except TypeError:
    print("Type Error Exception caught!")

try:
    print("In try block")
    raise TypeError
except:
    print("in except block")
finally:
    print("In the finally block")

try:
    a=int(input("Please enter the first number..."))
    b=int(input("Please enter the second number..."))
    if(a<0):
        raise TypeError
    c=x/y
    print("{} / {} = {}".format(a,b,c))
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("The data types are not proper")
except TypeError:
    print("The data is not in range")
except NameError:
    print("The data items are not defined")

