'''Namespaces:

Accessing global variables within functions: Use the global keyword to modify global variables inside a function.
Avoiding global variables: Generally, favor local variables and function arguments for better code organization and maintainability.
Module-level scope: Names defined at the top level of a module are global within that module but not accessible directly in other modules.
Importing modules: Import names from other modules to use them in your code.
Namespaces and modules: Each module has its own namespace, preventing conflicts between modules with the same variable names.
Understanding namespaces and scope is crucial for writing clean, organized, and predictable Python code.

Scope:

Concept: The region of a program where a name can be accessed directly.
Scope Resolution: Python follows the LEGB rule to determine which namespace to use when accessing a name:
L: Local (innermost function)
E: Enclosing (outer functions)
G: Global (module)
B: Built-in
'''
x = 10  # Global variable

def my_function():
    x = 5  # Local variable, shadows the global x within the function
    print(x)  # Output: 5 (accesses local x)

print(x)  # Output: 10 (accesses global x)
my_function()  # Prints 5



a=2
print('id(2) =',id(2))
print('id(a) =',id(a))
a=a+1
print('id(a) =',id(a))
b=2
print('id(2) =',id(2))

def outer_function():
    global a
    a=20
    def inner_function():
        global a
        a=30
        print('a=',a)
    inner_function()
    print('a=',a)

a=10
print("a=",a)
outer_function()
print("a=",a)





