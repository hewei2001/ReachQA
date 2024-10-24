import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for number of bird species observed in each park
park1_species = [8, 12, 15, 9, 11, 14, 10, 9, 13, 14, 16]
park2_species = [6, 9, 8, 7, 6, 10, 11, 12, 10]
park3_species = [15, 18, 14, 19, 21, 17, 16, 14, 20]
park4_species = [12, 10, 14, 11, 13, 15, 13, 12]
park5_species = [9, 11, 8, 7, 6, 9, 10, 8, 7, 10]

data = [park1_species, park2_species, park3_species, park4_species, park5_species]
labels = ['Park A', 'Park B', 'Park C', 'Park D', 'Park E']

fig, ax = plt.subplots(figsize=(14, 8))

# Create a violin plot with seaborn
sns.violinplot(data=data, ax=ax, palette='Pastel1', orient='h', inner=None)

# Overlay a boxplot
boxprops = dict(linestyle='-', linewidth=1.5, color='black')
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, labels=labels, boxprops=boxprops)

# Set box colors
colors = sns.color_palette('Pastel1')
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, and medians
for whisker in bp['whiskers']:
    whisker.set(color='grey', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='grey', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkred', linewidth=2)

# Add individual data points with jitter
for i, park_data in enumerate(data):
    x = park_data
    y = np.random.normal(i + 1, 0.04, size=len(x))  # slight jitter in y-axis for clarity
    ax.scatter(x, y, alpha=0.6, color='darkblue', zorder=3, label='Data Points' if i == 0 else "")

# Annotate means with markers
means = [np.mean(park) for park in data]
ax.scatter(means, range(1, len(means) + 1), color='orange', marker='D', s=100, zorder=4, label='Mean')

# Grid for enhanced readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Title and labels
ax.set_title('Bird Species Diversity Across Urban Parks\n(Data Collected in Spring 2023)', fontsize=16, fontweight='bold', color='darkslateblue', loc='left')
ax.set_xlabel('Number of Bird Species', fontsize=12)
ax.set_ylabel('Urban Parks', fontsize=12)

# Legend and layout adjustment
ax.legend(loc='upper right')
plt.tight_layout()

# Display the plot
plt.show()