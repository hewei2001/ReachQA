import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define years and planets
years = np.array([2025, 2030, 2035])
planets = ['Earth', 'Mars', 'Europa']

# Export volumes of minerals in metric tons (Platinum, Helium-3, Tritium)
exports_earth = np.array([[500, 600, 550], [400, 500, 450], [300, 400, 350]])
exports_mars = np.array([[100, 150, 200], [250, 300, 350], [200, 250, 300]])
exports_europa = np.array([[200, 250, 300], [300, 350, 400], [450, 500, 550]])

# Stacking mineral data for each planet
exports = [exports_earth, exports_mars, exports_europa]

# Initialize plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for each mineral
colors = ['royalblue', 'lightcoral', 'limegreen']
mineral_names = ['Platinum', 'Helium-3', 'Tritium']

# Plotting stacked bars
x_pos = np.arange(len(planets))
y_pos = np.arange(len(years))

for i, planet in enumerate(planets):
    for j, year in enumerate(years):
        bottom = 0
        for k, mineral in enumerate(mineral_names):
            ax.bar3d(i, j, bottom, 0.5, 0.5, exports[i][j][k], color=colors[k], alpha=0.8)
            bottom += exports[i][j][k]

# Customizing axes
ax.set_xlabel('Planets')
ax.set_ylabel('Years')
ax.set_zlabel('Export Volumes (Metric Tons)')
ax.set_xticks(x_pos)
ax.set_xticklabels(planets, rotation=45, ha='right')
ax.set_yticks(y_pos)
ax.set_yticklabels(years)

# Adjust view for clarity
ax.view_init(elev=20, azim=120)

# Title
ax.set_title('Intergalactic Mineral Trade:\nStacked 3D Bar Analysis of Planetary Exports', fontsize=14, fontweight='bold', y=1.05)

# Adding a legend
patches = [plt.Rectangle((0,0),1,1, color=colors[i], alpha=0.8) for i in range(len(mineral_names))]
ax.legend(patches, mineral_names, loc='upper left', bbox_to_anchor=(1, 1), title="Minerals")

# Automatically adjust layout for readability
plt.tight_layout()

# Show the plot
plt.show()