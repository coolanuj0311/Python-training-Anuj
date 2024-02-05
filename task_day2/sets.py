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