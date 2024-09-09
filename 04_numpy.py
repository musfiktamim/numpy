import numpy as np

array1 = np.arange(1,10).reshape(3,3)
array2 = np.arange(1,10).reshape(3,3)

print(array1+array2)
print(np.add(array1,array2))
print(array1-array2)
print(np.subtract(array1,array2))
print(array1*array2)
print(np.multiply(array1,array2))
print(array1/array2)
print(np.divide(array1,array2))
print(np.cumsum(array1))
print(np.cumprod(array1))

array2d = np.array([np.arange(1,10),np.arange(1,10)])
print(array2d)
print(np.cumprod(array2d,axis=0))

print(array2d.max())
print(array2d.argmax())

print(array2d.max(axis=0))

print(array2d.min())
print(array2d.argmin())

print(array2d.min(axis=0))
print(array2d.argmin(axis=0))

print(array2d.mean())
print(np.sqrt(array2d))

print(np.std(array2d))

print(np.exp(array2d))

print(np.log(array2d))
print(np.log10(array2d))