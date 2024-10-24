import matplotlib.pyplot as plt
import numpy as np

# Data for bee visitations and nectar availability
flower_species = ['Roses', 'Lilies', 'Sunflowers', 'Daisies', 'Tulips']
bee_visitations = np.array([45, 30, 60, 25, 50])  # Bee visitations per hour
nectar_availability = np.array([7, 5, 8, 4, 6])   # Nectar availability (scale 1-10)

# Define color palette for each flower species
colors = ['#e63946', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']
marker_sizes = nectar_availability * 25  # Scale marker sizes by nectar availability

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(nectar_availability, bee_visitations, c=colors, s=marker_sizes, edgecolor='k', linewidth=1.5)

# Add annotations for each point
for i, species in enumerate(flower_species):
    plt.annotate(species, (nectar_availability[i] + 0.1, bee_visitations[i]), fontsize=10)

# Customize plot
plt.title("Floral Pollination Dynamics:\nBee Visitations Across Flower Species", fontsize=14, fontweight='bold')
plt.xlabel("Nectar Availability (Scale 1-10)", fontsize=12)
plt.ylabel("Bee Visitations per Hour", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend using proxy artists for each species
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=10, label=flower_species[i]) for i in range(len(flower_species))]
plt.legend(title='Flower Species', handles=handles, loc='upper left', fontsize=10)

# Adjust layout and display
plt.tight_layout()
plt.show()