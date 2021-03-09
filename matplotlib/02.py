import matplotlib.pyplot as plt
import numpy as np

print("Numpy variables".center(50, '-'))
print(x)
print(y)

fig = plt.figure()

# left , bottom , width , height
ax01 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax02 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

ax01.plot(x, y)
ax02.plot(y, x)
plt.show()
