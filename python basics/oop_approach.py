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

class myBird:
    def __init__(self):
        print("myBird class constructor is executing...")
    def whatType(self):
        print("I am a Bird...")
    def canSwim(self):
        print("I can Swim...")
class myParrot:
    species="bird"
    def __init__(self,name,age):
        print("myParrot class constructor is executing")
        self.name=name
        self.age=age
    def canSing(self,thisSong):
        return "{} can sing {}...".format(self.name,thisSong)

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("I am penguin")
    def canRun(self):
        print("I can run faster")
mp1=myParrot("MyParrot1",10)
mp2=myParrot("MyParrot2",15)
print("MP1 is a {}".format(mp1.__class__.species))
print("MP2 is also a {}".format(mp2.__class__.species))
print("{} is {} yaears of age".format(mp1.name,mp1.age))
print("{} is {} years of age".format(mp2.name,mp2.age))
print(mp1.canSing("Chirp"))
pg1=myPenguin()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()\

class personalComputer:
    def __init__(self):
        self.maxComputerPrice=20000
    def mySell(self):
        print("Selling Price:{}".format(self.maxComputerPrice))
    def setMaxComputerPrice(self,price):
        self.maxComputerPrice=price
pc=personalComputer()
pc.mySell()
pc.maxComputerPrice=30000
pc.mySell()
pc.setMaxComputerPrice(40000)
pc.mySell()