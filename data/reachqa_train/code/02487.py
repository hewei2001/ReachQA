import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define data for exoplanet candidates
planet_names = ['Kepler-452b', 'Proxima Centauri b', 'TRAPPIST-1d', 'LHS 1140 b', 'Ross 128 b']
planet_size = np.array([1.63, 1.27, 0.91, 1.43, 1.19])  # Relative to Earth
distance_from_earth = np.array([1402, 4.24, 39.5, 40.0, 11.0])  # In light-years
habitability_score = np.array([7.5, 8.0, 6.5, 7.8, 8.2])  # Arbitrary scale for visualization

# Define colors for each planet based on habitability score
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each exoplanet candidate
scatter = ax.scatter(planet_size, distance_from_earth, habitability_score,
                     s=habitability_score * 100, c=colors, alpha=0.6, edgecolors='k', linewidth=0.5)

# Set labels and title
ax.set_title('Exoplanet Exploration:\nHabitable Zone Candidates by Size and Distance', fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Exoplanet Size (Earth Radii)', fontsize=11)
ax.set_ylabel('Distance from Earth (Light Years)', fontsize=11)
ax.set_zlabel('Habitability Score', fontsize=11)

# Add a legend with planet names
legend = ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label=planet,
                                       markerfacecolor=color, markersize=10) for planet, color in zip(planet_names, colors)],
                   title='Planet Candidates', loc='upper left', bbox_to_anchor=(1.05, 1.0), fontsize='small')

# Set a viewing angle
ax.view_init(elev=20, azim=45)

# Enable the grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()