'''  Data Types:

Common types:
Integers (int): Whole numbers (e.g., 42)
Floats (float): Decimal numbers (e.g., 3.14)
Strings (str): Textual data (e.g., "Hello, world!")
Booleans (bool): True or False
Lists (list): Ordered collections of items
Tuples (tuple): Immutable ordered collections
Dictionaries (dict): Unordered key-value pairs  

Integers: 42, -10, 0
Floats: 3.14, -2.5, 1.0
Strings: "hello", "world"
Booleans: True, False
Lists: [1, 2, 3], ["apple", "banana"]
Tuples: (10, 20), ("x", "y")
Dictionaries: {"name": "John", "age": 35}  

difference between list and tuples

Mutability:

Lists are mutable: You can change their elements after creation.
Add, remove, or modify items as needed.

Tuples are immutable: Their elements cannot be changed after creation.
Fixed sets of values that cannot be altered.

Syntax:

Lists use square brackets []: my_list = [1, 2, 3]
Tuples use parentheses (): my_tuple = (1, 2, 3)
Use Cases:

Lists are ideal for:
Storing collections of items that may change.
Ordering elements.
Representing sequences of data.
Tuples are ideal for:
Representing fixed sets of values.
Protecting data from accidental changes.
Passing data around as arguments to functions without modification.
Using as keys in dictionaries (keys must be immutable).

Performance:

Tuples can be slightly faster than lists:
Immutable nature makes them more memory-efficient.
Can be stored as hash values for faster lookups.

Choosing the Right One:

Use lists when you need to modify the elements or order.
Use tuples when you need a fixed set of values or want to ensure data integrity.

'''

