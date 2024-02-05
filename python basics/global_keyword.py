'''Purpose:

Allows you to modify a global variable from within a function.
Without global, a variable created or assigned within a function is considered local by default.

Syntax:
global variable_name

Placement:
Used within a function, before any assignments to the global variable.

Key Points:

Read without global: You can read a global variable's value within a function without global, but you cannot modify it.
Creating new global variables: Using global inside a function to create a new variable actually creates it in the global namespace, even if it's not yet defined outside the function.
Best practices:
Use global variables sparingly, as they can make code harder to understand and maintain.
Prefer passing variables as function arguments or using function returns for better encapsulation.
If global variables are necessary, consider using a separate module to hold them for better organization.

Cautions:

Overuse: Excessive use of global variables can lead to:
Unintended side effects: Changes in one part of the code can unexpectedly affect other parts.
Debugging challenges: It can be harder to track the flow of data and identify the source of errors.
Testing difficulties: Isolating and testing individual functions becomes more complex.
Conclusion:

Use the global keyword when necessary, but prioritize local variables and function arguments for better code structure and maintainability.'''
x = 10  # Global variable

def my_function():
    global x  # Declare x as global
    x = 20    # Modify the global x

print(x)  # Output: 10 (before calling the function)
my_function()
print(x)  # Output: 20 (after calling the function, global x is modified)

def funct1():
    x=20
    def funct2():
        global x
        x=25
    print("Before calling funct2:",x)
    print("Calling funct2 now")
    funct2()
    print("After calling funct2:",x)
funct1()
print("x in main:",x)