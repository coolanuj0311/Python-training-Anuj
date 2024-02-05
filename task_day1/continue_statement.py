
'''The continue statement in Python is another loop control statement, but it works quite differently from break.
Instead of terminating the loop, it skips the remaining statements in the current iteration and immediately goes to the next iteration.

Here's a breakdown of the continue statement:

What it does:

Skips the rest of the code in the current iteration of a loop (for or while).
Control flow jumps to the beginning of the next iteration.

Placement:

Used within the body of a loop.'''

# Skip numbers divisible by 3 in a for loop:
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

# Continue adding numbers until the sum exceeds 100:
total = 0
while total <= 100:
    num = int(input("Enter a number: "))
    total += num
    continue  # This line won't be executed if sum exceeds 100

# Build a list with squares of even numbers only:
squares = []
for i in range(1, 11):
    if i % 2 != 0:
        continue
    squares.append(i * i)

print(squares)  # Output: [4, 16, 36, 64, 100]
