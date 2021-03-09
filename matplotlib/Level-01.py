import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2

plt.plot(x, y)
plt.xlabel('0 to 99 numbers')
plt.ylabel('multiply by 2')
plt.title('Level 01 Graph')

fig = plt.figure()
ax01 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax02 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax01.plot(x, z, color="red")
ax02.plot(x, y, color="red")
plt.show()
