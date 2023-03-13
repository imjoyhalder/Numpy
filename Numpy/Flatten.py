import numpy as np
k = np.random.randint(6,100,(4,4))

print(k,"\n")
k[(0,1)]=0 # Try to be changed the value
print(k)
print(k.shape)
flatten = k.flatten()
print(flatten)

print(flatten.nbytes)


print(k)