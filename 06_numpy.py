import numpy as np
array2d1 = np.arange(1,17).reshape(4,4)
array2d2 = np.arange(17,33).reshape(4,4)
print(np.concatenate([array2d1,array2d2]))
print(np.concatenate([array2d1,array2d2],axis=1))
print(np.vstack((array2d1,array2d2)))
print(np.hstack((array2d1,array2d2)))
print(np.hstack((array2d1,array2d2)))
print(np.split(array2d1,2))