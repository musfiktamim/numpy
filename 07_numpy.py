import numpy as np
import matplotlib.pyplot as plt

print(np.sin(180))
print(np.sin(90))
print(np.cos(180))
print(np.tan(180))

x_Sin = np.arange(0,3*np.pi,0.1)
print(x_Sin)
y_Sin = np.sin(x_Sin)

plt.plot(x_Sin,y_Sin)
plt.show()