import matplotlib.pyplot as plt
import numpy as np

# Urban parks and their sizes across decades
parks = ['Central Park', 'Riverside Park', 'Botanical Gardens', 'Sunny Meadows', 'Lakeside Park']
sizes_across_decades = [
    [50, 55, 60, 65, 70],  # Central Park sizes
    [40, 45, 47, 50, 52],  # Riverside Park sizes
    [30, 35, 40, 45, 50],  # Botanical Gardens sizes
    [25, 28, 33, 37, 42],  # Sunny Meadows sizes
    [20, 23, 27, 30, 35]   # Lakeside Park sizes
]

# Plotting the vertical box plot
plt.figure(figsize=(12, 8))
bp = plt.boxplot(sizes_across_decades, labels=parks, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.7),
                 medianprops=dict(color='darkblue', linewidth=2),
                 whiskerprops=dict(color='darkgreen', linestyle='--'),
                 capprops=dict(color='darkgreen'),
                 flierprops=dict(marker='o', color='red', alpha=0.5))

# Customizing the plot
plt.title("A Decade of Green:\nThe Evolution of Urban Parks in GreenVille", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Park Name", fontsize=14)
plt.ylabel("Size (Acres)", fontsize=14)

# Adding annotations for highlighting a trend or interesting point
for i, park in enumerate(parks):
    plt.text(i + 1, sizes_across_decades[i][-1] + 2, f'{sizes_across_decades[i][-1]} Acres',
             ha='center', va='bottom', fontsize=10, color='black')

# Adding grid lines for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text from overlapping
plt.tight_layout()

# Display the plot
plt.show()