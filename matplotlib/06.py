import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

# alpha uses for transparency, linewidth(lw) uses for thickness, linestyle(ls) uses for styling
plt.plot(x, y, color='green', lw=2, alpha=0.5,
         ls=':', marker='o', markersize=10, markerfacecolor="red")
plt.plot(x, x**3, color='purple', lw=2, alpha=0.8,
         ls='--', marker='*', markersize=15, markerfacecolor="yellow", markeredgewidth=2, markeredgecolor='blue')
plt.show()
