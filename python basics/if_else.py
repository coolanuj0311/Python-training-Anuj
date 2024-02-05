'''What are if-else statements?

They are control flow statements that allow you to execute different code blocks based on whether a certain condition is true or false.
This enables you to make decisions in your code and control the flow of execution.

Types of if-else statements:

if statement:

Executes a block of code only if a condition is true.

if-else statement:

Executes one block of code if a condition is true, and a different block if it's false.

if-elif-else chain:

Allows for multiple conditions and code blocks to be executed based on which condition is met first.

How they work:

Condition evaluation: The interpreter starts by evaluating the condition in the if statement.
Code execution: If the condition is true, the code block within the if clause is executed.
Alternative execution: If the condition is false and there's an else clause, the code within the else clause is executed.
Multiple conditions: In an if-elif-else chain, each elif condition is checked in order until one is true, and its corresponding code block is executed.
Indentation: The code blocks within each clause must be indented consistently to define their scope.
'''
age=int(input("Please enter the age of the person:"))
if age<5:
    print("Too young")
elif age==5:
    print("Kindergarden")
elif((age>5) and age<=17):
    grade=age-5
    print("Go to {} grade".format(grade))
else:
    print("Go to college")

num=float(input("Enter an number:"))
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Positive number")

else:
    print("Negative number")




