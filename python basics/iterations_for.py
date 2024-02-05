'''Purpose:

Executes a block of code repeatedly for each item in a sequence (list, tuple, string, etc.).
Essential for tasks involving repeated actions on multiple elements.
Syntax:

for item in sequence:
    # Code to be executed for each item

Breakdown:

for keyword: Initiates the loop.
item variable: Holds the current item in each iteration.
in keyword: Specifies the sequence to iterate over.
sequence: The collection of items to be processed (e.g., list, tuple, string).
Indented block: Contains the code to be executed for each item.

Additional Features:

break statement: Immediately exits the loop.
continue statement: Skips the current iteration and moves to the next.
else clause: Executes code after the loop completes normally (not with break).
Iterating over dictionaries: Use keys(), values(), or items() methods.
Nested loops: Loops within loops for complex iterations.

Key Points:

Choose meaningful variable names for readability.
Use indentation properly to define the loop's body.
Consider using enumerate() to get both index and item in each iteration.
Master for loops for efficient data processing and automation in Python.'''

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, orange (each on a new line)
word = "hello"
for letter in word:
    print(letter)  # Output: h, e, l, l, o (each on a new line)
for i in range(5):  # Iterates from 0 to 4
    print(i)  # Output: 0, 1, 2, 3, 4 (each on a new line)

our_list=[44,77,11,33]
print(our_list)
our_iter=iter(our_list)
print(our_iter)
print(next(our_iter))
print(our_iter.__next__())
print(our_iter.__next__())

class Pow_of_Two:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
print(Pow_of_Two.__doc__)
a=Pow_of_Two(4)
i=iter(a)
print(next(i))
print(next(i))
print(next(i))

class Infinite_Iter:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        num=self.num
        self.num+=2
        return num
i=Infinite_Iter()
a=iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

a=[1,2,3,4,5]
for i in a:
    print(i,end=" ")
    print("hello")
for i in range(6,11):
    print(i)
b={11,12,13,14,15}
for i in b:
    print(i)
else:
    print("Printing Completed")

