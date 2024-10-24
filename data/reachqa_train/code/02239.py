import matplotlib.pyplot as plt
import numpy as np

# Define the biomes
biomes = ['Tropical Rainforest', 'Desert', 'Temperate Forest', 'Tundra', 'Grasslands']

# Height data in centimeters (artificially constructed)
heights_data = [
    [120, 130, 150, 160, 180, 200, 220, 240, 260, 300],  # Tropical Rainforest
    [10, 15, 20, 25, 30, 35, 40, 45, 50, 60],            # Desert
    [60, 70, 75, 80, 85, 90, 95, 100, 110, 120],         # Temperate Forest
    [5, 8, 10, 12, 14, 16, 18, 20, 22, 25],              # Tundra
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]             # Grasslands
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the vertical box plot
ax.boxplot(heights_data, patch_artist=True, notch=True, vert=True, labels=biomes)

# Customize box colors
colors = ['#3E9651', '#FF5733', '#3498DB', '#F1C40F', '#8E44AD']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title("Interdisciplinary Botany Expedition 2050\nPlant Height Distributions Across Different Biomes",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Biomes", fontsize=12)
ax.set_ylabel("Plant Height (cm)", fontsize=12)

# Enhance gridlines for readability
ax.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.7)

# Annotate with additional information
for i, biome in enumerate(biomes):
    ax.text(i + 1, max(heights_data[i]) + 5, f'Max: {max(heights_data[i])} cm', 
            ha='center', fontsize=10, color=colors[i])

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()