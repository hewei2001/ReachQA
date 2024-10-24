import matplotlib.pyplot as plt
import numpy as np

# Define plant species and ecological zones with additional details
plant_species = ['Oak', 'Pine', 'Cedar', 'Maple', 'Birch', 'Redwood', 'Bamboo', 'Cactus', 'Fern', 'Moss']
ecological_zones = ['Wetlands', 'Grasslands', 'Tropical Forests', 'Montane Zones', 'Desert Areas']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Constructing a more complex dataset with seasonal variation
observations = np.array([
    [50, 15, 5, 3, 1],  # Oak
    [10, 50, 25, 30, 0],  # Pine
    [0, 10, 15, 65, 0],  # Cedar
    [45, 20, 10, 10, 0],  # Maple
    [65, 10, 0, 0, 0],   # Birch
    [0, 0, 0, 0, 80],   # Redwood
    [25, 15, 0, 0, 70], # Bamboo
    [0, 0, 0, 0, 110],  # Cactus
    [15, 25, 45, 15, 0],# Fern
    [35, 35, 10, 10, 0], # Moss
    [55, 20, 8, 5, 2],
    [15, 55, 30, 35, 0],
    [5, 15, 25, 70, 0],
    [50, 25, 15, 15, 0],
    [70, 15, 0, 0, 0],
    [5, 0, 0, 0, 85],
    [30, 20, 5, 5, 75],
    [0, 0, 0, 0, 120],
    [20, 30, 50, 20, 5],
    [40, 40, 15, 15, 0],
    [60, 25, 10, 7, 3],
    [20, 60, 35, 40, 5],
    [10, 20, 35, 75, 5],
    [55, 30, 20, 20, 5],
    [75, 20, 5, 0, 5],
    [10, 5, 5, 0, 90],
    [35, 25, 10, 10, 80],
    [5, 0, 5, 0, 130],
    [25, 35, 55, 25, 10],
    [45, 45, 20, 20, 5],
    [65, 30, 15, 10, 5],
    [25, 65, 40, 45, 10],
    [15, 25, 45, 80, 10],
    [60, 35, 25, 25, 10],
    [80, 25, 10, 5, 10],
    [15, 10, 10, 5, 95],
    [40, 30, 15, 15, 85],
    [10, 5, 10, 5, 140],
    [30, 40, 60, 30, 15],
    [50, 50, 25, 25, 10]
])

# Reshape observations to include seasonal data
observations = observations.reshape((4, len(plant_species), len(ecological_zones)))

# Create the heatmap and additional line plot
fig, axs = plt.subplots(5, 1, figsize=(12, 20), gridspec_kw={'height_ratios': [3, 3, 3, 3, 1]})

# Generate heatmaps for each season
for idx, season in enumerate(seasons):
    cax = axs[idx].imshow(observations[idx], cmap='YlGn', aspect='auto', interpolation='nearest')
    axs[idx].set_xticks(np.arange(len(ecological_zones)))
    axs[idx].set_yticks(np.arange(len(plant_species)))
    axs[idx].set_xticklabels(ecological_zones, rotation=45, ha="right", fontsize=10)
    axs[idx].set_yticklabels(plant_species, fontsize=10)
    axs[idx].set_title(f'Species Distribution in Green Haven National Park ({season})', fontsize=14, fontweight='bold', pad=20)

    # Annotate each cell with the number of observations
    for i in range(len(plant_species)):
        for j in range(len(ecological_zones)):
            axs[idx].text(j, i, observations[idx, i, j], va='center', ha='center', color='black', fontsize=9)
    
    # Add color bar for each heatmap
    cbar = fig.colorbar(cax, ax=axs[idx])
    cbar.set_label('Number of Observations', fontsize=10)

# Create the line plot for total observations across all zones and seasons
total_observations = observations.sum(axis=2).sum(axis=0)
axs[-1].plot(plant_species, total_observations, marker='o', linestyle='-', color='b')
axs[-1].set_title('Total Observations Across All Zones and Seasons', fontsize=12, fontweight='bold')
axs[-1].set_xlabel('Plant Species', fontsize=10)
axs[-1].set_ylabel('Total Observations', fontsize=10)
axs[-1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()