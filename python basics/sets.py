'''Sets:

Unordered collections of unique items.
Mutable (can add or remove items).
Enclosed in curly braces {}.
Used for membership testing and removing duplicates.
Example: {"apple", "banana", "cherry"}'''

#1. Creating sets:

# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using the set() constructor
numbers = set([1, 2, 2, 3, 4])  # Duplicates are automatically removed
print(fruits)
print(numbers)

#2. Checking for membership:

if "apple" in fruits:
    print("Apple is in the set!")

#3. Adding elements:

fruits.add("orange")
print(fruits)  # Output: {"apple", "banana", "cherry", "orange"}

#4. Removing elements:

fruits.remove("banana")  # Raises an error if the element doesn't exist
fruits.discard("grape")  # Doesn't raise an error if the element isn't found

#5. Set operations:

# Union (combines elements from both sets)
all_fruits = fruits.union({"mango", "pineapple"})
print(all_fruits)  # Output: {"apple", "cherry", "orange", "mango", "pineapple"}

# Intersection (finds common elements)
common_numbers = {1, 2, 3}.intersection({2, 3, 4, 5})
print(common_numbers)  # Output: {2, 3}

# Difference (elements in set1 but not in set2)
unique_fruits = fruits.difference({"apple", "mango"})
print(unique_fruits)  # Output: {"cherry", "orange"}

#6. Symmetric difference (elements in either set but not in both):

diff_numbers = {1, 2, 3}.symmetric_difference({2, 3, 4, 5})
print(diff_numbers)  # Output: {1, 4, 5}

#. Checking for subsets and supersets:

if {"apple", "cherry"}.issubset(fruits):
    print("Subset found!")

if {"apple", "cherry", "orange"}.issuperset(fruits):
    print("Superset found!")

#8. Converting sets to lists or tuples:

fruit_list = list(fruits)
print(fruit_list)  # Output: ["apple", "cherry", "orange"]

fruit_tuple = tuple(fruits)
print(fruit_tuple)  # Output: ("apple", "cherry", "orange")

my_set1={11,33,66,55,44,22}
print(my_set1)

my_set2={101,"Agnibha",(21,2,1994)}
print(my_set2)

my_set3={11,22,33,44,33,22}
print(my_set3)

my_set5=set([1,2,3,4])
print(my_set5)
print(type(my_set5))

my_list1=list({11,22,33,44})
print(my_list1)
print(type(my_list1))

my_set1={11,33,44,66,55}
print(my_set1)
my_set1.add(77)
print(my_set1)

my_set1.update([88,99,22])
print(my_set1)

my_set1.update([100,102],[103,104,105])
print(my_set1)

my_set1={11,33,44,66,55}
print(my_set1)

my_set1.discard(4)
print(my_set1)

my_set1.discard(44)
print(my_set1)

my_set1.remove(55)
print(my_set1)

my_set1={11,33,44,66,55}
print(my_set1)

print(my_set1.pop())

print(my_set1.pop())
print(my_set1)

my_set1.clear()
print(my_set1)

myset1={0,1,2,3,4,5}
myset2={4,5,6,7,8,9}
print(myset1)
print(myset2)
print(myset1|myset2)
print(myset2|myset1)
print(myset1.union(myset2))
print(myset2.union(myset1))

myset1={0,1,2,3,4,5}
myset2={4,5,6,7,8,9}
print(myset1)
print(myset2)
print(myset1 & myset2)
print(myset2 & myset1)
print(myset1.intersection(myset2))
print(myset2.intersection(myset1))

myset1={0,1,2,3,4,5}
myset2={4,5,6,7,8,9}
print(myset1)
print(myset2)
print(myset1 - myset2)
print(myset2 - myset1)
print(myset1.difference(myset2))
print(myset2.difference(myset1))

myset1={0,1,2,3,4,5}
myset2={4,5,6,7,8,9}
print(myset1)
print(myset2)
print(myset1 ^ myset2)
print(myset2 ^ myset1)
print(myset1.symmetric_difference(myset2))
print(myset2.symmetric_difference(myset1))

myset1={0,1,2,3,4,5}
print(2 in myset1)
print(6 in myset1)
print(2 not in myset1)
print(6 not in myset1)

for letter in set("welcome"):
    print(letter)

myset1={0,1,2,3,4,5}
print(len(myset1))
print(max(myset1))
print(min(myset1))
print(sorted(myset1))

myset1=frozenset([1,2,3,4])
myset2=frozenset([3,4,5,6])
print(myset1)
print(myset2)
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.difference(myset2))
print(myset1.symmetric_difference(myset2))
