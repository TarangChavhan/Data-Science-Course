import numpy as np

single = np.array(45)
One = np.array([1,2,3,4,5,6])
two = np.array([[1,2,3],[4,5,6]])
three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(single.ndim)
print(One.ndim)
print(two.ndim)
print(three.ndim)