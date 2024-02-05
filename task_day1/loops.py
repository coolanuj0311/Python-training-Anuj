''' Loops:

1. Purpose:

for loop: Iterates over a sequence of elements (like a list, tuple, or string), executing a block of code for each element.
while loop: Repeats a block of code as long as a certain condition is true.

2. Syntax:

for loop:

for element in sequence:
    code_block

while loop:

while condition:
    code_block

3. When to Use:

Use a for loop:
When you know the number of iterations in advance.
When you want to process each element of a sequence.

Use a while loop:
When you don't know the exact number of iterations beforehand.
When the loop should continue based on a condition being met.
When you need more control over the loop's execution.



4.Key Points:

for loops are often used for iterating over known sequences.
while loops are often used for tasks that require repetition until a condition is met.
Use break to exit a loop early and continue to skip to the next iteration.
Both loops can be nested within each other to create more complex logic.

'''
for i in range(5): 
    print(i)

count=0
while count < 10: 
    print(count);
    count += 1

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2) 

count = 0
while count < 5:
    print(count)
    count += 1 