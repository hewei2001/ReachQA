import matplotlib.pyplot as plt
import numpy as np

# Define data for each type of green space
parks = {
    'Downtown': [5, 6, 8, 7, 7, 9, 10, 11, 10, 9, 12],
    'Riverside': [7, 8, 9, 10, 9, 11, 13, 14, 15, 14, 15],
    'Uptown': [4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11]
}

community_gardens = {
    'Downtown': [1, 2, 2, 3, 3, 4, 5, 4, 4, 5, 5],
    'Riverside': [2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8],
    'Uptown': [2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 6]
}

green_roofs = {
    'Downtown': [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.1, 1.3, 1.5],
    'Riverside': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2],
    'Uptown': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.8, 0.9, 1.0]
}

# Prepare data for box plots
data_parks = [parks['Downtown'], parks['Riverside'], parks['Uptown']]
data_community_gardens = [community_gardens['Downtown'], community_gardens['Riverside'], community_gardens['Uptown']]
data_green_roofs = [green_roofs['Downtown'], green_roofs['Riverside'], green_roofs['Uptown']]

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Positions for the box plots
positions_parks = np.array(range(len(data_parks))) * 4.0
positions_community_gardens = positions_parks + 1.0
positions_green_roofs = positions_parks + 2.0

# Box plots
ax.boxplot(data_parks, positions=positions_parks, widths=0.6, patch_artist=True, 
           boxprops=dict(facecolor='lightgreen'), medianprops=dict(color='darkgreen'), notch=True)
ax.boxplot(data_community_gardens, positions=positions_community_gardens, widths=0.6, patch_artist=True,
           boxprops=dict(facecolor='khaki'), medianprops=dict(color='goldenrod'), notch=True)
ax.boxplot(data_green_roofs, positions=positions_green_roofs, widths=0.6, patch_artist=True,
           boxprops=dict(facecolor='lightblue'), medianprops=dict(color='navy'), notch=True)

# Axes labels and title
ax.set_xticks(positions_parks + 1.0)
ax.set_xticklabels(['Downtown', 'Riverside', 'Uptown'], fontsize=12)
ax.set_xlabel('Districts', fontsize=12)
ax.set_ylabel('Area (Hectares)', fontsize=12)
ax.set_title('Evolution of Urban Green Spaces (2010-2020)', fontsize=14, fontweight='bold', pad=20)

# Legend
colors = ['lightgreen', 'khaki', 'lightblue']
labels = ['Parks', 'Community Gardens', 'Green Roofs']
patches = [plt.Line2D([0], [0], color=color, marker='o', linestyle='', markersize=15) for color in colors]
ax.legend(patches, labels, loc='upper left', fontsize=11, title='Green Space Types')

# Grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and display
plt.tight_layout()
plt.show()