import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)

print(arr)

# NumPy provides a helper function: hstack() to stack along rows.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))

print(arr)

# NumPy provides a helper function: vstack()  to stack along columns.

arr = np.vstack((arr1, arr2))

print(arr)

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

arr = np.dstack((arr1, arr2))

print(arr)