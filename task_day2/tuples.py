'''Tuples

Ordered and immutable (unchangeable) collections of items.
Enclosed in parentheses ().
Often used to represent fixed collections of data.
Accessed using indexing like lists.
Example: (10, "hello", True)
'''

#1. Representing coordinates:

point = (3, 5)
print(point[0])  # Output: 3 (accessing the x-coordinate)

#2. Storing RGB color values:

color = (255, 0, 0)  # Red
print(color)  # Output: (255, 0, 0)

#3. Handling multiple return values from functions:

def divide_and_remainder(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

result = divide_and_remainder(10, 3)
print(result)  # Output: (3, 1)

#4. Passing read-only data to functions:

def display_user_info(name, age):
    print("Name:", name)
    print("Age:", age)

user = ("Anuj", 23)
display_user_info(*user)  # Unpack tuple as arguments

#5. Using tuples as dictionary keys:

employee_data = {
    ("John", "Doe"): "Sales",
    ("Jane", "Smith"): "Marketing",
}
print(employee_data[("John", "Doe")])  # Output: Sales

#6. Grouping related data:

person = ("Anuj", 23, "Software Engineer")
print(person)  # Output: ('Anuj', 23, 'Software Engineer')

#7. Looping through tuples:

fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)  # Prints each fruit on a separate line

#. Creating tuples with a single element:

single_element_tuple = ("hello",)  # Note the comma
print(type(single_element_tuple))  # Output: <class 'tuple'>

#9. Using tuple unpacking:

coordinates = (3, 5)
x, y = coordinates
print(x, y)  # Output: 3 5

#10. Comparing tuples:

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 == tuple2)  # Output: False
