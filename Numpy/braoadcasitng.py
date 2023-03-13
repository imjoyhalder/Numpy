import numpy as np
arr = np.array([1,2,3])
arr2 = np.array([4,3,4])
print(arr*arr2)
print()
a = np.arange(1,10)
new = a.reshape((3,3))
print(new)
print()
b = new*2
print(b)
print()
print(new+b)