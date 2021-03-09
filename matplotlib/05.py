import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

fig = plt.figure()
plt.plot(x, x**2)
plt.plot(x, x**3)
plt.legend(['X square', 'X cube'], loc=0)
plt.show()
fig.savefig('matplotlib/assets/figure_legend.png')

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, x**2, label='X square')
# ax.plot(x, x**3, label='X cube')
# ax.legend()
# plt.show()

# fig.savefig('matplotlib/assets/figure_legend.png', dpi=200)
