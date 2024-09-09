import numpy as np

ch_name = "musfikur rahman"
str1 = "learn numpy"
print(np.char.add(ch_name,str1))
print(np.char.lower(ch_name))
print(np.char.upper(ch_name))
print(np.char.center(ch_name,50,fillchar="*"))
print(np.char.split(ch_name))
print(np.char.splitlines("hello\nmusfik"))
print(np.char.join())