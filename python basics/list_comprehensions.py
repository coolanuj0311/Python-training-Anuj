'''List Comprehensions:

Concise way to create lists based on existing iterables.
Syntax: [expression for item in iterable if condition]
Example: [x**2 for x in range(5)] creates [0, 1, 4, 9, 16]'''

#1. Creating a list of squares:

squares = [x**2 for x in range(10)]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#2. Extracting even numbers from a list:

numbers = [1, 4, 2, 5, 7, 3]
even_numbers = [x for x in numbers if x % 2 == 0]  # Output: [4, 2, 6]

#3. Creating a list of uppercase letters:

letters = ['a', 'b', 'c', 'd', 'e']
uppercase_letters = [letter.upper() for letter in letters]  # Output: ['A', 'B', 'C', 'D', 'E']

#4. Flattening a list of lists:

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]  # Output: [1, 2, 3, 4, 5, 6]

#5. Generating a list of word lengths:

words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]  # Output: [5, 6, 6]

#6. Creating a list of tuples:

coordinates = [(x, y) for x in range(3) for y in range(2)]  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

#7. Filtering strings based on length:

phrase = "The quick brown fox jumps over the lazy dog"
words = phrase.split()
long_words = [word for word in words if len(word) > 4]  # Output: ['quick', 'brown', 'jumps', 'over', 'lazy']

#8. Combining multiple lists:


list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [x for x in list1 + list2 if x % 2 == 0]  # Output: [2, 4, 6]

#9. Applying a function to each element:

numbers = [1, 4, 9, 16]
square_roots = [round(x**0.5, 2) for x in numbers]  # Output: [1.0, 2.0, 3.0, 4.0]

#10. Transforming elements based on conditions:

numbers = [-3, 0, 5, -1, 2]
sign_strings = ["Negative" if x < 0 else "Zero" if x == 0 else "Positive" for x in numbers]  # Output: ['Negative', 'Zero', 'Positive', 'Negative', 'Positive']

h_letters=[]
for letter in "human":
    h_letters.append(letter)
print(h_letters)

h_letters=[letter for letter in "human"]
print(h_letters)

h_letters=list(map(lambda x:x,'human'))
print(h_letters)

number_list=[x for x in range(20) if x%2==0]
print(number_list)

num_list=[y for y in range(100) if y%2==0 ]
print(num_list)

num_list=[y for y in range(100) if y%2==0 if y%5==0]
print(num_list)

obj=["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

matrix=[[1,2],[3,4],[5,6],[7,8]]
transpose=[[row[i] for row in matrix] for i in range(2)]
print(transpose)


