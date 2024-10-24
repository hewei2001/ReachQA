import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define rainforest layers and corresponding data
layers = ['Ground Layer', 'Understory', 'Canopy', 'Emergent']
layer_heights = np.array([1, 10, 30, 50])  # Height of each layer in meters
species_diversity = np.array([250, 180, 320, 120])  # Number of species
sunlight_exposure = np.array([5, 15, 65, 90])  # Sunlight exposure percentage
biomass_density = np.array([700, 400, 900, 300])  # Biomass density units

# Normalize colors based on sunlight exposure
colors = sunlight_exposure / sunlight_exposure.max()

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the bubble plot
sc = ax.scatter(species_diversity, layer_heights, sunlight_exposure,
                s=biomass_density / 2, c=colors, cmap='YlGn', alpha=0.8, edgecolors='black', linewidth=0.5)

# Set a viewing angle for the plot
ax.view_init(elev=25, azim=135)

# Set title and axis labels
ax.set_title('Biodiversity Across Rainforest Layers\nDiversity, Height, and Sunlight Exposure', fontsize=16, pad=20)
ax.set_xlabel('Species Diversity (Count)', fontsize=12, labelpad=10)
ax.set_ylabel('Layer Height (m)', fontsize=12, labelpad=10)
ax.set_zlabel('Sunlight Exposure (%)', fontsize=12, labelpad=10)

# Annotate each layer for clarity
for i, layer in enumerate(layers):
    ax.text(species_diversity[i], layer_heights[i], sunlight_exposure[i] + 5, layer, fontsize=10, fontweight='bold', color='darkgreen')

# Add a color bar to represent sunlight exposure levels
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Sunlight Exposure (%)', fontsize=12)

# Legend to represent biomass density
biomass_sizes = [300, 400, 700, 900]
biomass_labels = [plt.Line2D([0], [0], marker='o', color='w', label=f'{v} Biomass Units',
                             markerfacecolor='forestgreen', markersize=np.sqrt(v / 2), alpha=0.5)
                  for v in biomass_sizes]
ax.legend(title='Biomass Density', handles=biomass_labels, loc='upper right', fontsize=9)

# Automatically adjust subplot parameters for better layout
plt.tight_layout()

# Display the chart
plt.show()