'''What is Data Type Conversion?

It's the process of transforming a value from one data type (e.g., integer, string, float) to another.
Python often handles this implicitly, but you can also perform explicit conversions for more control.
Types of Data Type Conversion:

Implicit Conversion (Automatic):

Python performs this automatically when a value is used in a context that requires a different data type.
Examples:
Adding a string and a number: result = "5" + 3 # Output: "53" (string concatenation)
Comparing a number and a string: if 5 > "2": print("True") (number converted to string)
Explicit Conversion (Type Casting):

This involves using built-in functions to purposefully convert a value to a specific data type.
Common functions:
int(): Converts to integer
float(): Converts to floating-point number
str(): Converts to string
bool(): Converts to boolean (True or False)
list(): Converts to list
tuple(): Converts to tuple
'''

num_int=123
num_flo=1.23
num_new=num_int+num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

num_int=123
num_str="456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str before type casting",type(num_str))
num_str=int(num_str)
print("Data type of num_str after type casting",type(num_str))

num_sum=num_int+num_str
print("Sum of num_int and num_str:",num_sum)
print("Data types of the sum:",type(num_sum))
