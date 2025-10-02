import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

for x in arr:
  print(x)


for x in arr:
  for y in x:
    print(y)