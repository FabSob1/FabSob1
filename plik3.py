import math
import sys

print ("Podaj wartosci funkcji: a^2x + bx +c: ")
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#a^2x + bx + c
def fun(a, b, c):
    b = b*b
    delta = b - (4*a*c)
    if delta >0:
        x1 = (-b  -  math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
    elif delta == 0:
        x1 = -b/2*a
        print (x1)
        print (x2)

    else : 
        print ("brak rozwiazan")

fun(a,b,c)
