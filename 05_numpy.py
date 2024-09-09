import numpy as np

array = np.arange(1,101).reshape(10,10)
print(array)

print(array[0])
print(array[0,0])
print(array[:,0])
print(array[:,0:1])
print(array[1:4,1:4])
print(array[:,1:3])
# print(array[::])
print(array.itemsize)
print(array.dtype)