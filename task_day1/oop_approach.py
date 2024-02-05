'''Key Concepts:

Classes: Blueprints for creating objects with shared attributes (data) and methods (functions).
Objects: Instances of classes that represent real-world entities or abstract concepts.
Encapsulation: Bundling data and methods within a class, protecting data integrity and controlling access.
Inheritance: Deriving new classes (subclasses) from existing ones (base classes), reusing code and promoting hierarchy.
Polymorphism: Objects of different classes responding to the same method call in their own unique ways, enabling flexibility.

Main Advantages:

Modularity: Code is organized into reusable classes, promoting maintainability and code reusability.
Data Abstraction: Complex data structures and relationships are managed within classes, simplifying interaction.
Extensibility: Existing code can be easily extended through inheritance,
creating new functionality without modifying original code.
Maintainability: Changes to one class often don't affect others, reducing side effects and easing updates.

Basic Syntax:

class ClassName:
    def __init__(self, attribute1, attribute2):  # Constructor to initialize objects
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        # Code for method1

    def method2(self, parameter1):
        # Code for method2
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido", "Labrador")
my_dog.bark()  # Output: Woof!