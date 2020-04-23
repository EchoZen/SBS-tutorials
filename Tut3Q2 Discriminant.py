a = float(input("Enter value for a:"))
b = float(input("Enter value for b:"))
c = float(input("Enter value for c:"))
import math
d=b**2 - 4*a*c
if d<0:
    print("No values")
elif d>0:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
    print("x is", x, "and", y)
else:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("x is", x)
