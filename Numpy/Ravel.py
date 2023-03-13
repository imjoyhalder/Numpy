import numpy as np
a = np.random.randint(2,16,(4,5))
print(a)
revel = a.ravel()
print()
"Ravel makes an one dimention array from any dimention array"
print(revel)
print("\n")
revel[0]=7 # ravel makes an view of main array
           # In this array we can change any value 
print(revel)

b = np.random.randint(4,20,(6,6))
print(b)
ravel = b.ravel()
print("","\n")
print(ravel)
print("","\n")
ravel[7]=67
print(ravel)

