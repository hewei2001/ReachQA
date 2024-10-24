import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories
categories = ['Species Richness', 'Endemism Rate', 'Conservation Status', 
              'Pollinator Diversity', 'Height Diversity', 'Growth Adaptability']

# Number of variables/categories
num_vars = len(categories)

# Define biodiversity scores for each region (0 to 100 scale)
tropical_rainforest = [90, 80, 70, 95, 85, 90]
temperate_forest = [75, 65, 75, 70, 80, 65]
desert = [45, 50, 60, 40, 30, 50]
grassland = [60, 55, 65, 50, 75, 70]

# Data for radar chart
data = np.array([tropical_rainforest, temperate_forest, desert, grassland])

# Append the first score to each region to close the radar chart
data = np.concatenate((data, data[:,[0]]), axis=1)

# Create angles for the radar chart
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Plotting
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))  # Colormap for variety

# Draw one region at a time
regions = ['Tropical Rainforest', 'Temperate Forest', 'Desert', 'Grassland']
region_colors = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e']

for i, region in enumerate(regions):
    ax.fill(angles, data[i], color=region_colors[i], alpha=0.25)
    ax.plot(angles, data[i], color=region_colors[i], linewidth=2, label=region)
    for j, score in enumerate(data[i]):
        ax.annotate(f'{score}', xy=(angles[j], score + 3), fontsize=9, ha='center', color=region_colors[i])

# Add the labels for each point on the radar chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)

# Enhance the grid
ax.yaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, color='grey', linestyle='-', linewidth=0.5)

# Add title and legend
ax.set_title('Harmony of Nature:\nFlora Biodiversity Across Regions', size=16, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1.2), fontsize=9)

# Automatically adjust subplot params for a better fit
plt.tight_layout()

# Display the plot
plt.show()