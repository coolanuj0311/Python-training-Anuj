'''The ability to redefine how operators work with custom objects.
Provides a natural and intuitive way to interact with user-defined objects.
Achieved through special methods (dunder methods) within classes.

Arithmetic operators:
__add__(self, other): Addition (+)
__sub__(self, other): Subtraction (-)
__mul__(self, other): Multiplication (*)
__truediv__(self, other): True division (/)
__floordiv__(self, other): Floor division (//)
__mod__(self, other): Modulo (%)
__pow__(self, other): Exponentiation (**)
Comparison operators:
__lt__(self, other): Less than (<)
__le__(self, other): Less than or equal to (<=)
__eq__(self, other): Equality (==)
__ne__(self, other): Inequality (!=)
__gt__(self, other): Greater than (>)
__ge__(self, other): Greater than or equal to (>=)
Other operators:
__len__(self): Length using len() function
__getitem__(self, key): Indexing using []
__setitem__(self, key, value): Assignment using []
__contains__(self, item): Membership testing using in
And many more...
Benefits:

Intuitive syntax for custom objects
Consistent behavior with built-in types
Enhances code readability and maintainability

Best Practices:

Use operator overloading judiciously to avoid confusion.
Ensure the overloaded behavior is consistent with the expected semantics of the operator.
Consider alternative approaches (e.g., explicit methods) if overloading might lead to ambiguity.
'''

class myPoint:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return myPoint(x,y)
    def __lt__(self,other):
        self_mag=(self.x**2)+(self.y**2)
        other_mag=(other.x**2)+(other.y**2)
        return self_mag<other_mag
p1=myPoint(1,2)
p2=myPoint(4,5)
print(p1)
print(p2)
print()
print(p1<p2)
print(p1+p2)
print()
print(p1.__lt__(p2))
print(p1.__add__(p2))