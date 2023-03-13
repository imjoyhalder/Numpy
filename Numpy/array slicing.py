import numpy as np
a = np.random.rand(5)
print(a)


b = np.array([[1,2,4,5,6],
              [9,8,3,4,5],
              [3,5,8,1,5]])
print(b)

# here is trying to slicing array 

print(b[0,0])
print(b[2,4])
print(b[1,2])
print(b[1,3])

d = np.random.randint(1,10,size = (2,3,3))
print(d)


c = np.array( [[[5, 3, 8],
                [7, 4 ,8],
                [6, 3, 2],
                [3 ,1, 8],
                [6, 9 ,9],
                [7 ,2, 7]]])

print(c[0,1])