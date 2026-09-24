from posix import MFD_ALLOW_SEALING

N=int(input("Enter a number:"))

if N<2:
    print("Not Prime")
else:
    Prime=True
for i in range(2,N):
    if N%i==0:
        Prime=False
        break
if Prime:
    print("Prime")
else:
    print("Not Prime")

