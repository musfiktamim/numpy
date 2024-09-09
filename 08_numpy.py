import numpy as np
import random

array = np.random.random((3,3))
print(array)
arrayInt = np.random.randint(1,4,(4,4))
print(arrayInt)
array3d = np.random.randint(1,4,(2,4,4))
print(array3d)

arraysed = np.random.seed(10)
print(arraysed)