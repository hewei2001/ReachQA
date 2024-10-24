import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data representing 10 forest sites
forest_sites = np.array(['Site A', 'Site B', 'Site C', 'Site D', 'Site E', 
                         'Site F', 'Site G', 'Site H', 'Site I', 'Site J'])

# Forest density (trees per hectare)
forest_density = np.array([120, 150, 170, 200, 190, 160, 180, 145, 175, 155])

# Number of conservation initiatives
conservation_initiatives = np.array([3, 5, 7, 4, 6, 8, 5, 7, 6, 4])

# Species richness (number of species)
species_richness = np.array([25, 30, 35, 28, 32, 40, 30, 38, 33, 29])

# Area of forest sites (in hectares) for bubble size
forest_area = np.array([250, 300, 350, 280, 320, 400, 300, 380, 330, 290])

# Conservation effectiveness (a calculated metric)
conservation_effectiveness = species_richness / conservation_initiatives

# Initialize the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={})

# Convert ax1 to a 3D plot
ax1 = fig.add_subplot(121, projection='3d')

# Plot the 3D scatter with bubble sizes on the first subplot
sc1 = ax1.scatter(forest_density, conservation_initiatives, species_richness, 
                 s=forest_area * 0.5, c=species_richness, cmap='viridis', 
                 alpha=0.7, edgecolor='k')

# Add labels for each point in the first subplot
for i, txt in enumerate(forest_sites):
    ax1.text(forest_density[i], conservation_initiatives[i], species_richness[i], 
             txt, size=10, zorder=1, color='black')

# Add colorbar to the first subplot
colorbar1 = fig.colorbar(sc1, ax=ax1, pad=0.1)
colorbar1.set_label('Species Richness', fontsize=12)

# Set axis labels and title for the first subplot
ax1.set_xlabel('Forest Density (trees/ha)', fontsize=12)
ax1.set_ylabel('Conservation Initiatives', fontsize=12)
ax1.set_zlabel('Species Richness', fontsize=12)
ax1.set_title('Impact of Forest Density and Conservation Efforts\non Species Richness', fontsize=14, fontweight='bold')

# Adjust view angle for the first subplot
ax1.view_init(elev=30, azim=45)

# Plot a 2D bar chart on the second subplot
ax2.barh(forest_sites, conservation_effectiveness, color='lightseagreen')
ax2.set_xlabel('Conservation Effectiveness (Richness/Initiatives)', fontsize=12)
ax2.set_title('Conservation Effectiveness Across Forest Sites', fontsize=14, fontweight='bold')

# Ensure the layout is tight and elements do not overlap
plt.tight_layout()

# Display the plots
plt.show()