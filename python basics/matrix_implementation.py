'''Here are two common ways to implement matrices in Python:

1. Nested Lists:

Represents a matrix as a list of lists, where each inner list represents a row.
Easy to create and manipulate.

2. NumPy Arrays:

Offers a more comprehensive and efficient way to work with matrices.
Provides optimized operations for matrix manipulation.
'''
a=[['Roy',80,75,85,90,95],
   ['John',75,80,75,85,100],
   ['Dave',80,80,80,90,95]]
b=[['Roy',80,75,855,90,95],
   ['John',75,80,75],
   ['Dave',80,80,80,90,95]]
print(a)
print()
print(b)
n=3
m=4
a=[0]*n
print(a)
for i in range(n):
    a[i]=[0]*m
print(a)
print(a[0])
print(a[0][1])
print(a[1][2])

print(a)
print(a[-1])
print(a[-1][-2])
print(a[-2][-3])

print(a)
b=a[0]
print(b)
b[1]=75
print(b)
print(a)
a[2]=['Sam',82,79,88,97,99]
print(a)

