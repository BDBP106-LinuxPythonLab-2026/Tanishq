n=int(input("Enter a digit in a number:"))
S=0
while n>0:
    digit=n%10
    S=S+digit
    n=n//10
print(S)