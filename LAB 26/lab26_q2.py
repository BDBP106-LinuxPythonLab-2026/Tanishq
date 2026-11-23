#Array creation and manipulation exercises. Print all the arrays in each exercise
# i Create a 1D array from 0 to 9

import numpy as np
a=np.arange(10)
print(a)

# 2 Create a boolean array of size 3x3.
import numpy as np
arr=np.zeros((3, 3), dtype=bool)
print(arr)

# 3 Using syntax from list comprehension, create an array that satisfies the condition.For example,




#Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print the two arrays.
import numpy as np

a=np.random.rand(20)
print("1D Array")
print(a)

b=a.reshape(4,5)
print("Array")
print(b)

#Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has only 1s. Then stack the two arrays horizontally.
a=np.arange(10)
b=np.ones(10,dtype=int)
print("Array a:", a)
print("Array:", b)
print(np.hstack((a,b)))

#
