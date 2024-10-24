import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the data
biodiversity_data = np.array([
    [0.85, 0.75, 0.60, 0.70, 0.65],  # South America
    [0.78, 0.50, 0.55, 0.68, 0.60],  # Africa
    [0.82, 0.55, 0.58, 0.75, 0.68],  # Asia
    [0.80, 0.65, 0.62, 0.72, 0.66]   # Oceania
])

# Define the ecosystems and regions
ecosystems = ["Tropical\nRainforest", "Desert", "Temperate\nForest", "Coral\nReef", "Wetlands"]
regions = ["South America", "Africa", "Asia", "Oceania"]

# Average biodiversity for each region (new data for the subplot)
region_avg = biodiversity_data.mean(axis=1)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), gridspec_kw={'width_ratios': [3, 1]})

# Heatmap
cax = ax1.imshow(biodiversity_data, cmap='RdYlGn', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(cax, ax=ax1, fraction=0.046, pad=0.04)
cbar.set_label('Biodiversity Index', rotation=270, labelpad=20)

# Set ticks and labels for heatmap
ax1.set_xticks(np.arange(len(ecosystems)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(ecosystems, rotation=45, ha="right", fontsize=10)
ax1.set_yticklabels(regions, fontsize=10)
ax1.set_title('Biodiversity Index Across\nEcosystems and Regions', pad=20)

# Annotate cells
for i in range(len(regions)):
    for j in range(len(ecosystems)):
        value = biodiversity_data[i, j]
        color = 'white' if value < 0.65 else 'black'
        ax1.text(j, i, f'{value:.2f}', ha='center', va='center', color=color)

# Plot average biodiversity index for each region as a bar chart
ax2.barh(regions, region_avg, color='lightblue', edgecolor='black')
ax2.set_xlim(0, 1)
ax2.set_xlabel('Average Index')
ax2.set_title('Average Biodiversity\nby Region')

# Add patches/markers to highlight regions of interest in the heatmap
highlight_index = np.argmax(biodiversity_data)
highlight_x, highlight_y = np.unravel_index(highlight_index, biodiversity_data.shape)
highlight_patch = mpatches.Circle((highlight_y, highlight_x), 0.3, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
ax1.add_patch(highlight_patch)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()