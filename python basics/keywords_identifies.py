'''Keywords:

Reserved words with specific meanings in the language: They have predefined roles and cannot be used for user-defined names like variables or functions.
Examples: if, else, for, while, def, class, import, return, True, False, None, etc.
Case-sensitive: Most keywords are lowercase, except True, False, and None.

Identifiers:

Names given to variables, functions, classes, modules, etc.: They're used to identify and refer to these entities in your code.
Rules for naming identifiers:
Must start with a letter (A-Z or a-z) or an underscore (_).
Can contain letters, digits, and underscores.
Case-sensitive (e.g., myVariable is different from myvariable).
Cannot be a keyword.
Should be descriptive and meaningful.

Key Differences:

Function: Keywords define the language's syntax and structure, while identifiers are used for naming elements within your code.
Usage: Keywords are reserved and cannot be redefined, while identifiers can be created and assigned values.

Tips for Choosing Identifiers:

Use descriptive names: Make them meaningful and easy to understand.
Follow naming conventions: Python conventions (e.g., lowercase_with_underscores for variables and functions, CamelCase for classes) improve readability.
Avoid reserved keywords: Don't use keywords for your own names.
Be consistent: Use a consistent naming style throughout your code.

'''

# Keywords:
for i in range(10):  # `for` and `in` are keywords
    print(i)

# Identifiers:
my_variable = 5  # `my_variable` is an identifier
def my_function():  # `my_function` is an identifier
    pass

print(5==5)
print(5>5)

print(None==0)
print(None==False)
print(None==[])
print(None==None)

def a_void_function():
    a=1
    b=2
    c=a+b
x=a_void_function()
print(x)

print(True and False)
print(True or False)
print(not False)
print(True and True)
print(True or True)
print(not True)

import math as myMath
print(myMath.cos(myMath.pi))

assert 5>4
assert 5==5

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,8):
    if i==5:
        continue
    print(i)

class ExampleClass:
    def function1(parameters):
        print("function1() executing...")
    def function2(parameters):
        print("function2() executing...")
ob1=ExampleClass()
ob1.function1()
ob1.function2()

def function_name(parameters):
    pass
function_name(10)

a=10
print(a)

num=2
if num==1:
    print('one')
elif num==2:
    print('two')
else:
    print('Something else')

try:
    x=9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("division cannot be performed")
finally:
    print("execution successfully")

for i in range(1,10):
    print(i)

import math
from math import cos
print(cos(10))

globvar=10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar=5
def write2():
    globvar=15

read1()
write1()
read1()
write2()
read1()

a=[1,2,3,4]
print(4 in a)
print(4 not in a)

print(True is True)

a=lambda x:x*2
for i in range(1,6):
    print(a(i))

def outer_function():
    a=5
    def inner_function():
        nonlocal a
        a=10
        print("inner_function:",a)
    inner_function()
    print("Outer function:",a)
outer_function()

def function(args):
    pass
function(10)

def func_return():
    a=10
    return a
print(func_return())

i=5
while(i>0):
    print(i)
    i-=1

with open("my_file.txt","w") as file:
    file.write("hello world!")

def generator():
    for i in range(6):
        yield i*i
g=generator()
for i in g:
    print(i)



