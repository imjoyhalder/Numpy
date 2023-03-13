import numpy as np
a = np.array([[10,40,-1,78],[34,21,90,1]])
#   axis = 0 it's works in coloum
# sorted
a.sort(axis=0)
print(a)
print()
print()
b = np.arange(10,19,1,dtype='int')
print(b.reshape(3,(3)))
print()
print(b.argmin(axis=0))
