'''What is Multiple Inheritance?

It allows a subclass to inherit from multiple base classes, combining their features.
It offers flexibility but can introduce complexity if not handled carefully.

Syntax:

class Subclass(BaseClass1, BaseClass2):
    # ...

Key Points:

Inheritance Order: The subclass inherits attributes and methods from base classes in the order they are specified in the parentheses.
Method Resolution Order (MRO): Python uses a specific algorithm (C3 linearization) to determine the order in which methods are searched for and resolved. You can view the MRO using Subclass.__mro__.
Constructor (__init__): Constructors of all base classes are called in MRO order when a subclass instance is created. Use super() to control this process.

Challenges and Best Practices:

Diamond Problem: Occurs when two base classes inherit from a common ancestor, leading to potential ambiguity in method calls. Python's MRO resolves this, but it's important to be aware of it.
Overridden Method Resolution: Understand how MRO determines which overridden method is called.
Use with Caution: Prefer single inheritance or composition when possible to avoid complexity.
Clear Hierarchy: Design a clear and logical inheritance structure to prevent confusion.
Thorough Testing: Test code extensively to ensure correct behavior.

Alternatives:

Composition: Instead of inheriting from multiple classes, create objects as attributes to achieve modularity and avoid complex inheritance hierarchies.
Mixins: Provide reusable functionality without creating full-fledged base classes.
Remember: Use multiple inheritance judiciously and consider alternatives when appropriate to maintain code clarity and avoid potential issues.

'''
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def breathe(self):
        print("Breathing")

class Bird(Animal):
    def fly(self):
        print("Flying")

class Bat(Mammal, Bird):  # Multiple inheritance
    def echolocate(self):
        print("Echolocating")

class Base1:
    pass
class Base2:
    pass
class MUltiDerived(Base1,Base2):
    pass

class Base1:
    def funBase1(self):
        print("funcBase1() is execting...")
class Base2:
    def funBase2(self):
        print("funcBase2() is execting...")
class Base3:
    def funBase3(self):
        print("funcBase3() is execting...")
class MutiDerived(Base1,Base2,Base3):
    def funcMutiDerived(self):
        print("funcMutiDerived() is executing")
md1=MutiDerived()
md1.funBase1()
md1.funBase2()
md1.funBase3()
md1.funcMutiDerived()
