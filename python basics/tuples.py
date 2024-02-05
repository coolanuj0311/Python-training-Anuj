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

tuple1=()
print(tuple1)

tuple2=(1,2,3)
print(tuple2)

tuple3=(101,"Anarbian",20000.00,"HR Dept")
print(tuple3)

tuple4=("points",[1,4,3],(7,8,6))
print(tuple4)

tuple5=101,"Anarbian",20000.00,"HR Dept"
print(tuple5)

empid,empname,empsal,empdept=tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)
print(type(tuple5))

tuple1=('w','e','l','c','o','m','e')
print(tuple1)
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])

nest_tuple2=("points",[1,3,4],[8,7,9])
print(nest_tuple2)
print(nest_tuple2[0][3])
print(nest_tuple2[1][2])
print(nest_tuple2[2][2])

tuple1=('w','e','l','c','o','m','e')
print(tuple1)
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])

tuple1=('w','e','l','c','o','m','e')
print(tuple1)
tuple1=('g','o','o','d','b','y','e')
print(tuple1)

tuple2=('w','e','l','c')
tuple3=('o','m','e')
print(tuple2)
print(tuple3)
print(tuple2+tuple3)
print(("again",)*4)

tuple4=('w','e','l','c','o','m','e')
print(tuple4)
del tuple4

tuple5=('w','e','l','c','o','m','e')
a=tuple5.count('e')
b=tuple5.index('c')
print(a)
print(b)

tuple6=('w','e','l','c','o','m','e')
print('c' in tuple6)
print('c' not in tuple6)
print('a' in tuple6)
print('a' not in tuple6)

tuple6=('w','e','l','c','o','m','e')
for letters in tuple6:
    print("letter is ->",letters)

tuple7=(22,33,55,44,77,66,11)
print(tuple7)
print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))









