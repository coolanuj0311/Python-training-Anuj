''' Generator Functions:

Special functions that yield a sequence of values, saving memory.
Generators are memory-efficient, particularly for large datasets or infinite sequences.
They enable iteration without creating the entire sequence in memory at once.
Use generators to create custom iterators and control data flow in a more flexible way.'''

#Generating Fibonacci Sequence:

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

#Infinite Streams:

def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

for num in infinite_counter():
    if num > 10:
        break  # Stop when the count reaches 11
    print(num)