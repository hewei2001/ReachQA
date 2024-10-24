import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define sectors and years
sectors = ['Transportation', 'Education', 'Healthcare', 'Housing', 'Recreation']
years = ['2023', '2024', '2025', '2026', '2027']

# Define investment data (in millions) for each sector per year
investments = np.array([
    [150, 160, 170, 180, 190],  # Transportation
    [100, 110, 115, 120, 125],  # Education
    [120, 130, 140, 150, 160],  # Healthcare
    [90, 100, 110, 120, 130],   # Housing
    [50, 55, 60, 70, 75],       # Recreation
])

# Define positions for the bars
xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(sectors)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Define the size of each bar
dx = dy = 0.7
dz = investments.flatten()

# Create the 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot bars for each sector
for i, color in enumerate(colors):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], color=color, alpha=0.8)

# Set labels and ticks
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Sector', fontsize=12, labelpad=10)
ax.set_zlabel('Investment (in millions)', fontsize=12, labelpad=10)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(sectors)))
ax.set_yticklabels(sectors)

# Set title with a line break
ax.set_title('Projected Infrastructure Investment\nin Metropolis Next (2023-2027)', fontsize=14, fontweight='bold', pad=20)

# Adjust the view angle for better visibility
ax.view_init(elev=20., azim=45)

# Enhance the visualization
ax.grid(True)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()