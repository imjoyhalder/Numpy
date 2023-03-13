import numpy as np
a = np.arange(1,21,1,dtype="complex")
print(a.reshape(5,4))
b = np.where(a%2 == 0)
print()
print(b)
