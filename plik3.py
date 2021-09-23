import math
import sys

print ("Podaj wartosci funkcji: a^2x + bx +c: ")
a,b,c = sys.argv[1:]
a = int(a)
b = int(b)
c = int(c)
#a^2x + bx + c
def fun(a, b, c):
    delta = b*b- (4*a*c)
    if delta >0:
        x1 = (-b  -  math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        print (x1)
        print (x2)

    elif delta == 0:
        x1 = -b/2*a
        print (x1)

    else : 
        print ("brak rozwiazan")

fun(a,b,c)
