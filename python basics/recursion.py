'''Recursion is a powerful technique in programming where a function calls itself directly or indirectly. While it might seem counterintuitive at first, it can be a concise and elegant way to solve certain problems, especially those involving repetitive tasks or self-similar structures.

Here's how recursion works in Python:

Function Definition: You define a function that includes a base case (stopping condition) and a recursive case (where it calls itself).
Recursive Call: When the function is called, it checks the base case. If met, it returns a specific value or performs a simple operation.
Recursive Step: If the base case isn't met, the function calls itself with modified input that brings it closer to the base case. This creates a stack of function calls.
Unwinding the Stack: Once the base case is reached in a nested call, the function returns a value. This value is returned up through the stack, replacing the input for the previous call. This process continues until the original call is resolved.
'''
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print("factorial of 5 is",fact(5))
