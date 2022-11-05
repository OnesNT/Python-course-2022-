from math import *
def convert_number(a, b):
    if (a >= 0):
        c = a % b
    if (a < 0):
        c = -(abs(a) % b)
    return c ;

x = int(input())
y = int(input())

print(convert_number(x, y));