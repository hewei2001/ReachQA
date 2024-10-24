import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define space stations and types of goods
space_stations = ['Omega', 'Zenith', 'Helios', 'Orion', 'Nova', 'Luna', 'Aether', 'Stellar']
goods_types = ['Food', 'Medical', 'Robotics', 'Raw Materials', 'Quantum Tech', 'Textiles', 'Energy Cells']

# Simulated volume data in thousands of cubic meters
volume_data = np.array([
    [80, 60, 70, 90, 100, 50, 40, 30],  # Food
    [30, 40, 25, 35, 50, 45, 55, 65],   # Medical
    [45, 55, 35, 40, 60, 70, 65, 75],   # Robotics
    [60, 70, 80, 55, 65, 85, 95, 75],   # Raw Materials
    [20, 30, 25, 35, 45, 55, 60, 50],   # Quantum Tech
    [50, 40, 45, 55, 60, 50, 65, 75],   # Textiles
    [70, 60, 80, 90, 85, 70, 60, 50],   # Energy Cells
])

# Define colors for each type of goods
colors = ['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', '#B276B2', '#DECF3F']

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar dimensions and positions
bar_width = 0.4
_x = np.arange(len(space_stations))
_y = np.arange(len(goods_types))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros_like(x)
top = volume_data.ravel()

# Plot each type of goods for each space station
ax.bar3d(x, y, z, bar_width, bar_width, top, color=[colors[i // len(space_stations)] for i in range(len(x))], alpha=0.8)

# Labeling
ax.set_xticks(_x + bar_width / 2)
ax.set_xticklabels(space_stations, rotation=45, ha='right')
ax.set_yticks(_y + bar_width / 2)
ax.set_yticklabels(goods_types)
ax.set_zlabel('Volume (000s Cubic Meters)', fontsize=10)

# Title
ax.set_title(
    "Interstellar Cargo Distribution:\nVolume of Goods Delivered to Space Stations in 2123",
    fontsize=14, weight='bold', pad=20
)

# Adjust the view angle for better visibility
ax.view_init(elev=30, azim=120)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Legend
legend_labels = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='') for color in colors]
ax.legend(legend_labels, goods_types, title="Types of Goods", loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()