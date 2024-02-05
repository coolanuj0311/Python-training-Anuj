'''Dictionary Comprehensions:

Creates dictionaries using key-value expressions.
Example: {x: x**2 for x in range(5)} creates {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}'''

#1. Creating a dictionary of squares:

squares = {x: x**2 for x in range(5)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#2. Creating a dictionary from two lists:

keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = {key: value for key, value in zip(keys, values)}  # Output: {'a': 1, 'b': 2, 'c': 3}

#3. Reversing key-value pairs:

original_dict = {"apple": "red", "banana": "yellow", "cherry": "red"}
reversed_dict = {value: key for key, value in original_dict.items()}  # Output: {'red': 'apple', 'yellow': 'banana'}

#4. Filtering items based on a condition:

numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
even_numbers_dict = {key: value for key, value in numbers.items() if key % 2 == 0}  # Output: {2: 'two', 4: 'four'}

#5. Transforming values:


words = {"hello": 5, "world": 6}
uppercase_words = {key: value.upper() for key, value in words.items()}  # Output: {'hello': 'HELLO', 'world': 'WORLD
#6. Creating a dictionary from a list of tuples:

data = [("apple", 5), ("banana", 3), ("cherry", 2)]
fruit_counts = {fruit: count for fruit, count in data}  # Output: {'apple': 5, 'banana': 3, 'cherry': 2}

#7. Counting word frequencies:
    
text = "apple banana apple cherry"
word_counts = {word: text.count(word) for word in text.split()}  # Output: {'apple': 2, 'banana': 1, 'cherry': 1}

#8. Creating a dictionary of factorials:

factorials = {x: math.factorial(x) for x in range(6)}  # Output: {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

