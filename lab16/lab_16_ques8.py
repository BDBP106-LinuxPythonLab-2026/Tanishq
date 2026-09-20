import math
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))

if x>0 and y>0:
    print("qudrant 1st")
elif x<0 and y>0:
    print("quadrant 2nd")
elif x<0 and y<0:
    print("quadrant 3rd")
elif x>0 and y<0:
    print("quadrant 4th")
