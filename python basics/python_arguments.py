'''What are Function Arguments?

They are values that are passed to a function when it's called.
They provide a way to customize the function's behavior based on different inputs.

Types of Function Arguments:

Positional Arguments:

Passed in a specific order, matching their definition in the function.
Example: def greet(name, greeting): print(greeting, name)
Call: greet("Anuj", "Hello")
Keyword Arguments:

Passed by name, allowing for flexibility in order.
Example: greet(name="Anshika", greeting="Hi")
Default Arguments:

Have a default value if not provided during the call.
Example:
Arbitrary Arguments:

Accept any number of arguments using *args (positional) and **kwargs (keyword).

Accessing Arguments:

Inside the function, use the argument names to access their values.
Best Practices:

Use clear and meaningful argument names.
Provide default values when appropriate.
Handle errors gracefully if invalid arguments are passed.
Consider using type hints for better code readability and maintainability.

Key Points:

Choose the appropriate argument types for your functions based on their needs.
Use positional arguments for required values and keyword arguments for optional ones.
Default arguments provide flexibility and make functions more adaptable.
Arbitrary arguments allow for a variable number of inputs.'''

def sum_all(*numbers):
    return sum(numbers)
sum_all(1,2,3,4)
def greet(name, greeting="Hello"):
    print(greeting, name + "!")

greet("Anuj")  # Uses default greeting
greet("Anshika", "Hi")  # Uses specified greeting

def calculate_area(length, width=10):
    return length * width
calculate_area(5)

def findMax(a,b):
    if a>b:
        return a
    else:
        return b
print("Max number between 10 and 20 is",findMax(10,20))

def hello(name,msg=",how are you?"):
    print("Hello",name,msg)
hello("Anuj",",have a nice day.")
hello("Anuj")

def sumAll(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("Sum of alll the integers between 1-5 is",sumAll(1,2,3,4,5))

def defaultArg(a=100,b=200,c=300):
    print("a={},b={},c={}".format(a,b,c))
defaultArg(10,20,30)
defaultArg(10,20)
defaultArg(10)
defaultArg()
defaultArg(b=222,c=333,a=111)