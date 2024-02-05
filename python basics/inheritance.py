'''What is Inheritance?

It's a fundamental concept in object-oriented programming (OOP) that allows you to create new classes (subclasses) that inherit properties and methods from existing classes (base classes).
It promotes code reusability, organization, and hierarchical relationships between classes.
Key Terms:

Base Class (Parent Class, Superclass): The class that provides the features to be inherited.
Subclass (Child Class, Derived Class): The class that inherits from the base class.
How to Use Inheritance in Python:

Specify the Base Class:

class Subclass(BaseClass):
    # ...

Inherited Features:

The subclass automatically inherits all attributes and methods from the base class, except for the constructor (__init__) and private methods/attributes (prefixed with __).
Overriding Methods:

You can redefine inherited methods in the subclass to provide specialized behavior:

class Subclass(BaseClass):
    def method_name(self, *args, **kwargs):
        # New implementation

Calling the Base Class Method:

Use super() to call the base class method from within the overridden method:
Python
class Subclass(BaseClass):
    def method_name(self, *args, **kwargs):
        super().method_name(*args, **kwargs)  # Call the base class method


Types of Inheritance:

Single Inheritance: A subclass inherits from a single base class.
Multiple Inheritance: A subclass inherits from multiple base classes (use with caution due to potential complexity).
Multilevel Inheritance: A chain of inheritance where a subclass inherits from a class that itself inherits from another class.
Hierarchical Inheritance: Multiple subclasses inherit from a single base class.

Benefits of Inheritance:

Code Reusability: Avoids redundant code by sharing common features among classes.
Organization: Creates a logical structure for classes, making code easier to understand and maintain.
Extensibility: Allows you to create specialized classes without modifying existing code.
Real-World Modeling: Represents "is-a" relationships between objects effectively.

Remember: Use inheritance wisely to maintain code clarity and avoid unnecessary complexity. Consider composition (using objects as attributes) as an alternative when appropriate.


'''
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")


class myBird:
    def __init__(self):
        print("myBird class constructor is executing...")
    def whatType(self):
        print("I am a Bird...")
    def canSwim(self):
        print("I can Swim...")

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("myPenguin class constructor is executing...")
    def whoisThis(self):
        print("I am penguin...")
    def canRun(self):
        print("I can run faster...")
pg1=myPenguin()
pg1.whatType()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()

class MyParrot:
    def canFly(self):
        print("Parrot can fly...")
    def canSwim(self):
        print("Parrot can't swim...")
class MyPenguin:
    def canFly(self):
        print("penguin can't fly...")
    def canSwim(self):
        print("penguin can swim...")
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()
bird_parrot=MyParrot()
bird_penguin=MyPenguin()
flying_bird_test(bird_parrot)
print()
flying_bird_test(bird_penguin)