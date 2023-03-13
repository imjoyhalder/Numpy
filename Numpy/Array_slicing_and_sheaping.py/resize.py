import numpy as np
arr = np.zeros((5,4))
print(arr)
arr1 = np.ones((4,4))
print()
print(arr1)

print("\n")
arr2 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
print("This is the first Shape of this array")
print(arr2)
resize = np.resize(arr2,(4,3))
print("\n")
print("This is the reshep of first array")
print(resize)