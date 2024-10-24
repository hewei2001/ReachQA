import matplotlib.pyplot as plt
import numpy as np

# Original Data
park_sizes = np.array([5, 8, 12, 15, 20, 22, 30, 35, 40, 45, 50, 55, 60, 65, 70])
biodiversity_indices = np.array([23, 30, 35, 37, 45, 50, 55, 60, 65, 68, 70, 75, 80, 82, 85])

# Related Data for the new subplot
species_richness = np.array([5, 12, 14, 20, 25, 28, 32, 36, 40, 42, 47, 53, 55, 58, 60])

# Plot configurations
colors = ['green', 'lightgreen', 'forestgreen', 'lime', 'olive', 'darkgreen', 
          'yellowgreen', 'greenyellow', 'seagreen', 'springgreen', 'mediumseagreen', 
          'darkolivegreen', 'lawngreen', 'chartreuse', 'mediumspringgreen']
marker_sizes = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]

# Create a 1x2 subplot layout
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Scatter plot
ax[0].scatter(park_sizes, biodiversity_indices, c=colors, s=marker_sizes, alpha=0.8, edgecolors='black')
z = np.polyfit(park_sizes, biodiversity_indices, 1)
p = np.poly1d(z)
ax[0].plot(park_sizes, p(park_sizes), linestyle='--', color='grey', linewidth=1.5)

ax[0].set_title("Park Sizes vs Biodiversity Index\nA Hypothetical Study", fontsize=14, fontweight='bold')
ax[0].set_xlabel("Park Size (hectares)", fontsize=12)
ax[0].set_ylabel("Biodiversity Index", fontsize=12)
ax[0].grid(True, linestyle='--', alpha=0.5)

legend_labels = [
    'Woodland', 'Wetland', 'Meadow', 'Orchard', 'Natural Grassland',
    'Constructed Wetland', 'Community Garden', 'City Arboretum', 'Bioswale',
    'Native Flora Park', 'Rooftop Gardens', 'Riverbank', 'Perennial Meadow',
    'Botanical Reserve', 'Eco-Park'
]
ax[0].legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label=label,
                                  markerfacecolor=color, markersize=10, markeredgecolor='black') 
                      for label, color in zip(legend_labels, colors)],
             title="Habitat Types", loc='lower right', fontsize=10, title_fontsize='12')

# Second subplot: Bar plot showing species richness
ax[1].bar(park_sizes, species_richness, color='teal', alpha=0.7, edgecolor='black')
ax[1].set_title("Species Richness in Parks", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Park Size (hectares)", fontsize=12)
ax[1].set_ylabel("Species Richness", fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()