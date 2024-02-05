''' Iterators:

Objects that allow you to traverse elements one by one.
(list is an iterable)
Iterators provide a way to access elements of a sequence one at a time.
They are fundamental for efficient data handling, especially with large datasets.
Use them in loops, comprehensions, and various built-in functions for flexible data processing.
'''
#1.Built-in Iterators:

#Lists:
my_list = [1, 2, 3, 4, 5]
for item in my_list:  # Iterates over the list elements
    print(item)

#Strings:

my_string = "Hello,Anuj!"
for char in my_string:  # Iterates over each character
    print(char)

#Ranges:
for num in range(5):  # Generates numbers from 0 to 4
    print(num)
