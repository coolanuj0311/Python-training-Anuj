'''Number Types:

Integers (int): Whole numbers without decimals. Examples: 10, -5, 0.
Floating-point numbers (float): Numbers with decimals. Examples: 3.14, -2.5, 1.0.
Complex numbers (complex): Numbers with real and imaginary parts. Examples: 2 + 3j, -1 - 4j.

Creating Number Literals:

Integers: Simply type the number (e.g., 42).
Floating-point numbers: Use a decimal point (e.g., 3.14159).
Complex numbers: Use the j or J suffix for the imaginary part (e.g., 5 + 2j).

Basic Arithmetic Operations:

+ (addition)
- (subtraction)
* (multiplication)
/ (division)
// (floor division: discards the remainder)
% (modulo: returns the remainder)
** (exponentiation)

Built-in Functions:

abs(): Absolute value
round(): Rounding to a specified number of decimal places
int(): Converting to an integer (truncates decimals)
float(): Converting to a float
complex(): Creating a complex number
math module: Extensive mathematical functions (e.g., sin, cos, sqrt)

Type Conversions:

Python automatically converts between numbers when necessary.
Use explicit conversion functions for specific needs.

Important Considerations:

Number Precision: Floating-point numbers have limited precision, so be mindful of potential rounding errors in calculations.
Integer Division: In Python 2, integer division always truncates. Use // or convert to float for correct division.
Complex Numbers: Python fully supports complex numbers for advanced mathematical operations.

Additional Tips:

Use meaningful variable names to improve code readability.
Consider using comments to explain complex calculations.
Explore the math module for a wide range of mathematical functions.'''

x = 10  # Integer
y = 3.14  # Float
z = 2 + 5j  # Complex

result = x + y * z  # Mixed-type calculation
print(result)  # Output: (16.28+15.7j)

value1=100
print(type(value1))
print(isinstance(value1,int))
print(isinstance(value1,float))
print(isinstance(value1,complex))

value2=100.24
print(type(value2))
print(isinstance(value2,int))
print(isinstance(value2,float))
print(isinstance(value2,complex))

value3=50+6j
print(type(value3))
print(isinstance(value3,int))
print(isinstance(value3,float))
print(isinstance(value3,complex))

print(0b1101)
print(0xab)
print(0o23)

print(10+33.4)

print(int(10.5))
print(int(-20.99))
print(float(10))

data1=0.1+0.2
print(data1)
data1=1.20*2.50
print(data1)
from decimal import Decimal as D
print(D('0.1')+D('0.2'))
print(D('1.2')* D('2.5'))

from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))

import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.exp(10))
print(math.factorial(5))
print(math.sinh(10))
print(abs(-12.34))

import random
print('Random numbere -> ',random.randrange(5,15))
print('Random numbere -> ',random.randrange(5,15))
print('Random numbere -> ',random.randrange(5,15))
print('Random numbere -> ',random.randrange(5,15))

day=['Sun','Mon','Tue','Wed','Thu','Sat']
print(random.choice(day))
print(day)
random.shuffle(day)
print(day)
print(random.random())

