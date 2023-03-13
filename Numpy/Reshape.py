import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)



print()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)
print()
print(newarr.ndim)
print(newarr.shape)
one_dimention = newarr.reshape(4,2,-1)
print(one_dimention)
print(one_dimention.reshape(-1))
print(one_dimention.ndim)
print(one_dimention.shape)
