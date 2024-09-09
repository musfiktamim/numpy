import numpy as np
array = np.arange(1,10)
print(array)

arrayLinespace = np.linspace(1,5,4)
print(arrayLinespace)

arrayReshape = array.reshape(3,3)
print(arrayReshape)

array = np.arange(1,13)

array3d = array.reshape(2,3,2)
print(array3d)

Ravel = array3d.ravel()
print(Ravel)

Flatten = array.flatten()
print(Flatten)

Transpose = array3d.transpose()
print(Transpose)