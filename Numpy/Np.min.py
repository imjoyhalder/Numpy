import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print("Minimum: ",np.min(arr))

arr1 = np.array([11,12,13,11,10,1,23,4,5,6,7])
print("Max: ",np.max(arr1))

# Use of max
arr2 = np.array([3,4,5,33,5,6,75,])
print("Max: ",np.max(arr2),"  Position: ",np.argmax(arr2))
print()
# Use of Mini
arr3 = np.array([2,3,4,5,6,1,5,55,63,56])
print("Mini: ",np.min(arr3),"  Position: ",np.argmin(arr3))
print()
# Use of Squrt
arr4 = np.array([3,4,5,6,7,22,25,24])
print(np.sqrt(arr4))
print()
#Use of Sin
arr5 = np.array([0,30,45,60,90])
print(np.sin(arr5))
print()

# Use of cos
arr6 = np.array([3,4,5,6,7,22,25,24])
print(np.cos(arr6))

print()
#Use of Cumsum
arr7 = np.array([3,4,5,6,7,22,25,24])
print(np.cumsum(arr7))






