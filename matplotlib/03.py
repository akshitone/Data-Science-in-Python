import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)

print(ax)
fig, ax = plt.subplots(nrows=1, ncols=2)
print(ax)
for current_ax in ax:
    current_ax.plot(x, y)

# add perfect margin between graphs
plt.tight_layout()
plt.show()
