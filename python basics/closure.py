'''What is a Closure?

A closure is a function that has access to variables in its outer (enclosing) function's scope, even after the outer function has finished executing.
It's essentially a nested function that "remembers" the values of those outer variables.
How It Works:

Creating a Closure:

Define a nested function within an outer function.
The nested function references variables from the outer function's scope.
Return the nested function from the outer function.
Accessing Enclosed Variables:

The closure can access and use those variables even after the outer function is done.
It creates a "closed" environment that preserves those values.'''

'''def print_message(message):
    def print_message_inner():
        print(message)
    return print_message_inner()
another=print_message("Hello")
another()
'''
def multiplier_outer(n):
    def multiplier_inner(x):
        return x*n
    return multiplier_inner
times3=multiplier_outer(3)
times5=multiplier_outer(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))