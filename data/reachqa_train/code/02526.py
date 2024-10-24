import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Expanded data set with more flower species
flower_species = [
    'Roses', 'Lilies', 'Sunflowers', 'Daisies', 'Tulips', 
    'Orchids', 'Marigolds', 'Petunias', 'Lavender', 'Lilacs'
]
bee_visitations = np.array([45, 30, 60, 25, 50, 55, 40, 35, 28, 65])  # Visitations per hour
nectar_availability = np.array([7, 5, 8, 4, 6, 9, 3, 8, 6, 7])       # Nectar availability (scale 1-10)
growth_season = np.array([1, 3, 4, 2, 3, 5, 1, 2, 4, 3])             # Growth season (1-5)

colors = ['#e63946', '#f4a261', '#e9c46a', '#2a9d8f', '#264653', 
          '#7f4a54', '#9c6f3b', '#deb887', '#4f6272', '#d4a5a5']
marker_sizes = nectar_availability * 20  # Scale marker sizes by nectar availability

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(nectar_availability, bee_visitations, growth_season, c=colors, s=marker_sizes, edgecolor='k', linewidth=1.5)

# Add annotations for each point
for i, species in enumerate(flower_species):
    ax.text(nectar_availability[i] + 0.1, bee_visitations[i], growth_season[i], species, fontsize=8)

# Customize plot
ax.set_title("Floral Pollination Dynamics:\nBee Visitations Across Flower Species and Growth Seasons", fontsize=14, fontweight='bold')
ax.set_xlabel("Nectar Availability (Scale 1-10)", fontsize=10)
ax.set_ylabel("Bee Visitations per Hour", fontsize=10)
ax.set_zlabel("Growth Season (Scale 1-5)", fontsize=10)
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend using proxy artists for each species
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=8, label=flower_species[i]) for i in range(len(flower_species))]
ax.legend(title='Flower Species', handles=handles, loc='upper left', fontsize=9)

# Adding a secondary 2D plot for comparison: Nectar Availability vs. Average Bee Visitations
plt.figure(figsize=(10, 4))
average_visits_by_nectar = [np.mean(bee_visitations[nectar_availability == n]) for n in range(1, 11)]
plt.plot(range(1, 11), average_visits_by_nectar, marker='o', linestyle='-', color='b', label='Average Bee Visitations')

# Customize secondary plot
plt.title("Average Bee Visitations by Nectar Availability", fontsize=12, fontweight='bold')
plt.xlabel("Nectar Availability (Scale 1-10)", fontsize=10)
plt.ylabel("Average Bee Visitations per Hour", fontsize=10)
plt.xticks(range(1, 11))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper right')

# Adjust layout and display
plt.tight_layout()
plt.show()