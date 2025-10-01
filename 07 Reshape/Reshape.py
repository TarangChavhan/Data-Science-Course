# arr.reshape(no_of_arrays, rows, columns)

import numpy as np

arr = np.arange(1,31)

print(arr) # 1D Array 

newarr = arr.reshape(5,6) # Two Diminsion array, It Should have Perfect Fixing Number is matrix while reshaping it
print(newarr)


D3Arr= arr.reshape(1,5,6) # Single 1D To 3D Array.
print(D3Arr)

D3Arr2 = arr.reshape(2,5,3) # 
print(D3Arr2)

AutoCalculate = arr.reshape(2,-1,5) # Pass -1 as the value, and NumPy will calculate this number for you.
print(AutoCalculate)

D1Arr = D3Arr2.reshape(-1) # 3d to 1d
print(D1Arr)