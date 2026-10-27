#Write the above program using lambda expression.
temp_c=list(map(int,input('Enter temp in c').split()))
temp_f=list(map(lambda p:round(p*1.8+32),temp_c))
print(temp_f)