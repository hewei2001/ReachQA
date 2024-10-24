import matplotlib.pyplot as plt
import numpy as np

# Define the biomes and indicators
biomes = ['Tropical Rainforest', 'Desert', 'Grassland', 'Temperate Forest', 'Tundra']
indicators = ['Biodiversity', 'Water Availability', 'Carbon Sequestration', 'Human Impact', 'Climate Stability']

# Sustainability indicator scores for each biome
data = np.array([
    [95, 80, 90, 30, 85],  # Tropical Rainforest
    [40, 20, 45, 60, 25],  # Desert
    [60, 65, 50, 55, 60],  # Grassland
    [80, 75, 85, 45, 70],  # Temperate Forest
    [30, 55, 65, 50, 40]   # Tundra
])

# Number of variables
num_vars = len(indicators)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so complete the loop
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Colors for each biome
colors = ['b', 'orange', 'green', 'red', 'purple']

# Draw one line per biome and fill the area
for idx, (d, label) in enumerate(zip(data, biomes)):
    ax.plot(angles, d, linewidth=2, linestyle='solid', label=label, color=colors[idx])
    ax.fill(angles, d, alpha=0.25, color=colors[idx])

# Add attribute labels to the plot
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(indicators, fontsize=12)

# Adjust legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
plt.title('Sustainability Profiles of Earth\'s Biomes', size=16, color='navy', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()