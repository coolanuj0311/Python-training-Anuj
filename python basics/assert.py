'''The assert statement in Python is a powerful tool for testing assumptions and catching errors during development. Here's a breakdown of its key aspects:

What it does:

The assert statement checks if a given condition is True.
If the condition is True, the program continues execution normally.
If the condition is False, the program raises an AssertionError exception and stops execution.

<condition> is any valid Python expression that evaluates to True or False.
<optional_error_message> is a string that provides additional information about the failed assertion. This is helpful for debugging purposes.


'''

def avg(marks):
    assert len(marks)!=0
    return sum(marks)/len(marks)
mark1=[11,22,33]
print("Average of mark1:",avg(mark1))
mark1=[10,20]
print("Average of mark1:",avg(mark1))

def avg(marks):
    assert len(marks)!=0,"List is empty."
    return sum(marks)/len(marks)
mark2=[55,88,78,90,79]
print("Average of mark2",avg(mark2))
mark1=[]
print("Average of mark1:",avg(mark1))


