import matplotlib.pyplot as plt
import numpy as np

# Define the data: biodiversity index values for each ecosystem in different regions
biodiversity_data = np.array([
    [0.85, 0.75, 0.60, 0.70, 0.65],  # South America
    [0.78, 0.50, 0.55, 0.68, 0.60],  # Africa
    [0.82, 0.55, 0.58, 0.75, 0.68],  # Asia
    [0.80, 0.65, 0.62, 0.72, 0.66]   # Oceania
])

# Define the ecosystems and regions
ecosystems = ["Tropical\nRainforest", "Desert", "Temperate\nForest", "Coral\nReef", "Wetlands"]
regions = ["South America", "Africa", "Asia", "Oceania"]

# Create a figure and a heatmap using imshow
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(biodiversity_data, cmap='YlGn', aspect='auto', interpolation='nearest')

# Add colorbar with proper labeling
cbar = fig.colorbar(cax)
cbar.set_label('Biodiversity Index', rotation=270, labelpad=20)

# Set tick marks and labels
ax.set_xticks(np.arange(len(ecosystems)))
ax.set_yticks(np.arange(len(regions)))
ax.set_xticklabels(ecosystems, rotation=45, ha="right")
ax.set_yticklabels(regions)

# Add title and labels
plt.title('Biodiversity Index Across\nEcosystems and Regions', pad=20)
plt.xlabel('Ecosystems')
plt.ylabel('Geographical Regions')

# Annotate each cell with the biodiversity index value
for i in range(len(regions)):
    for j in range(len(ecosystems)):
        ax.text(j, i, f'{biodiversity_data[i, j]:.2f}', ha='center', va='center', color='black')

# Adjust layout to ensure no overlapping elements
plt.tight_layout()

# Show the plot
plt.show()