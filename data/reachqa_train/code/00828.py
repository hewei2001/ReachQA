import matplotlib.pyplot as plt
import numpy as np

# District names
districts = ['Central', 'Eastside', 'Westend', 'North Hills', 'Southfield']

# Park sizes for each district (in acres)
central_parks = [2, 5, 7, 10, 15, 18, 22, 25, 28, 30]
eastside_parks = [3, 4, 6, 8, 9, 12, 13, 15, 17, 20]
westend_parks = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
north_hills_parks = [1, 3, 4, 6, 8, 11, 14, 18, 19, 22]
southfield_parks = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

# Compile data into a single list
park_sizes = [central_parks, eastside_parks, westend_parks, north_hills_parks, southfield_parks]

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the box chart
boxes = ax.boxplot(park_sizes, patch_artist=True, notch=True, vert=True,
                   boxprops=dict(facecolor='#87CEEB', color='black'),
                   medianprops=dict(color='red'),
                   whiskerprops=dict(color='black'),
                   capprops=dict(color='black'),
                   flierprops=dict(marker='o', color='black', alpha=0.5))

# Set the color for each box
colors = ['#77BFC7', '#FFB6C1', '#FFDEAD', '#B0E57C', '#FFCCCB']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot with titles and labels
ax.set_title('Urban Green Spaces: Distribution of Park Sizes\nAcross Districts in 2023', fontsize=14, fontweight='bold')
ax.set_xlabel('Districts', fontsize=12)
ax.set_ylabel('Park Sizes (Acres)', fontsize=12)
ax.set_xticks(np.arange(1, len(districts) + 1))
ax.set_xticklabels(districts, rotation=30, ha='right')

# Annotate with additional information
ax.text(0.95, 0.02, "Promoting equitable access\nto green spaces in urban areas.",
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

# Adjust the layout to ensure there is no overlap
plt.tight_layout()

# Show the plot
plt.show()