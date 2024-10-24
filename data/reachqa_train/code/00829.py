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

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the box chart with additional properties
boxes = ax.boxplot(park_sizes, patch_artist=True, notch=True, vert=True,
                   boxprops=dict(color='black', linewidth=1.5),
                   medianprops=dict(color='red', linewidth=2),
                   whiskerprops=dict(color='black', linewidth=1.5),
                   capprops=dict(color='black', linewidth=1.5),
                   flierprops=dict(marker='o', color='black', alpha=0.5, markersize=8))

# Set the color for each box using different shades
colors = ['#77BFC7', '#FFB6C1', '#FFDEAD', '#B0E57C', '#FFCCCB']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Overlay jittered scatter plot
for i, data in enumerate(park_sizes, start=1):
    y = np.array(data)
    x = np.random.normal(i, 0.04, size=len(y))  # jitter x position
    ax.scatter(x, y, alpha=0.6, edgecolor='w', s=80, label=f'{districts[i-1]} Points' if i == 1 else "")

# Customize the plot with titles and labels
ax.set_title('Urban Green Spaces: Distribution of Park Sizes\nAcross Districts in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Districts', fontsize=12)
ax.set_ylabel('Park Sizes (Acres)', fontsize=12)
ax.set_xticks(np.arange(1, len(districts) + 1))
ax.set_xticklabels(districts, rotation=30, ha='right', fontsize=10)

# Add grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Annotate with additional statistical information
mean_sizes = [np.mean(d) for d in park_sizes]
for i, mean in enumerate(mean_sizes, start=1):
    ax.axhline(mean, ls='--', color=colors[i-1], alpha=0.7, linewidth=1.5, label=f'{districts[i-1]} Mean' if i == 1 else "")

# Adding an annotation with a small background color box
ax.text(0.95, 0.02, "Promoting equitable access\nto green spaces in urban areas.",
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

# Automatically adjust the subplot params for better layout
plt.tight_layout()

# Add legend
ax.legend(loc='upper left', fontsize=9)

# Show the plot
plt.show()