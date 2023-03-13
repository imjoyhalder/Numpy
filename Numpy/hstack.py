import numpy as np
arr = np.arange(1,17,1)
four_dimention = arr.reshape(4,4)
print(four_dimention)
print()
arr2 = four_dimention*2
# hstack
new = np.hstack((four_dimention,arr2))
print(new)

#column_stack
print()
column = np.column_stack((four_dimention,arr2))
print(column)

# hastack and colulmn_stack is same