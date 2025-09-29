# We can also define the step, like this: [start:end:step]

import numpy as np

ArrayOne = np.array([1,2,3,4,5,6])

print(ArrayOne[2:]) # starting From index 2 and display all element [3,4,5,6]
print(ArrayOne[:2]) # End at index 2 [1,2]

print(ArrayOne[2:5]) # Start From Index 2 And Goes to 5 [3,4,5]

print(ArrayOne[2:6:2]) # start From Index 2 End at 6 jump 2 [3,5]

print(ArrayOne[::2]) # Jump 2 from start [1,3,5]

print(ArrayOne[-3:-1]) # start from index -3 backside  and end at -1 [4,5]