import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Device categories and educational stages
devices = ['Tablets', 'Laptops', 'Interactive Whiteboards']
stages = ['Primary', 'Secondary', 'Tertiary']

# Usage data as percentages
usage_data = np.array([
    [60, 20, 20],  # Primary
    [30, 50, 20],  # Secondary
    [20, 70, 10]   # Tertiary
])

# X, Y positions for each device-stage pair
_x = np.arange(len(stages))
_y = np.arange(len(devices))
_xx, _yy = np.meshgrid(_x, _y)

# Flatten the arrays to plot in bar chart
x = _xx.ravel()
y = _yy.ravel()
z = np.zeros_like(x)

# Corresponding usage percentages as heights of bars
dz = usage_data.T.ravel()

# Define colors for each device category
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Initialize figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the 3D bar chart
ax.bar3d(x, y, z, 0.6, 0.6, dz, color=[colors[i % len(devices)] for i in range(len(dz))], edgecolor='w')

# Setting labels and title
ax.set_xlabel('Educational Stage', labelpad=10)
ax.set_ylabel('Device Type', labelpad=10)
ax.set_zlabel('Usage (%)', labelpad=10)
ax.set_title('Digital Device Usage\nin Educational Settings', fontsize=14, weight='bold', pad=20)

# Setting ticks and labels for each axis
ax.set_xticks(_x + 0.3)
ax.set_xticklabels(stages, fontsize=10, weight='bold', rotation=45)
ax.set_yticks(_y + 0.3)
ax.set_yticklabels(devices, fontsize=10, weight='bold')

# Normalize z-axis to 0-100 scale
ax.set_zlim(0, 100)

# Creating a custom legend
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_patches, devices, title="Device Category", loc='upper left', bbox_to_anchor=(1.05, 1))

# Adjust the layout for better appearance and avoid overlaps
plt.tight_layout()

# Set a viewing angle
ax.view_init(elev=30, azim=120)

# Show the plot
plt.show()