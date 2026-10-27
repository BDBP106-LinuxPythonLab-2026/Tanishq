#Write a program to filter out the odd elements of the Fibonacci series for the first n terms.
nums=int(input("enter the number of terms:"))
a,b=0,1
fib=[]
for i in range(nums):
    fib.append(a)
    a,b=b,a+b
odd=[x for x in fib if x%2!=0]
print("fibbonacci series:",fib)
print("odd elements:",odd)
