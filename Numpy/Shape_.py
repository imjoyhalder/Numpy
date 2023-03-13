import numpy as np

# To See row and coloum to this array

arr= np.array([[[[[1,2,3,4,5],[2,8,9,5,4]]]]])
print(arr.shape)
print(" ")
print(arr.ndim)
print()
print("Minimum Value: ", np.min(arr) , "Position: ",np.argmin(arr))
print()
print("Maximum Value: ",np.max(arr), "Position: ",np.argmax(arr))

# Squrt
print()
print(np.sqrt(arr))

#Sin
print()
print(np.sin(arr))

#Cos
print()
print(np.cos(arr))

# Dtpye
print(np.dtype(arr))