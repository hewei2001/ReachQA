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

# Plotting the horizontal box plot
plt.figure(figsize=(14, 8))
box = plt.boxplot(
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
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing whiskers, caps, and medians
plt.setp(box['whiskers'], color='grey', linestyle='-')
plt.setp(box['caps'], color='grey')
plt.setp(box['medians'], color='black', linewidth=2)

# Add titles and labels
plt.title(
    "Stellar Outfits: A Survey of Space Fashion Trends", 
    fontsize=20, fontweight='bold', pad=20
)
plt.xlabel('Fashion Ratings (0-100)', fontsize=14)
plt.ylabel('Space Fashion Categories', fontsize=14)

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7, axis='x')

# Add legend with custom handles for colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, fashion_categories, title='Fashion Category', loc='lower right', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()