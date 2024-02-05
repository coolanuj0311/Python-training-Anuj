'''While Python doesn't have a built-in array data structure like some other languages, it offers several ways to work with arrays:

1. Lists:

Most common way to represent arrays: Lists are versatile and can hold elements of different data types.
Dynamically sized: They can grow or shrink as needed.
Efficient for most array operations: Insertion, deletion, and access have O(1) time complexity in most cases.

2. NumPy Arrays:

Optimized for numerical computations: NumPy arrays offer efficient storage and operations for large numerical datasets.
Homogeneous: All elements must be of the same data type.
Fast vectorized operations: Perform calculations on entire arrays without explicit loops.
Require the NumPy library:

3. ctypes Arrays:

Access arrays from C code: ctypes module allows interaction with C libraries.
Fixed-size: Size must be specified in advance.
Specific data types: Elements must be of a compatible C data type.

4. Custom Array Implementation:

For specific needs or learning purposes: You can create a custom array class using lists or other Python data structures.
Choosing the Right Approach:

Lists: General-purpose, flexible arrays for most tasks.
NumPy Arrays: Numerical computations, large datasets, vectorized operations.
ctypes Arrays: Interacting with C code or libraries.
Custom Implementation: Specific requirements or learning exercises.'''


my_list = [1, 2, 3, "hello", True]
print(my_list[2])  # Accessing elements
my_list.append(4)  # Adding elements
my_list.remove(2)  # Removing elements
print(my_list)

import numpy as np
my_array = np.array([1, 2, 3, 4])
print(my_array * 2)  # Vectorized operation


import ctypes

my_array = (ctypes.c_int * 4)(*[1, 2, 3, 4])  # Array of 4 integers
print(my_array[0])

arr=[10,20,30,40,50]
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

brands=["coke","Apple","Google","Microsoft","Toyota"]
print(brands)

print(len(brands))

num_brands=len(brands)
print(num_brands)

brands.append("Intel")
print(brands)

colors=["indigo","blue","green","yellow","orange","red"]
print(colors)
del colors[4]
print(colors)
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)

fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits)
fruits[1]="Pineapple"
print(fruits)
fruits[-1]="Guava"
print(fruits)

concat=[1,2,3]
print(concat)
concat=concat+[4,5,6]
print(concat)

repeat=["a"]
print(repeat)
repeat=repeat*5
print(repeat)

fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])

multd=[[1,2],[3,4],[5,6],[7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])













