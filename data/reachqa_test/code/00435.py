import matplotlib.pyplot as plt
import numpy as np

# Define the expanded rainforest regions and animal classes
rainforest_regions = [
    'Amazon', 'Congo Basin', 'Southeast Asia',
    'Australasia', 'Central America', 'Madagascar'
]
animal_classes = ['Amphibians', 'Birds', 'Mammals', 'Reptiles', 'Insects']

# Adjusted biodiversity density values for more variability
biodiversity_data = np.array([
    [220, 340, 270, 180, 580],  # Amazon
    [190, 300, 250, 160, 570],  # Congo Basin
    [150, 320, 210, 140, 560],  # Southeast Asia
    [110, 290, 160, 110, 510],  # Australasia
    [170, 315, 265, 150, 595],  # Central America
    [145, 305, 215, 130, 540]   # Madagascar
])

# Calculate average biodiversity density for each region
average_density = biodiversity_data.mean(axis=1)

# Create figure and axes for multiple subplots
fig, ax = plt.subplots(2, 1, figsize=(12, 12), gridspec_kw={'height_ratios': [3, 1]})

# Plot the biodiversity heatmap
heatmap = ax[0].imshow(biodiversity_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')
cbar = plt.colorbar(heatmap, ax=ax[0])
cbar.set_label('Density of Population (per sq km)', fontsize=12)

# Set ticks and labels for axes
ax[0].set_xticks(np.arange(len(animal_classes)))
ax[0].set_xticklabels(animal_classes, fontsize=12, rotation=45, ha='right')
ax[0].set_yticks(np.arange(len(rainforest_regions)))
ax[0].set_yticklabels(rainforest_regions, fontsize=12)

# Title and labels
ax[0].set_title("Biodiversity Distribution in Various Rainforest Regions\nAcross Multiple Animal Classes",
                fontsize=16, weight='bold', pad=15)
ax[0].set_xlabel("Animal Classes", fontsize=14)
ax[0].set_ylabel("Rainforest Regions", fontsize=14)

# Annotate each cell with the corresponding value, with adjusted font size for better visibility
for i in range(biodiversity_data.shape[0]):
    for j in range(biodiversity_data.shape[1]):
        ax[0].text(j, i, f'{biodiversity_data[i, j]}', ha='center', va='center', color='black', fontsize=11)

# Plot the average biodiversity density with transparency and spacing between bars
ax[1].bar(rainforest_regions, average_density, color='skyblue', alpha=0.8, width=0.5)
ax[1].set_title("Average Biodiversity Density per Region", fontsize=14, weight='bold')
ax[1].set_ylabel("Average Density (per sq km)", fontsize=12)
ax[1].set_xlabel("Rainforest Regions", fontsize=12)
ax[1].tick_params(axis='x', rotation=45)

# Adjust y-axis to avoid excessive empty space
ax[1].set_ylim(0, max(average_density) * 1.1)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()