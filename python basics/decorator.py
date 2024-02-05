'''What are decorators?

A design pattern that allows you to dynamically modify the behavior of a function or method without directly changing its source code.
They achieve this by wrapping the original function with another function that adds extra functionality.
How do decorators work?

Defining a decorator: A decorator is a function that takes another function as an argument and returns a modified function.
Applying a decorator: Decorators are typically applied using the @ symbol syntax before a function definition.
Wrapping the original function: When a function is decorated, the decorator function is called with the original function as an argument. The decorator then returns a new function (the wrapper) that will be called instead of the original function.
Executing the wrapper: When you call the decorated function, you're actually calling the wrapper function created by the decorator. The wrapper can perform additional tasks before or after calling the original function.
'''
'''def make_decorated(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function()
@make_decorated
def simple_func():
    print("I am a simple function")
decor=make_decorated(simple_func)
decor()
'''
def my_smart_div(func):
    def inner_func(x,y):
        print("I am dividing ",x," and ",y)
        if y==0:
            print("Oops division by zero is illegal...!!!")
            return
        return func(x,y)
    return inner_func
@my_smart_div
def go_divide(a,b):
    return a/b
print(go_divide(20,2))
print(go_divide(20,0))
