

import numpy as np
new = np.array([1,2,3,4,5,6,7,8,9,10])
new_r = np.searchsorted(new,[99,98,78,95])
print(new_r)
print(new)
co = np.copy(new)
print(co)
ve = np.hstack(new)
print(ve)