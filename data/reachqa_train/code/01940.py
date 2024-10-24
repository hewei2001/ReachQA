import matplotlib.pyplot as plt
import numpy as np

# Define plant species and ecological zones
plant_species = ['Oak', 'Pine', 'Cedar', 'Maple', 'Birch', 'Redwood', 'Bamboo', 'Cactus', 'Fern', 'Moss']
ecological_zones = ['Wetlands', 'Grasslands', 'Tropical Forests', 'Montane Zones', 'Desert Areas']

# Artificial data: Number of observations of each species in the respective zones
observations = np.array([
    [50, 10, 5, 2, 0],  # Oak
    [5, 45, 20, 30, 0],  # Pine
    [0, 5, 10, 60, 0],  # Cedar
    [40, 15, 5, 5, 0],  # Maple
    [60, 5, 0, 0, 0],   # Birch
    [0, 0, 0, 0, 70],   # Redwood
    [20, 10, 0, 0, 60], # Bamboo
    [0, 0, 0, 0, 100],  # Cactus
    [10, 20, 40, 10, 0],# Fern
    [30, 30, 5, 5, 0]   # Moss
])

# Create the heat map
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(observations, cmap='YlGn', aspect='auto', interpolation='nearest')

# Add color bar
cbar = fig.colorbar(cax)
cbar.set_label('Number of Observations', fontsize=10)

# Set labels and title
ax.set_xticks(np.arange(len(ecological_zones)))
ax.set_yticks(np.arange(len(plant_species)))
ax.set_xticklabels(ecological_zones, rotation=45, ha="right", fontsize=10)
ax.set_yticklabels(plant_species, fontsize=10)
ax.set_title('Species Distribution in Green Haven National Park', fontsize=14, fontweight='bold', pad=20)

# Annotate each cell with the number of observations
for i in range(len(plant_species)):
    for j in range(len(ecological_zones)):
        ax.text(j, i, observations[i, j], va='center', ha='center', color='black', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()