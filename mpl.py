import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid in x and y satisfying x^2 + y^2 = 4
theta = np.linspace(0, 2 * np.pi, 100)
r = 2  # sqrt(4)
x = r * np.cos(theta)
y = r * np.sin(theta)

# z = y
z = y

# Plot the 3D curve (circle in x-y, extended with z=y)
ax.plot(x, y, z, label='x² + y² = 4, z = y', color='blue')

# Plot settings
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Curve: x² + y² = 4 and z = y')
ax.legend()
ax.grid(True)

plt.show()
