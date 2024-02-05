'''Dictionaries:

Unordered collections of key-value pairs.
Mutable (can add, remove, or modify key-value pairs).
Enclosed in curly braces {}.
Keys must be unique and immutable.
Used for efficient lookups by key.
Example: {"name": "Anuj", "age": 23}'''

#1. Storing user information:

user = {
    "name": "Anuj",
    "age": 23,
    "city": "Noida",
    "email": "anuj@example.com"
}
print(user["name"])  # Output: Anuj

#2. Creating a phonebook:

phonebook = {
    "Anuj": "123-456-7890",
    "Jane": "987-654-3210",
    "Bob": "555-1212"
}
print(phonebook["Anuj"])  # Output: 987-654-3210

#3. Counting word frequencies:

text = "apple banana apple cherry banana"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)  # Output: {'apple': 2, 'banana': 2, 'cherry': 1}

#4. Building a shopping cart:

cart = {}
cart["apple"] = 2
cart["banana"] = 3
cart["bread"] = 1
print(cart)  # Output: {'apple': 2, 'banana': 3, 'bread': 1}

#5. Storing configuration settings:

settings = {
    "username": "admin",
    "password": "123456",
    "language": "English",
    "theme": "dark"
}
print(settings["language"])  # Output: English

#6. Representing a graph:

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"]
}
print(graph["A"])  # Output: ['B', 'C']

#7. Using dictionary comprehension:

squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#8. Iterating over key-value pairs:

for key, value in user.items():
    print(f"{key}: {value}")

#9. Checking for key existence:

if "email" in user:
    print("Email is present in the dictionary.")

#10. Accessing nested dictionaries:

person = {
    "name": "Bob",
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}
print(person["address"]["city"])  # Output: Anytown
