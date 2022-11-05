xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())

xd = 2*xc - xa
yd = 2*yc - ya
xe = 2*xc - xb
ye = 2*yc - yb

def check_false_value():
    if (xa == xb) and (ya == yb):
        return False
    if (xc >= min(xa, xb) and xc <= max(xa, xb) and yc >= min(ya, yb) and yc <= max(ya, yb)):
        return False
    return True


if(check_false_value() == True):
    print(xd)
    print(yd)
    print(xe)
    print(ye)
else:
    print(False)