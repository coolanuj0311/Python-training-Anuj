'''What are generator functions?

They are a special type of function that doesn't return a single value, but rather an iterator that produces a sequence of values on demand.
This makes them memory-efficient, especially when dealing with large datasets.
Key characteristics:

Defined using def like regular functions.
Use yield instead of return to pause execution and return values one at a time.
Return a generator object when called, which can be iterated over.
'''

def my_generator():
    n=1
    print("This is printed first")
    yield n
    n+=1
    print("This is print second")
    yield n
    n+=1
    print('This is printed at last')
    yield n
a=my_generator()
next(a)
next(a)
next(a)
print("Using for loop...")
for item in my_generator():
    print(item)

def reverse_string(my_string):
    length=len(my_string)
    for i in range(length-1,-1,-1):
        yield my_string[i]
for char in reverse_string("WORLD"):
    print(char)




