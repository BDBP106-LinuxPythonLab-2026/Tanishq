n=int(input("Enter a number:"))
a=n
b=0
while n>0:
    digit=n%10
    b=b*10+digit
    n=n//10
if a==b:
    print("Palindromic")
else:
    print("Not Palindromic")

