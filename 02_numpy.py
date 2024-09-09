import numpy as np

array2d = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(array2d)
arrayOnes = np.ones((3,4))
arrayInt = arrayOnes.copy().astype(int)
print(arrayOnes)
print(arrayInt)

arrayZeros = np.zeros((3,4))
arrayZInt = arrayZeros.copy().astype(bool)
arrayZIStr = arrayZInt.copy().astype(str)
print(arrayZeros)
print(arrayZInt)
print(arrayZIStr)

arrayEmpty = np.empty((3,3))
print(arrayEmpty)