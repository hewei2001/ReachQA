import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
planets = ['Jupiter', 'Mars', 'Venus', 'Saturn', 'Neptune']
years = ['2020', '2021', '2022', '2023']
coffee_consumption = np.array([
    [80, 85, 90, 95],  # Jupiter
    [50, 60, 55, 65],  # Mars
    [30, 40, 45, 50],  # Venus
    [20, 25, 30, 35],  # Saturn
    [70, 75, 80, 85]   # Neptune
])

# Setup the figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid for bar positions
x_data = np.arange(len(planets))
y_data = np.arange(len(years))
x_data, y_data = np.meshgrid(x_data, y_data)
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = np.zeros_like(x_data)
dz = coffee_consumption.flatten()

# Define bar dimensions and colors
dx = dy = 0.4
colors = plt.cm.viridis(dz / dz.max())

# Plot 3D bars
ax.bar3d(x_data, y_data, z_data, dx, dy, dz, color=colors, zsort='average', alpha=0.8)

# Adding annotations for each bar
for i in range(len(dz)):
    ax.text(x_data[i], y_data[i], dz[i] + 2, f'{dz[i]}', color='black', ha='center', fontsize=8)

# Customize axes ticks and labels
ax.set_xticks(np.arange(len(planets)))
ax.set_xticklabels(planets, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years, fontsize=10)
ax.set_xlabel('Planets', fontsize=12)
ax.set_ylabel('Years', fontsize=12)
ax.set_zlabel('Coffee Consumption\n(Million Tons)', fontsize=12)

# Enhance titles and context
ax.set_title('Galactic Coffee Consumption\n2020-2023 Overview', fontsize=16, fontweight='bold', loc='left')

# Adding color legend
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=dz.min(), vmax=dz.max()))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.5, aspect=10, pad=0.1)
cbar.set_label('Consumption Level', fontsize=12)

# Customize the view angle
ax.view_init(elev=25, azim=120)

# Add grid for better reference
ax.grid(True, linestyle='--', linewidth=0.5)

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()