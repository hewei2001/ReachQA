import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Expanded dataset for species
species = [
    'Urban Fox', 'Park Deer', 'City Squirrel', 'Pigeon', 'Mallard Duck',
    'Garden Snake', 'Urban Hawk', 'Raccoon', 'House Sparrow', 'Cottontail Rabbit',
    'Feral Cat', 'Coyote', 'Bat', 'Robin', 'Goldfinch', 'Turtle'
]

# Number of sightings (per year)
sightings = np.array([150, 80, 120, 200, 60, 50, 30, 70, 180, 90, 110, 40, 25, 160, 140, 55])

# Area of parks (in hectares)
park_area = np.array([50, 75, 60, 55, 40, 30, 45, 70, 65, 50, 80, 35, 20, 45, 55, 60])

# Average size of the species (in centimeters)
species_size = np.array([60, 150, 25, 35, 45, 90, 100, 65, 20, 50, 40, 160, 8, 30, 13, 25])

# Additional variable: Average lifespan (years)
lifespan = np.array([6, 10, 5, 3, 7, 9, 14, 3, 2, 6, 15, 12, 5, 4, 3, 50])

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Bubble sizes and colors encoding
bubble_sizes = sightings * 5
colors = lifespan

# 3D scatter plot
scatter = ax.scatter(park_area, species_size, sightings, 
                     s=bubble_sizes, c=colors, cmap='plasma', 
                     alpha=0.8, edgecolor='k', linewidth=0.5)

# Color bar for lifespan
cbar = plt.colorbar(scatter)
cbar.set_label('Average Lifespan (years)', rotation=270, labelpad=15)

# Setting axis labels
ax.set_xlabel('Park Area (hectares)', labelpad=10)
ax.set_ylabel('Average Species Size (cm)', labelpad=10)
ax.set_zlabel('Number of Sightings', labelpad=10)

# Title
ax.set_title('Complex Study on Urban Wildlife Sightings\nIntegrating Park Size, Species Size, and Lifespan', 
             fontsize=15, fontweight='bold', pad=20)

# Annotating each point with species names
for i, sp in enumerate(species):
    ax.text(park_area[i], species_size[i], sightings[i], sp, fontsize=8, ha='right')

# Enhance the view
ax.view_init(elev=30, azim=40)

# Use tight layout for optimal spacing
plt.tight_layout()

# Show plot
plt.show()