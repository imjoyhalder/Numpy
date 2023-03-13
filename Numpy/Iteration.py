import numpy as np
arr = np.array([[[1,2,3,4],[9,8,7,6]]])
for i in arr:
    for j in i:
        for k in j:
            print(k)