#Write a program to find the sum of all the elements in a list using lambda and reduce functions.
from functools import reduce
list1=[1,6,4,9,7]
Sum=reduce(lambda x,y: x+y , list1)
print(Sum)