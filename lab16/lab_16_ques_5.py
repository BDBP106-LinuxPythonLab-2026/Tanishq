import math
a=float(input("Enter a number: "))
b=float(input("Enter a number: "))
c=float(input("Enter a number: "))

d=b**2-4*a*c
if d>0:
    print("discriminant is positive , so roots are found")
    print('d')
else:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print(r1)
    print(r2)


