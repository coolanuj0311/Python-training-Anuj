'''What is a while loop?

It's a control flow statement that allows you to repeat a block of code as long as a certain condition is true.
It's useful when you don't know beforehand how many times the code needs to be executed.How it works:

Check condition: The loop starts by evaluating the condition.
Execute code: If the condition is true, the code within the loop's body is executed.
Repeat: After the code in the body runs, the condition is checked again. If it's still true, the code is executed again. This process repeats until the condition becomes false.
Terminate: When the condition becomes false, the loop terminates, and execution continues with the code after the loop.
'''
i=3
while i>0:
    print(i)
    i-=1
while i<10:
    print(i)
    i+=1

else:
    print("Displayed Suceessfully!")
n=int(input("Please enter the number of layers..."))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(".",end="")
        j=j+1
    j=1
    while j<= 2*i-1:
        print("*",end="")
        j=j+1
    print()
    i=i+1
n=int(input("Please enter the odd number of layers..."))
m=n+1/2
i=1
while i<=n:
    if(i>m):
        b=n-i
        s=2*(i-m)+1
    else:
        b=i-1
        s=2*(m-i)+1
    j=1
    while j<=b:
        print(".",end="")
        j=j+1
    j=1
    while j<=s:
        print("*",end="")
        j=j+1
    print()
    i=i+1
