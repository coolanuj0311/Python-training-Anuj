
'''constants:

purpose: represent values that remain fixed throughout the program's execution.
technical implementation: python doesn't have a built-in constant keyword like some other languages. however, it relies on conventions to simulate constant behavior.
conventions:
naming: use all uppercase letters, separated by underscores for readability (e.g., max_speed, pi, company_name).
assignment: typically assigned in a separate module or file to avoid accidental changes.

Variables:

Purpose: Store values that can change during program execution.
Declaration: Use lowercase letters or camelCase for names (e.g., name, age, total_count).
Assignment: Use the = operator to assign values.
'''


PI=3.14
GRAVITY=9.8
print(PI)
a="apple"
print(a)
a="aeroplane"
print(a)
a=100
print(a)
b,c,d=1,2.5,"hello"
print(b,c,d)
b=c=d=5
print(b,c,d)