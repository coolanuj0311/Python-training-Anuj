'''Global variables can be accessed from anywhere within a module, but using them excessively can make code less modular and harder to test.
Local variables are preferred for better code organization and reusability.
Use the global keyword to modify a global variable from within a function.
Use the nonlocal keyword to modify variables in enclosing namespaces from within nested functions.
'''


x="global"
def funct1():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)
print("Global x=",x)
funct1()
print("Global x=",x)

a=5
def funct2():
    a=10
    print("local a:",a)
print("global a:",a)
funct2()
print("global a:",a)

def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()