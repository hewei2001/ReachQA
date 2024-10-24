import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Define regions and languages data
regions = ['N. America', 'S. America', 'Europe', 'Africa', 'Asia', 'Oceania', 'Mid. East']
languages_count = [
    [100, 200, 50, 2000, 2300, 1300, 250],    # Scenario A
    [120, 220, 70, 2100, 2400, 1400, 300],    # Scenario B
    [90, 150, 45, 2050, 2250, 1250, 280],     # Scenario C
    [110, 180, 65, 2150, 2350, 1350, 270]     # Scenario D
]

# Convert data to numpy array for heatmap
languages_array = np.array(languages_count)
total_per_scenario = languages_array.sum(axis=1)

# Set up the matplotlib figure with a different subplot for detailed comparison
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Create a colormap
cmap = plt.cm.viridis

# Create the heat map using imshow
heatmap = ax.imshow(languages_array, cmap=cmap, aspect='auto', interpolation='nearest')

# Add color bar
cbar = plt.colorbar(heatmap, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Number of Languages', fontsize=12)

# Title and labels with multiple lines for long texts
ax.set_title("Mapping the Mosaic:\nHeat Map of Global Languages Diversity", fontsize=16, fontweight='bold')
ax.set_xlabel('World Regions', fontsize=12)
ax.set_ylabel('Hypothetical Scenarios', fontsize=12)

# Set ticks and labels
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha="right", fontsize=10)
ax.set_yticks(np.arange(languages_array.shape[0]))
ax.set_yticklabels(['Scenario A', 'Scenario B', 'Scenario C', 'Scenario D'])

# Add gridlines for better separation
ax.grid(False)  # To disable the default grid
ax.set_xticks(np.arange(languages_array.shape[1]+1)-.5, minor=True)
ax.set_yticks(np.arange(languages_array.shape[0]+1)-.5, minor=True)
ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)

# Annotate each cell with its value and percentage of the total
for i in range(languages_array.shape[0]):
    for j in range(languages_array.shape[1]):
        value = languages_array[i, j]
        percentage = (value / total_per_scenario[i]) * 100
        color = 'white' if cmap(value/np.max(languages_array))[:3] < (0.5, 0.5, 0.5) else 'black'
        ax.text(j, i, f"{value}\n({percentage:.1f}%)", ha='center', va='center', color=color, fontsize=9)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()