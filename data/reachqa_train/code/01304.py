import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data: Exoplanet discoveries and characteristics
exoplanets = ["Kepler-22b", "Proxima b", "Trappist-1d", "HD 189733 b", 
              "51 Pegasi b", "Kepler-452b", "GJ 1214 b"]
distances = np.array([600, 4.24, 40, 63, 50, 1400, 42])  # in light years
masses = np.array([2.4, 1.1, 0.68, 1.13, 0.47, 5, 6.5])  # relative to Jupiter
discovery_years = np.array([2009, 2016, 2017, 2005, 1995, 2015, 2009])

# Bubble sizes (scaled by mass for visual emphasis)
bubble_sizes = masses * 100

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create scatter plot
scatter = ax.scatter(distances, discovery_years, masses, s=bubble_sizes, 
                     c=distances, cmap='coolwarm', alpha=0.8, edgecolors='w')

# Set labels for the axes
ax.set_xlabel('Distance from Earth (light years)', fontsize=10, labelpad=10)
ax.set_ylabel('Discovery Year', fontsize=10, labelpad=10)
ax.set_zlabel('Mass (Jupiter Mass)', fontsize=10, labelpad=10)

# Set the title with proper spacing to avoid overlap
ax.set_title("Exploring the Cosmos:\nA Decade of Exoplanet Discoveries", 
             fontsize=14, fontweight='bold', pad=40)

# Annotate each point with the exoplanet's name
for i, planet in enumerate(exoplanets):
    ax.text(distances[i], discovery_years[i], masses[i], planet, fontsize=9, ha='right')

# Add a color bar to reflect distance
cbar = plt.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Distance from Earth (light years)', fontsize=10)

# Adjust the viewing angle for better perspective
ax.view_init(elev=20, azim=120)

# Automatically adjust the layout for readability
plt.tight_layout()

# Display the plot
plt.show()