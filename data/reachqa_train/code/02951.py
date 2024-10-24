import matplotlib.pyplot as plt
import numpy as np

# Data for monthly visitors (in thousands)
genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Biography', 'Historical', 'Non-Fiction', 'Romance']

visitors_data = [
    [45, 50, 55, 48, 52, 53, 51, 49, 60, 54, 57, 55],  # Science Fiction
    [38, 42, 45, 47, 39, 43, 40, 41, 44, 46, 50, 49],  # Fantasy
    [29, 34, 31, 30, 33, 32, 35, 36, 28, 37, 34, 32],  # Mystery
    [22, 24, 26, 23, 25, 27, 24, 28, 29, 30, 23, 26],  # Biography
    [31, 29, 35, 32, 36, 34, 33, 37, 38, 39, 32, 35],  # Historical
    [47, 45, 48, 46, 50, 49, 52, 51, 53, 54, 50, 49],  # Non-Fiction
    [35, 38, 36, 37, 34, 39, 33, 40, 41, 42, 38, 37],  # Romance
]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
boxprops = dict(linestyle='-', linewidth=1.5, color='black')

ax.boxplot(visitors_data, vert=False, patch_artist=True, notch=True,
           boxprops=dict(facecolor='#7B68EE', color='black', linewidth=1.2),
           whiskerprops=dict(color='black', linewidth=1.2),
           capprops=dict(color='black', linewidth=1.2),
           flierprops=dict(marker='o', color='red', alpha=0.5, markersize=6),
           medianprops=dict(color='gold', linewidth=2))

# Set axis labels and title
ax.set_yticklabels(genres, fontsize=12)
ax.set_xlabel('Monthly Visitors (in Thousands)', fontsize=12)
ax.set_title('Library of Tomorrow: Monthly Visitors by Genre in 2050', fontsize=14, fontweight='bold', pad=15)

# Customize grid
ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()