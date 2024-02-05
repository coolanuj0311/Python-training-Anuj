'''functions
Functions are reusable blocks of code that perform specific tasks.
They improve code organization, readability, and maintainability.
Use functions to break down complex problems into smaller, manageable steps.
Choose appropriate parameter types, return values, and control flow within functions to achieve desired results.
Employ recursive functions for tasks that can be defined in terms of themselves.
Document functions with docstrings for clarity and understanding.'''

#1. Basic Function with Parameters and Return Value:

def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

greeting = greet("Anuj")
print(greeting)  # Output: Hello, Anuj!

#2. Function with Multiple Parameters and Conditional Logic:

def calculate_area(shape, length, width=None):
    """Calculates the area of a rectangle or triangle."""
    if shape == "rectangle":
        return length * width
    elif shape == "triangle":
        return 0.5 * length * width
    else:
        return "Invalid shape"

rectangle_area = calculate_area("rectangle", 5, 4)
triangle_area = calculate_area("triangle", 6, 8)
print(rectangle_area)  # Output: 20
print(triangle_area)  # Output: 24.0

#3. Function with Default Arguments:

def greet_user(name, greeting="Hello"):
    """Greets a user with a customizable greeting."""
    return f"{greeting}, {name}!"

print(greet_user("Anuj"))  # Output: Hello, Anuj!
print(greet_user("Anshika", "Hi"))  # Output: Hi, Anshika!


#4. Function with Variable-Length Arguments (varargs):

def sum_numbers(*numbers):
    """Sums an arbitrary number of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

#5. Function with Keyword Arguments:
def create_user(name, age, city="New York"):
    """Creates a user profile with optional city."""
    return {"name": name, "age": age, "city": city}

user1 = create_user("Anuj", 20)
user2 = create_user("Anshika", 15, city="London")
print(user1)  # Output: {'name': 'Anuj', 'age': 20, 'city': 'New York'}
print(user2)  # Output: {'name': 'Anshika', 'age': 15, 'city': 'London'}

#6. Recursive Function:

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120

def hello1():
    print("Hello! I love to code in Python.")
def hello2():
    """
    This is
    multiline
    text

    """
    return "Hello! I love to code in Python."
hello1()
print(hello2())
print(hello2.__doc__)

def myAddition(x,y):
    print("Performing the addition operation...")
    return(x+y)
def mySubtraction(x,y):
    print("Performing the subtraction operation...")
    return(x-y)
def myMultiplication(x,y):
    print("Performing the multiplication operation...")
    return(x*y)
def myDivision(x,y):
    print("Performing the division operation...")
    return(x/y)
def myMenu():
    print("Main Menu...")
    print("1 > Addition operation...")
    print("2 > Subtraction operation...")
    print("3 > Multiplication opeartion...")
    print("4 > Division operation...")
    ch=int(input("Please enter your option number..."))
    return ch
def calculation():
    ch=myMenu()
    num1=int(input("Please enter the first number..."))
    num2=int(input("Please enter the second number..."))
    if ch==1:
        result=myAddition(num1,num2)
    elif ch==2:
        result=mySubtraction(num1,num2)
    elif ch==3:
        result=myMultiplication(num1,num2)
    elif ch==4:
        result=myDivision(num1,num2)
    print("So result = ",result)
calculation()
























