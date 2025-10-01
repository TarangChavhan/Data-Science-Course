# 2D Array = arr[row_start:row_end , col_start:col_end]
# 3D Array = arr[depth_start:depth_end , row_start:row_end , col_start:col_end]

import numpy as np
 
arr = np.arange(1,31)
print(arr)
D3Arr = arr.reshape(1,-1,2)
print(D3Arr)

Slicing1 = D3Arr[0,0:2,0:]
print(Slicing1)

Slicing2 = D3Arr[0,13:15,0:]
print(Slicing2)