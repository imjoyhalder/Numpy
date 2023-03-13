import numpy as np

# Add
var = np.array([1,3,4,5,6,7,8])

print(var*3)

var1 = np.array([2,1,3,8,4])
print(var1.__and__(var1))

print(var1*2)

print(var1%3)

print(var1-6)

n_var = np.array([1,2,3,4],[1,2,3,4])
re_var = np.array([1,2,3,4],[1,2,3,4])

cal = n_var + re_var
print(cal)