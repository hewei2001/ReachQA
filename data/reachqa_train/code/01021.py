import matplotlib.pyplot as plt
import numpy as np

# Original data
earth_proximity = [5, 7, 9, 6, 8, 7, 10, 6, 7, 8]
outer_planets = [10, 12, 11, 15, 14, 13, 10, 11, 13, 12]
andromeda_sector = [17, 20, 19, 18, 22, 24, 23, 21, 19, 20]
zeta_quadrant = [8, 9, 10, 9, 12, 11, 13, 11, 10, 11]
galactic_core = [22, 25, 23, 26, 27, 28, 26, 24, 25, 27]

# Related data for the second plot: Complexity Index (hypothetical)
complexity_index = {
    "Earth's Proximity": [2.5, 3.2, 4.1, 3.8, 3.5],
    "Outer Planets": [3.8, 4.5, 4.0, 5.1, 4.7],
    "Andromeda Sector": [5.5, 6.0, 5.7, 5.9, 6.3],
    "Zeta Quadrant": [3.2, 3.5, 3.9, 4.1, 3.8],
    "Galactic Core": [6.2, 6.8, 7.1, 7.4, 7.0]
}

# Setup subplots
fig, axes = plt.subplots(ncols=2, figsize=(15, 6))

# Box plot on the first subplot
data = [earth_proximity, outer_planets, andromeda_sector, zeta_quadrant, galactic_core]
axes[0].boxplot(data, vert=True, patch_artist=True, notch=True,
                boxprops=dict(facecolor='#ccebc5', color='black'),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='blue', linewidth=1.5),
                capprops=dict(color='blue', linewidth=1.5),
                flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none', markeredgecolor='orange'))

# Title and labels for the first plot
axes[0].set_title('Interstellar Language Studies:\nDiversity of Communication Methods Across Galactic Regions', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Galactic Regions', fontsize=10)
axes[0].set_ylabel('Number of Communication Methods', fontsize=10)
axes[0].set_xticklabels(['Earth\'s Proximity', 'Outer Planets', 'Andromeda Sector', 'Zeta Quadrant', 'Galactic Core'], rotation=15)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].annotate('High Diversity in Galactic Core', 
                 xy=(5, 27), 
                 xytext=(3.5, 30), 
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
                 fontsize=10, color='black')

# Bar plot on the second subplot
categories = list(complexity_index.keys())
indices = np.arange(len(categories))
mean_complexity = [np.mean(complexity_index[region]) for region in categories]

axes[1].bar(indices, mean_complexity, color='#8da0cb', edgecolor='black', alpha=0.7)
axes[1].set_title('Complexity Index of Communication Methods\nAcross Galactic Regions', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Galactic Regions', fontsize=10)
axes[1].set_ylabel('Complexity Index', fontsize=10)
axes[1].set_xticks(indices)
axes[1].set_xticklabels(categories, rotation=15)

# Automatically adjust layout
plt.tight_layout()

# Display the plots
plt.show()