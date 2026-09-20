from _pyrepl import simple_interact

principle = float(input('Enter your principle:'))
rate = float(input('Enter your rate of interest in percentage per annum:'))
time = float(input('Enter your time of interest in years:'))

import math
simple_interest = principle * rate * time / 100
amount = math.floor(simple_interest+principle)

print(simple_interest)
print(amount)