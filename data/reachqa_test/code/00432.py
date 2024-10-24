import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Extended data for star systems
star_systems = [
    'Alpha Centauri', 'Proxima Centauri', 'Barnard\'s Star', 
    'Wolf 359', 'Lalande 21185', 'Sirius', 'Epsilon Eridani', 
    'Tau Ceti', 'Gliese 581', 'Kepler-186', 'TRAPPIST-1', 
    'Luyten\'s Star', 'Ross 128', 'Vega', 'Betelgeuse'
]

# Distances in light years
distances = np.array([4.37, 4.24, 5.96, 7.78, 8.31, 8.6, 10.5, 11.9, 20.3, 490, 39.6, 12.4, 11.0, 25.0, 548])

# Number of missions conducted
missions = np.array([50, 60, 30, 20, 25, 15, 10, 8, 5, 2, 12, 18, 22, 17, 5])

# Average success rate of missions in percentage
success_rate = np.array([80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 70, 60, 55, 50, 45])

# Size of scatter points representing mission significance
significance = missions * 10

# Define color map for the success rate
cmap = cm.get_cmap('coolwarm')

# Set up the figure with subplots
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot with color map representing success rate
sc = ax.scatter(distances, missions, s=significance, c=success_rate, cmap=cmap, alpha=0.7, edgecolors='w', linewidth=1.5)

# Adding title and labels
ax.set_title("Galactic Exploration Efforts:\nComparative Analysis of Star Systems", fontsize=18, fontweight='bold')
ax.set_xlabel("Distance from Earth (Light Years)", fontsize=12)
ax.set_ylabel("Number of Missions Conducted", fontsize=12)

# Setting tick marks
ax.set_xticks(np.arange(0, 600, 50))
ax.set_yticks(np.arange(0, 70, 10))

# Adding a color bar to show the success rate gradient
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Mission Success Rate (%)')

# Annotate each point with the star system name, adjusted for overlapping text
for i, (star, x, y) in enumerate(zip(star_systems, distances, missions)):
    ax.annotate(star, (x, y), fontsize=9, xytext=(7, 7), textcoords='offset points', rotation=10, ha='right')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()