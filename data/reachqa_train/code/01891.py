import matplotlib.pyplot as plt
import numpy as np

# Data representing sightings for different bird species over four seasons
sparrows = [15, 18, 20, 22, 17, 21, 19, 23, 24, 20, 18, 25]
pigeons = [30, 28, 35, 33, 32, 29, 34, 36, 38, 31, 35, 37]
woodpeckers = [5, 7, 8, 6, 9, 10, 12, 11, 7, 9, 8, 10]
finches = [12, 14, 16, 13, 15, 14, 17, 18, 16, 19, 15, 20]

# Combine data into a list for easier plotting
bird_data = [sparrows, pigeons, woodpeckers, finches]
species = ['Sparrows', 'Pigeons', 'Woodpeckers', 'Finches']

# Create figure and axis with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal box plot with additional enhancements
box = ax.boxplot(bird_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightblue', color='navy'),
                 whiskerprops=dict(color='navy', linestyle='--'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkred', linewidth=2),
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 meanline=True, showmeans=True, meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black', markersize=7))

# Customize the appearance of each box
colors = ['#A3C1AD', '#C5DCA0', '#F2E394', '#F9AA7D']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Overlay data points for enhanced detail
for i, data in enumerate(bird_data):
    y = np.random.normal(i + 1, 0.04, size=len(data))
    ax.plot(data, y, 'o', alpha=0.3, color='gray')

# Add axis labels and title
ax.set_xlabel('Number of Sightings', fontsize=12)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(species)
ax.set_title('Bird Species Sightings Across Seasons\nGreenfield Urban Park', fontsize=16, fontweight='bold', pad=20)

# Add a legend to identify the mean
ax.legend([box["means"][0]], ['Mean Value'], loc='upper right', fontsize=10)

# Add a grid for easier reading
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Highlight Interquartile Range (IQR) with annotations
for i, data in enumerate(bird_data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    IQR = q3 - q1
    ax.annotate(f'IQR = {IQR:.1f}', xy=(0.05, i + 1), xycoords=('axes fraction', 'data'),
                ha='center', va='center', fontsize=10, color='darkgreen')

# Automatically adjust layout to fit elements neatly
plt.tight_layout()

# Display the plot
plt.show()