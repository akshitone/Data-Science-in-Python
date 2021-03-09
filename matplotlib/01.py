import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2
print("Numpy variables".center(50, '-'))
print(x)
print(y)

# Graph
plt.plot(x, y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Sqaure Number')
plt.show()

# Multiple graphs
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r-')
plt.subplot(1, 2, 2)
plt.plot(y, x)
plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Using figure and axes')
plt.show()
