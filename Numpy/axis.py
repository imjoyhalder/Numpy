import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

print()


arr = np.array([[5,6,7,8],[1,3,5,5]])
arr3 = np.array([1,2,3,4])
print(arr.__add__(arr3))
