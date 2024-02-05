'''What is a break statement?

It's a loop control statement that immediately terminates the execution of the innermost loop it's currently in.
It's used to exit a loop prematurely when a certain condition is met.

How does it work?
Placement: The break statement is placed within the body of a loop (for, while).
Condition: When the interpreter encounters the break statement, it stops the current iteration of the loop and jumps to the first statement after the loop's body.
Innermost Loop: If there are nested loops, break only terminates the innermost loop it's placed within.'''

for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break  # Exits the loop when count reaches 3
import random as r
rand_num=r.randrange(1,20)
print("Number to be guessed: ",rand_num)
i=1
while True:
    print("Number Guessed: ",i)
    if(i==rand_num):
        print("Random number has been guessed successfully!")
        break
    i+=1
print("End of the program...")

