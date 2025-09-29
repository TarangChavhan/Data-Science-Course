# Fprmula = array[row_start:row_end : row_step, column_start:column_end : column_step]
import numpy as np

d2arr = np.array([[1,2,3],[4,5,6]])
print(d2arr[1, 1:4])
print(d2arr[0:2, 2])
print(d2arr[0:2, 1:4])