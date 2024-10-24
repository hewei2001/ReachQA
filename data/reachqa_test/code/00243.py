import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Original exoplanetary data
exoplanets = ['Zeta Aurigae b', 'Proxima C. d', 'Gliese 581 g', 'Tau Ceti e', 'Kepler-442 b', 'Trappist-1 e']
average_temperatures = np.array([15, -25, 10, 22, 5, -60])  # °C
oxygen_levels = np.array([21, 18, 15, 23, 19, 16])  # %
distances_from_star = np.array([1.0, 0.2, 0.13, 0.55, 0.99, 0.05])  # AU
habitability_index = np.array([85, 70, 60, 90, 75, 65])  # Arbitrary index

# Additional data for subplot: hypothetical sizes and historical habitability
exoplanet_sizes = np.array([0.8, 1.0, 0.95, 1.1, 0.9, 0.6])  # Earth Masses
habitability_over_time = {
    'Zeta Aurigae b': [80, 82, 84, 85],
    'Proxima C. d': [65, 68, 69, 70],
    'Gliese 581 g': [58, 59, 60, 60],
    'Tau Ceti e': [85, 87, 89, 90],
    'Kepler-442 b': [72, 73, 74, 75],
    'Trappist-1 e': [63, 64, 64, 65]
}
years = [2020, 2021, 2022, 2023]

# Setup figure with subplots
fig = plt.figure(figsize=(16, 8))

# 3D scatter plot
ax1 = fig.add_subplot(121, projection='3d')
bubble_sizes = habitability_index * 10
scatter = ax1.scatter(
    average_temperatures, oxygen_levels, distances_from_star,
    s=bubble_sizes, c=habitability_index, cmap='plasma', alpha=0.8, edgecolors='w'
)
ax1.set_xlabel('Avg Surface Temp (°C)', labelpad=10)
ax1.set_ylabel('Oxygen Levels (%)', labelpad=10)
ax1.set_zlabel('Distance from Star (AU)', labelpad=10)
ax1.set_title('Galactic Exploration Mission:\nHabitability Conditions in Exoplanet Systems', pad=20)
cbar = plt.colorbar(scatter, ax=ax1, shrink=0.6, aspect=10)
cbar.set_label('Potential Habitability Index', fontsize=12)
for i, exoplanet in enumerate(exoplanets):
    ax1.text(average_temperatures[i], oxygen_levels[i], distances_from_star[i], exoplanet,
             fontsize=9, ha='right', va='bottom')
ax1.view_init(elev=25, azim=135)

# 2D line plot for habitability index over time
ax2 = fig.add_subplot(122)
for planet, indices in habitability_over_time.items():
    ax2.plot(years, indices, marker='o', label=planet)
ax2.set_xlabel('Year')
ax2.set_ylabel('Habitability Index')
ax2.set_title('Habitability Index Evolution Over Time')
ax2.legend(title="Exoplanets", fontsize=8, loc='best')
ax2.grid(True)

# Ensure layout does not overlap
plt.tight_layout()

# Display the plot
plt.show()