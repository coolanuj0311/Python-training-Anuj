'''  Conditional Statements:

if statements: Execute code blocks based on conditions (e.g., if age >= 18: print("You are an adult")).
else statements: Provide alternative code execution.
elif statements: Chain multiple conditions. 

Remember:


Indentation is crucial in Python to define code blocks within conditional statements.
Choose appropriate logical operators (and, or, not) for combining conditions.
Use conditional statements to control the flow of your code based on different scenarios.
'''

#simple if else
age = 25
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not old enough to vote.")

#Multiple conditions with elif:

grade = 85
if grade >= 90:
    print("Excellent!")
elif grade >= 80:
    print("Very good!")
elif grade >= 70:
    print("Good.")
else:
    print("Needs improvement.")

# Nesting if statements:
has_ticket = True
is_vip = False

if has_ticket:
    print("You can enter the event.")
    if is_vip:
        print("You have access to the VIP lounge.")
    else:
        print("Enjoy the regular seating.")
else:
    print("You need a ticket to enter.")

#Checking for equality:

name = "Anuj"
if name == "Anuj":
    print("Hello, Anuj!")

#Checking for inequality:

temperature = 25
if temperature != 30:
    print("It's not exactly 30 degrees today.")

#Checking for multiple conditions:
age=25
country="USA"
if age >= 18 and country == "USA":
    print("You are eligible to vote in the USA.")

#Checking for any condition to be true:

if age >= 18 or has_parental_consent:
    print("You can watch this movie.")

#Using conditional statements within functions:

def greet(name):
    if name:
        print("Hello, " + name + "!")
    else:
        print("Hello, there!")

greet("Anuj")  # Output: Hello, Anuj!
greet("")    # Output: Hello, there!
