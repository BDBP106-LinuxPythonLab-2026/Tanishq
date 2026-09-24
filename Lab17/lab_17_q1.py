B=input("Enter a binary number:")

decimal=0
for digit in B:
    decimal = decimal*2+int(digit)
print("decimal number =", decimal)