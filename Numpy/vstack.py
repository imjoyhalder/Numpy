import numpy as np
arr = np.arange(1,21)
two_dimention = arr.reshape(4,5)
print(two_dimention)
print()
# vstack is Vartical Stack

new = two_dimention*3
print(new)
print()

vstack = np.vstack((new,two_dimention))
print(vstack)
print()

# concatenate
con = np.concatenate((new,two_dimention))
print(con)

# Vstack and concatenate works is same