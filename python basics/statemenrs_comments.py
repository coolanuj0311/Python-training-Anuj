'''Statements

Building blocks of Python code: They represent individual instructions that the Python interpreter executes to perform actions.
Types of statements:
Assignment statements: Assign values to variables (x = 5, name = "Alice").
Expression statements: Evaluate expressions and discard the results (print("Hello, world!")).
Control flow statements: Control the execution flow of the code (if, for, while).
Function calls: Invoke functions to perform specific tasks (result = calculate_area(length, width)).
Import statements: Import modules to access their functionality (import math).
Class definitions: Create new classes (class Person:).

Comments

Non-executable text added to code for clarity: They are ignored by the interpreter and serve to explain code logic, purpose, or notes for developers.
Use comments to explain complex logic or non-obvious code sections.
Comment on the purpose of functions and variables, especially those with non-descriptive names.
Add comments to highlight important sections or potential pitfalls.
Keep comments concise and to the point.
Avoid overly commenting on self-explanatory code.
Update comments when code changes to maintain accuracy.

'''

"""
Multi-line comments 
can also be written like this
"""
a=1
b=1+2+3+\
    4+5+6
print(b)
c=(1+2+3+
   4+5+6)
print(c)
d=1;e=3;f=0
print(d,e,f)
for i in range(1,10):
    print(i)
    if i==5:
        break
print("End of the program...")