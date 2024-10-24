import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define species types and their corresponding data
species_names = ['Roseus Majestica', 'Sunbloom Radiant', 'Willow Whisperer', 
                 'Oak Heartbound', 'Skywing Faera', 'Moonlight Howler']

# Assign data points for each species: [longitude, latitude, population, impact]
species_data = [
    [30, 40, 300, 150],  # Roseus Majestica
    [50, 20, 150, 100],  # Sunbloom Radiant
    [60, 45, 400, 250],  # Willow Whisperer
    [70, 55, 200, 200],  # Oak Heartbound
    [35, 50, 350, 350],  # Skywing Faera
    [45, 25, 280, 300]   # Moonlight Howler
]

# Extract individual lists from the data
longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

# Define colors for each species
colors = ['#FF6347', '#FFD700', '#8B4513', '#32CD32', '#4169E1', '#9370DB']

# Create the figure and a 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot each species as a scatter point in 3D space
for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=colors[i], label=species, alpha=0.6, edgecolors='k')

# Set labels and title for the plot
ax.set_xlabel('Longitude', fontsize=10)
ax.set_ylabel('Latitude', fontsize=10)
ax.set_zlabel('Population (Thousands)', fontsize=10)
ax.set_title('Biodiversity Interaction in TerraLuna\nUnderstanding Flora and Fauna Dynamics', fontsize=14, fontweight='bold', pad=20)

# Add a legend
ax.legend(title="Species Types", loc='upper left', fontsize=10, title_fontsize='11', bbox_to_anchor=(1.1, 0.85))

# Adjust the viewing angle for a better visualization
ax.view_init(elev=15, azim=40)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()