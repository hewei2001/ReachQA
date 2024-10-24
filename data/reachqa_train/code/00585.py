import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data for the chart
years = np.array([2030, 2031, 2032, 2033, 2034])
destinations = ['Moon', 'Mars', 'Space Hotels']
moon_tourists = np.array([10, 15, 25, 35, 50])
mars_tourists = np.array([5, 10, 20, 30, 45])
space_hotels_tourists = np.array([20, 25, 35, 50, 70])
tourist_data = np.array([moon_tourists, mars_tourists, space_hotels_tourists])

# Create the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Prepare for plotting
_x = np.arange(len(years))
_y = np.arange(len(destinations))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros_like(x)
dx = dy = 0.4
dz = tourist_data.ravel()

# Plotting the bars
colors = ['skyblue', 'salmon', 'palegreen']
for i in range(len(destinations)):
    ax.bar3d(x[y == i], y[y == i], z[y == i], dx, dy, dz[y == i], color=colors[i], alpha=0.8)

# Labeling the axes
ax.set_xlabel('Year')
ax.set_ylabel('Destination')
ax.set_zlabel('Tourists (Thousands)')

# Title with a line break for clarity
ax.set_title("Exploring the Cosmos: Space Tourism Growth\n(2030-2034)", fontsize=14, fontweight='bold')

# Setting x-ticks and y-ticks
ax.set_xticks(_x)
ax.set_xticklabels(years)
ax.set_yticks(_y)
ax.set_yticklabels(destinations)

# Adjust the viewing angle
ax.view_init(elev=25, azim=135)

# Enhancing visual appearance
ax.grid(True, linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.tight_layout()

# Display the plot
plt.show()