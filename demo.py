import math as m

print ("Hello!")

def add(x,y):
    """Add 2 values"""
    a = x
    b = y
    c = a + b
    print ("We add",a,"and",b)
    return c

a = input("enter value of a:")  # input is always taken as a string
b = input("enter value of b:")  # input is always taken as a string
a,b = b,a

print ("After swapping, a:",a,"and b:",b)

a = int(a)
b = int(b)

print ("Sum of a + b:",a+b)

"""
result = add(2,3)
print ("result is:", result)

result = add(34,39)
print ("result is:", result)
"""

num = 25
result = m.sqrt(num)

print(result)