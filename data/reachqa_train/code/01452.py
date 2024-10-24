import matplotlib.pyplot as plt
import numpy as np

# Define the biomes and their attributes
categories = ['Biodiversity', 'Climatic Resilience', 'Soil Fertility', 'Water Availability', 
              'Carbon Sequestration', 'Human Impact Resilience']
n_categories = len(categories)

# Data for each biome (fictional but logical for each type)
forest = [9, 8, 7, 8, 9, 6]
desert = [4, 9, 3, 2, 2, 8]
grassland = [7, 6, 6, 5, 6, 5]
wetland = [8, 7, 8, 9, 7, 4]
tundra = [5, 8, 4, 3, 8, 6]

# Combine all data
data = np.array([forest, desert, grassland, wetland, tundra])
labels = ['Forest', 'Desert', 'Grassland', 'Wetland', 'Tundra']

# Prepare angles for the radar chart
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
data = np.concatenate((data, data[:,[0]]), axis=1)  # close the loop
angles += angles[:1]  # complete the loop for radar plot

# Create radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Function to plot each biome
def plot_radar(ax, data, colors):
    for idx, d in enumerate(data):
        ax.fill(angles, d, color=colors[idx], alpha=0.2, label=labels[idx])
        ax.plot(angles, d, color=colors[idx], linewidth=2)

# Define a color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the data
plot_radar(ax, data, colors)

# Add labels and titles
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')
ax.set_yticklabels([])  # Hide y-tick labels
ax.set_title('Biome Strength Analysis:\nUnderstanding the Adaptive Characteristics', size=16, fontweight='bold', pad=40)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()