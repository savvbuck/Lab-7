import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y = np.arange(-0.5, 0.5, 0.01)
x, y = np.meshgrid(x, y)
z = np.tan(x + y)

fig, ax = plt.subplots(subplot_kw={'projection':'3d'}, figsize=(10, 4))
ax.plot_surface(x, y, z, cmap='coolwarm', vmin=z.min())


plt.show()