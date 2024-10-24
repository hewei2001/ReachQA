import matplotlib.pyplot as plt
import numpy as np

# Fashion categories
fashion_categories = [
    'Galactic Casual', 'Lunar Leisure', 
    'Martian Elegance', 'Astro Adventure', 'Starry Nightwear'
]

# Survey data for each category
space_fashion_ratings = [
    [75, 80, 78, 70, 82, 84, 85, 79, 81, 83, 77, 79, 76],  # Galactic Casual
    [65, 68, 70, 72, 67, 66, 70, 71, 69, 68, 65, 67, 72],  # Lunar Leisure
    [85, 88, 86, 89, 84, 87, 90, 88, 86, 90, 84, 85, 88],  # Martian Elegance
    [80, 82, 79, 78, 81, 83, 82, 80, 81, 82, 79, 81, 84],  # Astro Adventure
    [95, 93, 92, 96, 94, 95, 97, 93, 95, 96, 94, 97, 95]   # Starry Nightwear
]

# Related data for the line plot (average ratings trend over time)
months = np.arange(1, 14)
average_ratings = np.mean(space_fashion_ratings, axis=0)

# Create a figure with 2 subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plotting the box plot in the first subplot
axes[0].boxplot(
    space_fashion_ratings,
    patch_artist=True,
    labels=fashion_categories,
    notch=True,
    vert=False,
    showmeans=True,
    meanprops={"marker": "D", "markerfacecolor": "cyan", "markeredgecolor": "black", "markersize": 8}
)

# Customizing the boxplot with a space-themed color palette
colors = ['#FFD700', '#FF8C00', '#DC143C', '#00CED1', '#8A2BE2']
for patch, color in zip(axes[0].artists, colors):
    patch.set_facecolor(color)

axes[0].set_title("Stellar Outfits: A Survey of Space Fashion Trends", fontsize=16, fontweight='bold', pad=10)
axes[0].set_xlabel('Fashion Ratings (0-100)', fontsize=12)
axes[0].set_ylabel('Space Fashion Categories', fontsize=12)

axes[0].grid(linestyle='--', alpha=0.7, axis='x')

# Add legend to the first subplot
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
axes[0].legend(handles, fashion_categories, title='Fashion Category', loc='lower right', fontsize=10)

# Plotting the line plot in the second subplot
for i, category in enumerate(fashion_categories):
    axes[1].plot(months, space_fashion_ratings[i], label=category, marker='o')

axes[1].plot(months, average_ratings, label='Average Rating', linestyle='--', color='black', linewidth=2)
axes[1].set_title("Ratings Trend Over Time", fontsize=16, fontweight='bold', pad=10)
axes[1].set_xlabel('Month', fontsize=12)
axes[1].set_ylabel('Ratings', fontsize=12)

axes[1].legend(loc='upper right', fontsize=10)
axes[1].grid(linestyle='--', alpha=0.7)

# Automatically adjust the subplot layout
plt.tight_layout()

# Show the plot
plt.show()