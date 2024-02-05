''' Lambda Functions:

Small, anonymous functions defined inline using the lambda keyword.
Lambda functions are concise, anonymous functions defined using the lambda keyword.
They are often used for simple tasks or as arguments to other functions.
Can have multiple arguments but only one expression.
Contribute to code brevity and expressiveness.
Use them for sorting, filtering, mapping, and other data manipulation tasks.
Employ them in higher-order functions to achieve complex operations.'''

#1. Simple Lambda Function:

add = lambda x, y: x + y  # Equivalent to def add(x, y): return x + y
result = add(5, 3)
print(result)  # Output: 8

#2. Sorting with a Lambda Function:

numbers = [3, 1, 4, 2]
numbers.sort(key=lambda x: x**2)  # Sort by squares
print(numbers)  # Output: [1, 2, 3, 4]

#3. Filtering with a Lambda Function:

words = ["apple", "banana", "cherry", "date"]
filtered_words = list(filter(lambda word: len(word) > 5, words))
print(filtered_words)  # Output: ["banana", "cherry"]

#4. Mapping with a Lambda Function:

numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]

#5. Using Lambda in Higher-Order Functions:

from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # Calculate the product
print(product)  # Output: 24

#6. Sorting a List of Dictionaries by a Key:

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
data.sort(key=lambda item: item["age"])  # Sort by age
print(data)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]

#7. Passing Lambda as an Argument:

def apply_operation(x, operation):
    return operation(x)

result = apply_operation(10, lambda x: x * 2)
print(result)  # Output: 20
