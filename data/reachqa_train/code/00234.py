import matplotlib.pyplot as plt

# Refined data for number of bird species observed in each park
park1_species = [8, 12, 15, 9, 11, 14, 10, 9, 13, 14, 16]
park2_species = [6, 9, 8, 7, 6, 10, 11, 12, 10]
park3_species = [15, 18, 14, 19, 21, 17, 16, 14, 20]
park4_species = [12, 10, 14, 11, 13, 15, 13, 12]
park5_species = [9, 11, 8, 7, 6, 9, 10, 8, 7, 10]

# Combine data into a list for plotting
data = [park1_species, park2_species, park3_species, park4_species, park5_species]

# Labels corresponding to each park
labels = ['Park A', 'Park B', 'Park C', 'Park D', 'Park E']

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
boxprops = dict(linestyle='-', linewidth=1.5, color='black')

# Boxplot with horizontal orientation, notches, and custom colors
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, labels=labels, boxprops=boxprops)

# Color each box differently for clarity
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers and medians
for whisker in bp['whiskers']:
    whisker.set(color='grey', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='grey', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkred', linewidth=2)

# Add a grid for enhanced readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set plot title and axis labels
ax.set_title('Bird Species Diversity Across Urban Parks', fontsize=16, fontweight='bold', color='darkslateblue', loc='left')
ax.set_xlabel('Number of Bird Species', fontsize=12)
ax.set_ylabel('Urban Parks', fontsize=12)

# Adjust layout to ensure there is no overlap of elements
plt.tight_layout()

# Display the plot
plt.show()