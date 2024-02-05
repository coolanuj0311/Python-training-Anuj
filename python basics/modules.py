'''Modules in Python:

Self-contained units of code: They organize code, promote reusability, and make large projects more manageable.
Can contain functions, classes, variables, etc.: They group related elements together.
Can be imported and used in other Python files: This enables code sharing and collaboration.
Types of Modules:

Built-in Modules:

Come pre-installed with Python.
Offer essential functionality for various tasks.
Examples:
Math: Mathematical functions (e.g., sqrt, sin, cos)
Math module
Random: Random number generation (e.g., randint, choice)
Random module
Datetime: Handling dates and times
Datetime module
OS: Interacting with the operating system
JSON: Working with JSON data
And many more!

External Modules (Third-Party Libraries):

Created by the Python community and available through the Python Package Index (PyPI).
Expand Python's capabilities in various domains.
Installed using pip.
Examples:
NumPy: Numerical computations and array manipulation
NumPy module
Pandas: Data analysis and manipulation
Python Pandas module
Matplotlib: Data visualization
Python Matplotlib module
Requests: Making HTTP requests
Beautiful Soup: Web scraping
Django: Web development framework
TensorFlow: Machine learning
And countless others!
User-Defined Modules:

Created by you for specific project needs.
Organized as separate Python files with the .py extension.
Promote code reusability and maintainability.
Importing Modules:

Use the import statement:

import module_name

Access its elements using dot notation:

module_name.function_name()
module_name.variable_name
'''

import math

result = math.sqrt(16)  # Accessing the sqrt function from the math module
print(result)  # Output: 4.0

import math as m
print("the value of pi is",m.pi)


from math import pi
print("the value of pi is",pi)

from math import *
print("the value of pi is",pi)


''''# Decorators

Decorators
are
used
to
modify or enhance
the
behavior
of
functions or methods
without
changing
their
source
code.
'''
# Decorator for get request (@require_GET)

# Types of Decorators:

''''** Function
Decorators ** (Adding logging or timing functionality to a function)
** Class
Decorators ** (Applying a decorator to a


class that enhances the behavior of its methods)
** Method Decorators ** (Authenticating or authorizing access to a specific method within a class )
** Property Decorators ** (Adding validation logic to a class attribute)
** Parameterized Decorators ** (Passing configuration parameters to a decorator to customize its behavior)
** Multiple Decorators ** (You can apply multiple decorators to a single function or method, and they will be executed in the order they are applied.)'''


