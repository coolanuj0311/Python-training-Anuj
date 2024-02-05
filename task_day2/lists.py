'''Lists:

Ordered collections of items, mutable (changeable).
Enclosed in square brackets [].
Can hold different data types.
Access elements using indexing (starting from 0).
Example: [1, "apple", 3.14, True]'''

#1. Storing a sequence of numbers:

numbers = [1, 2, 3, 4, 5]
print(numbers[2])  # Output: 3 (accessing the third element)

#2. Holding mixed data types:

mixed_list = [10, "hello", True, 3.14]
print(mixed_list)  # Output: [10, 'hello', True, 3.14]

#3. Creating a list of colors:

colors = ["red", "green", "blue", "purple"]
for color in colors:
    print(color)  # Prints each color on a separate line

#4. Using list comprehension:

squares = [x**2 for x in range(10)]  # Create squares of numbers 0-9
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#5. Slicing lists:

letters = ["a", "b", "c", "d", "e"]
sublist = letters[1:4]  # Extract a slice from index 1 to 3 (excluding 4)
print(sublist)  # Output: ['b', 'c', 'd']

#6. Appending and extending lists:

shopping_list = ["bread", "milk"]
shopping_list.append("eggs")  # Add an item to the end
shopping_list.extend(["apples", "bananas"])  # Add multiple items
print(shopping_list)  # Output: ['bread', 'milk', 'eggs', 'apples', 'bananas']

#7. Finding items in a list:


if "apples" in shopping_list:
    print("Apples are on the list!")

#8. Removing items from a list:

shopping_list.remove("bread")  # Remove the first occurrence of "bread"
shopping_list.pop(2)  # Remove the item at index 2
print(shopping_list)  # Output: ['milk', 'apples', 'bananas']

#9. Sorting a list:

numbers = [5, 2, 8, 1, 9]
numbers.sort()  # Sort in ascending order
print(numbers)  # Output: [1, 2, 5, 8, 9]

#10. Reversing a list:


numbers.reverse()  # Reverse the order of elements
print(numbers)  # Output: [9, 8, 5, 2, 1]