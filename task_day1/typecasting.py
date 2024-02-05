'''Type-casting:

Converting between data types (e.g., int(3.14) converts a float to an integer).
Remember:

Casting may cause errors if the conversion is not possible (e.g., "abc" to int).
Choose the appropriate casting method based on the desired data type and format.


1. Converting between Numbers:

Int to string: str(35) -> "35"
Float to string: str(3.14159) -> "3.14159"
String to int: int("42") -> 42
String to float: float("1.23") -> 1.23

2. Converting to Boolean:

bool(0) -> False (zero is considered false)
bool("") -> False (empty string is considered false)
bool(None) -> False (None represents no value)
bool("Hello") -> True (non-empty string is considered true)
bool(1) -> True (any non-zero number is considered true)

3. Converting to Lists:

str.split(): splits a string into a list of words
str = "This is a sentence."
list = str.split() -> ["This", "is", "a", "sentence"]
list(range(5)): creates a list of numbers from 0 to 4
list("apple"): creates a list of individual characters from a string

4. Converting to Tuples:

tuple(): creates an empty tuple
tuple([1, 2, 3]): creates a tuple from a list


'''
