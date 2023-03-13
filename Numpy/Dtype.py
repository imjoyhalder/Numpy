import numpy as np
var = np.array([1,2,3,4,5])
print(var.dtype)

a = np.array([1.0,2.3,4.2])
print(a.dtype)

b = np.array(["a",'v',"b"])
print(b.dtype)

c = np.array(["a","p","s"])
print(c.__reduce__)
print("Anything is possible if you try hardly")
k = np.array([1,2,3,4,5])
new = np.int64(k)
print(k)
print(new.dtype)

c = np.array([1.0,2.3,4.2])
n = np.int_(c)
print(n)