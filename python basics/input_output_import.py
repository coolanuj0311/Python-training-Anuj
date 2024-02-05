'''Input:

input() function:
Takes user input from the keyboard.
Syntax: variable_name = input("Prompt for the user: ")
Example: name = input("Enter your name: ")
Always returns a string, even if the user enters a number.
Convert to other data types if needed: int(name), float(name)
Output:

print() function:
Displays output to the console or screen.
Syntax: print(value1, value2, ...)
Can print multiple values, separated by spaces by default.
Formatting options:
sep to change the separator: print(1, 2, 3, sep=",")
end to change the ending: print("Hello", end=" ")
Import:

import keyword:
Accesses code from external modules (libraries or files).
Syntax:
import module_name to import the entire module.
from module_name import specific_function to import a specific function.
Examples:
import math to use math functions like sqrt and sin.
from random import randint to use the randint function for random numbers.

'''

print('This sentence is output to the screen')
a=5
print("The value of a is",a)
print(1,2,3,4)
print(1,2,3,4,sep="*")
print(1,2,3,4,sep="#",end="&")
print()
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
x=input("Please enter any number:")
print(x)
y=int(input("please enter any number:"))
print(y)
print(x+str(y))
print(int(x)+y)
import math
print(math.pow(int(x),2))
