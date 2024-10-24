import matplotlib.pyplot as plt
import numpy as np

# Updated ecosystems data
ecosystems = [
    'Amazon Rainforest', 'Coral Reefs', 'Deep Sea', 'Alpine Meadows', 
    'Wetlands', 'Savanna', 'Temperate Forests', 'Tundra', 'Mangroves', 'Grasslands'
]
unique_species_counts = [390, 230, 150, 80, 110, 200, 170, 50, 130, 90]
species_variability = [20, 15, 10, 5, 12, 18, 13, 8, 11, 9]  # Added variability as standard deviation

# Additional data dimension - species categories (simple split into two for demonstration)
species_categories = np.array([
    [250, 140], [140, 90], [100, 50], [55, 25], [70, 40],
    [120, 80], [110, 60], [30, 20], [90, 40], [55, 35]
])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Bar colors and patterns for visual distinction
colors = ['#4CAF50', '#FFA07A', '#87CEEB', '#FFD700', '#8FBC8F', 
          '#E6E6FA', '#FF6347', '#00FA9A', '#8A2BE2', '#D2691E']
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

# Positions for bars
positions = np.arange(len(ecosystems))

# Plotting stacked bar chart with error bars
for i in range(species_categories.shape[1]):
    bars = ax.barh(
        positions, species_categories[:, i], left=np.sum(species_categories[:, :i], axis=1),
        color=colors, edgecolor='black', height=0.6, hatch=hatches[i],
        xerr=species_variability if i == 1 else None, capsize=5, label=f'Species Category {i+1}'
    )

# Set the y-ticks to the ecosystem names
ax.set_yticks(positions)
ax.set_yticklabels(ecosystems, fontsize=11)

# Add title and labels
ax.set_title('Biodiversity Richness and Variability\nAcross Diverse Ecosystems', 
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Number of Unique Species', fontsize=14, labelpad=15)
ax.set_ylabel('Ecosystems', fontsize=14, labelpad=15)

# Add grid and annotations
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate each bar with the total number of species
for i in range(len(positions)):
    total = sum(species_categories[i])
    ax.text(total + 10, positions[i], f'{total}', va='center', ha='left', 
            fontsize=11, fontweight='bold', color='black')

# Add legend to distinguish between species categories
ax.legend(title='Species Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()