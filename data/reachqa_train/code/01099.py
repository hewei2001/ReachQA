import matplotlib.pyplot as plt
import numpy as np

# Define art genres and fictional price data (in thousands of USD)
genres = ['Abstract', 'Contemporary', 'Impressionism', 'Modern', 'Pop Art']

# Artworks' price data for each genre
price_data = [
    [12, 15, 14, 18, 20, 19, 13, 22, 25, 18],  # Abstract
    [7, 8, 10, 9, 10, 8, 7, 12, 10, 9],       # Contemporary
    [30, 40, 35, 32, 33, 31, 29, 36, 38, 37], # Impressionism
    [20, 22, 23, 19, 18, 21, 24, 25, 20, 19], # Modern
    [10, 12, 9, 13, 15, 10, 8, 14, 13, 12]    # Pop Art
]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Horizontal box plots
box = ax.boxplot(price_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Define colors for each box
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

# Customize outliers
for flier in box['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# Customize plot elements
ax.set_yticklabels(genres, fontsize=11)
ax.set_xlabel('Price (Thousands USD)', fontsize=12)
ax.set_title('Online Art Marketplace Analysis\nArt Sales Prices by Genre', fontsize=14, fontweight='bold', pad=20)

# Add a legend for clarity
custom_legend = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(genres))]
ax.legend(custom_legend, genres, title="Art Genres", loc='upper right', fontsize=10)

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()