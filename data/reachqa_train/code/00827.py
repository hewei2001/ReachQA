import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the agencies and years
agencies = ['NASA', 'ESA', 'CNSA']
years = np.arange(2010, 2020)

# Success rates of space missions for each agency over the years
successful_missions = np.array([
    [5, 6, 7, 8, 9, 10, 12, 13, 12, 14],  # NASA
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],     # ESA
    [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]    # CNSA
])

# Create a 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for each agency
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Dimensions for the bars
dx = np.ones_like(years) * 0.6
dy = np.ones_like(years) * 0.6

# Plot each agency's performance
for i, agency in enumerate(agencies):
    xs = years
    ys = np.full_like(xs, i)
    zs = np.zeros_like(xs)
    dz = successful_missions[i]
    
    ax.bar3d(xs, ys, zs, dx, dy, dz, color=colors[i], alpha=0.7, label=agency)

# Customize the plot
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Agency', fontsize=12, labelpad=10)
ax.set_zlabel('Successful Missions', fontsize=12, labelpad=10)
ax.set_xticks(years)
ax.set_yticks(np.arange(len(agencies)))
ax.set_yticklabels(agencies)
ax.set_title('A Decade of Cosmic Exploration:\nSuccess Rates of Global Space Missions', fontsize=14, fontweight='bold', pad=20)
ax.view_init(elev=30, azim=120)

# Enhance visibility with grid
ax.xaxis._axinfo['grid'].update(color='lightgrey', linestyle='--', linewidth=0.5)
ax.yaxis._axinfo['grid'].update(color='lightgrey', linestyle='--', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color='lightgrey', linestyle='--', linewidth=0.5)

# Add a legend
ax.legend(loc='upper left', fontsize='small', bbox_to_anchor=(0.1, 1.05))

# Adjust the layout for better visualization
plt.tight_layout()

# Display the plot
plt.show()