import math

a = int(input())
b = int(input())
c = int(input())

#a^2x + bx + c
def fun(a, b, c):
    b = b*b
    delta = b - (4*a*c)
    if delta >0:
        x1 = (-b  -  math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        print (x1)
        print (x2)

fun(a,b,c)
