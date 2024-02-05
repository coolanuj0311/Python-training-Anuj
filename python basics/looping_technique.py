


'''Looping is a fundamental concept in most programming languages, including Python. It allows you to repeat a block of code a certain number of times or until a specific condition is met. Python offers various looping techniques to handle different scenarios:

1. for Loop:

Used to iterate over a sequence (list, tuple, string) or range of numbers.

2. while Loop:

Executes a block of code repeatedly until a condition becomes false.

3. Nested Loops:

You can have one loop inside another to iterate over multiple sequences or layers of data.

4. Loop Control Statements:

break statement exits the loop immediately.
continue statement skips the current iteration and continues to the next.
Useful for controlling the loop execution based on specific conditions.
5. List Comprehensions:

A concise way to create a new list by iterating over another list and transforming each element.
'''

while True:
    n=int(input("Input an integer: "))
    if(n%2==0):
        print("Even number...")
    else:
        print("Odd number...")
