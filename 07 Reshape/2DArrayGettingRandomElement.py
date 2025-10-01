# 2D Array = arr[row_start:row_end , col_start:col_end]
# 3D Array = arr[depth_start:depth_end , row_start:row_end , col_start:col_end]


import numpy as np 

arr = np.arange(1,26)

D2Arr = arr.reshape(5,5)

print(D2Arr)

sliceing = D2Arr[0:2,1:3]
print(sliceing)

Slicing2 = D2Arr[2:,2:4]
print(Slicing2)