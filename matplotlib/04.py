import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

# fig = plt.figure(figsize=(8, 2))
# ax = fig.add_axes([0, 0, 1, 1])

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
for current_ax in ax:
    current_ax.plot(x, y)

plt.tight_layout()
plt.show()

fig.savefig('matplotlib/assets/figuare_graph01.png', dpi=200)
