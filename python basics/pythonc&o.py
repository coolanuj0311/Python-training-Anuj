'''Here's a comprehensive explanation of Python classes and objects:

Classes:

Blueprints for creating objects: A class defines the structure and behavior of a particular type of object. It's like a template or a recipe that outlines what properties (data) and actions (methods) objects of that type will have.
Defined using the class keyword: 

Here's the basic syntax:
class ClassName:
    # Class body (attributes and methods)

Objects:

Instances of a class: An object is a concrete instantiation of a class. It's an individual entity that has its own state (values for its attributes) and can perform actions defined by the class's methods.
Created using the class name followed by parentheses:
object_name = ClassName()

Key Concepts:

Attributes:

Data associated with an object.
Represented by variables within the class.
Can be of different types (int, string, list, etc.).
Defined either at the class level (shared by all instances) or within the __init__() method (specific to each instance).

Methods:

Functions defined within a class that operate on its objects.
Represent the actions that objects of that class can perform.
Defined using the def keyword inside the class body.
Automatically take the object itself as the first argument (self).

__init__() Method:

Special method called the constructor.
Executed automatically when a new object is created.
Used to initialize the object's attributes (set their initial values).

Benefits of Using Classes and Objects:

Organization and Encapsulation: Classes group related data and code together, making code more modular and maintainable.
Reusability: Classes can be reused to create multiple objects with similar properties and behaviors.
Abstraction: Classes hide implementation details and provide a clear interface for interacting with objects.
Modeling Real-World Concepts: Classes are well-suited for modeling real-world entities and relationships in code, making code more intuitive and relatable.

'''

class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance attributes
        self.breed = breed

    def bark(self):
        print("Woof!")  # Method

# Create two dog objects
dog1 = Dog("Fido", "Labrador")
dog2 = Dog("Buddy", "Golden Retriever")

# Access attributes
print(dog1.name)  # Output: Fido
print(dog2.breed)  # Output: Golden Retriever

# Call methods
dog1.bark()  # Output: Woof!


class MyComplexNumber:
    def __init__(self,real=0,imag=0):
        print("MyComplexNumber constructor executing")
        self.real=real
        self.imag=imag
    def displayComplex(self):
        print("{0}+{1}j".format(self.real,self.imag))
cmp1x1=MyComplexNumber(40,50)
cmp1x1.displayComplex()
cmp1x2=MyComplexNumber(60,70)
cmp1x2.displayComplex()
cmp1x2.new_attribute=80
print((cmp1x2.real,cmp1x2.imag,cmp1x2.new_attribute))




