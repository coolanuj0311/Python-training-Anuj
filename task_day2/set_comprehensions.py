'''Set Comprehensions:

Similar syntax, but creates sets.
Example: {x for x in range(10) if x % 2 == 0} creates {0, 2, 4, 6, 8}'''

#1. Creating a set of unique squares:

unique_squares = {x**2 for x in range(10)}  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

#2. Filtering even numbers from a list and removing duplicates:

numbers = [1, 4, 2, 5, 6, 2, 4]
even_set = {x for x in numbers if x % 2 == 0}  # Output: {2, 4, 6}
#3. Creating a set of unique letters from a string:

phrase = "hello world"
unique_letters = {letter for letter in phrase}  # Output: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

#4. Finding unique words in a list:

words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = {word for word in words}  # Output: {'apple', 'banana', 'cherry'}

#5. Converting a list to a set to remove duplicates:

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}  # Output: {1, 2, 3, 4, 5}

#6. Generating a set of prime numbers:

primes = {x for x in range(2, 50) if all(x % y != 0 for y in range(2, x))}  # Output: {2, 3, 5, 7, ..., 47}

#7. Creating a set of character pairs from a string:

word = "hello"
pairs = {(word[i], word[i+1]) for i in range(len(word)-1)}  # Output: {('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')}

#8. Finding common elements in two sets:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common_elements = {x for x in set1 if x in set2}  # Output: {3, 4}

#9. Finding elements in one set that are not in another:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = {x for x in set1 if x not in set2}  # Output: {1, 2}

#10. Creating a set of tuples with unique first elements:

data = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
unique_first = {(x, y) for x, y in data if (x,) not in unique_first}  # Output: {(1, 'a'), (2, 'b'), (3, 'd')}
