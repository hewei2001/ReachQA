import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data for the missions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
mission_years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
distances = np.array([91.7, 41.4, 0, 78.3, 628.7, 1275, 2724, 4347])  # Million km
durations = np.array([6, 7, 0, 9, 14, 36, 84, 150])  # Months

# Normalize the distances for color intensity and durations for bubble size
color_intensity = (distances - np.min(distances)) / (np.max(distances) - np.min(distances))
bubble_sizes = (durations + 1) * 15  # Scaled and offset to prevent zero size

# Create a colormap based on distance from the Sun (shorter distance, brighter color)
colors = plt.cm.plasma(color_intensity)

# Plotting the 3D scatter chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
sc = ax.scatter(mission_years, distances, durations, s=bubble_sizes, c=colors, alpha=0.8, edgecolors='w', linewidth=1)

# Add labels to the plot
for i, planet in enumerate(planets):
    ax.text(mission_years[i], distances[i], durations[i] + 5, planet, fontsize=10, ha='right')

# Set axis labels and title
ax.set_xlabel('Mission Year', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)
ax.set_zlabel('Mission Duration (Months)', fontsize=12)
ax.set_title('Hypothetical Solar System Exploration Missions\nYear, Distance, and Duration', fontsize=14, fontweight='bold', y=1.05)

# Add a color bar to indicate the distance from the Sun
mappable = plt.cm.ScalarMappable(cmap=plt.cm.plasma)
mappable.set_array(distances)
plt.colorbar(mappable, ax=ax, shrink=0.5, aspect=10, label='Relative Distance from the Sun')

# Set viewing angle
ax.view_init(elev=20, azim=60)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()