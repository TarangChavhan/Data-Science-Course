import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr)

for x in arr:
  print(x)

for x in arr:
  for y in x:
    for z in y:
      print(z)

# nditer() In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
for x in np.nditer(arr):
  print(x)

# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
# Enumerated Iteration Using ndenumerate()
# we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  