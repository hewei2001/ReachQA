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

# New dataset: Average daily usage hours
usage_hours = np.array([
    [2.5, 1.0, 0.5],  # Primary
    [1.5, 2.5, 1.0],  # Secondary
    [1.0, 3.0, 0.8]   # Tertiary
])

# X, Y positions for each device-stage pair for the 3D plot
_x = np.arange(len(stages))
_y = np.arange(len(devices))
_xx, _yy = np.meshgrid(_x, _y)

# Flatten the arrays to plot in bar chart
x = _xx.ravel()
y = _yy.ravel()
z = np.zeros_like(x)

# Heights of bars for 3D chart
dz = usage_data.T.ravel()

# Define colors for each device category
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Initialize figure with two subplots
fig = plt.figure(figsize=(14, 8))

# First subplot: 3D bar chart of usage percentages
ax1 = fig.add_subplot(121, projection='3d')
ax1.bar3d(x, y, z, 0.6, 0.6, dz, color=[colors[i % len(devices)] for i in range(len(dz))], edgecolor='w')
ax1.set_xlabel('Educational Stage', labelpad=10)
ax1.set_ylabel('Device Type', labelpad=10)
ax1.set_zlabel('Usage (%)', labelpad=10)
ax1.set_title('Digital Device Usage\nin Educational Settings', fontsize=13, weight='bold', pad=20)
ax1.set_xticks(_x + 0.3)
ax1.set_xticklabels(stages, fontsize=10, weight='bold', rotation=45)
ax1.set_yticks(_y + 0.3)
ax1.set_yticklabels(devices, fontsize=10, weight='bold')
ax1.set_zlim(0, 100)
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(legend_patches, devices, title="Device Category", loc='upper left', bbox_to_anchor=(1.05, 1))
ax1.view_init(elev=30, azim=120)

# Second subplot: 2D stacked bar chart of average daily usage hours
ax2 = fig.add_subplot(122)
for i, device in enumerate(devices):
    ax2.bar(stages, usage_hours[:, i], bottom=np.sum(usage_hours[:, :i], axis=1), color=colors[i], label=device, width=0.5)

ax2.set_xlabel('Educational Stage', fontsize=10, weight='bold')
ax2.set_ylabel('Average Daily Usage (Hours)', fontsize=10, weight='bold')
ax2.set_title('Average Daily Digital Device Usage\nby Educational Stage', fontsize=13, weight='bold', pad=20)
ax2.legend(title="Device Category")
ax2.set_ylim(0, np.max(usage_hours.sum(axis=1)) + 1)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plots
plt.show()