import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Years and sectors
years = np.arange(2020, 2026)
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Energy consumption data (in Petajoules) for each sector over the years
data = {
    'Residential': [50, 52, 51, 50, 48, 47],
    'Commercial': [40, 41, 42, 42, 41, 40],
    'Industrial': [100, 98, 97, 96, 95, 93],
    'Transportation': [70, 69, 68, 67, 66, 65]
}

# Define color palette for each sector
colors = ['#FF7F0E', '#1F77B4', '#2CA02C', '#D62728']

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

x_positions = np.arange(len(years))
y_positions = np.arange(len(sectors))

# Iterate over each sector to plot the bars
for i, (sector, color) in enumerate(zip(sectors, colors)):
    z_positions = np.zeros_like(x_positions)
    dx = dy = 0.8
    dz = data[sector]
    ax.bar3d(x_positions, y_positions[i], z_positions, dx, dy, dz, color=color, alpha=0.7)

# Set viewing angle
ax.view_init(elev=20, azim=45)

# Set axes labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Sector')
ax.set_zlabel('Energy (Petajoules)')
ax.set_title("Energy Consumption in Techlandia:\nSectoral Contributions 2020-2025", fontsize=16, fontweight='bold')

# Set tick labels
ax.set_xticks(x_positions)
ax.set_xticklabels(years)
ax.set_yticks(y_positions)
ax.set_yticklabels(sectors)

# Add legend
ax.legend(sectors, loc='upper left', fontsize=10, title='Sectors', bbox_to_anchor=(1.05, 1))

# Improve layout
plt.tight_layout()

# Show plot
plt.show()