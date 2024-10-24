import matplotlib.pyplot as plt
import numpy as np

# Define the species and parks
species = ['Sparrows', 'Hawks', 'Robins']
parks = ['Central Park', 'Urban Gardens', 'Riverside Reserve']

# Create artificial data for the sightings of each species in each park
sparrows_sightings = [30, 28, 32, 31, 29, 27, 33, 34, 30, 29, 30, 31, 32, 28, 29, 34]
hawks_sightings = [5, 6, 7, 4, 5, 6, 7, 8, 5, 4, 6, 7, 8, 5, 5, 6]
robins_sightings = [20, 21, 19, 22, 23, 21, 22, 23, 24, 20, 21, 22, 23, 24, 22, 21]

# Group the data for each park
central_park_data = np.array([sparrows_sightings[:5], hawks_sightings[:5], robins_sightings[:5]]).T
urban_gardens_data = np.array([sparrows_sightings[5:10], hawks_sightings[5:10], robins_sightings[5:10]]).T
riverside_reserve_data = np.array([sparrows_sightings[10:], hawks_sightings[10:], robins_sightings[10:]]).T

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal box plots for each park
bplot1 = ax.boxplot(central_park_data, vert=False, patch_artist=True, positions=np.arange(3)*3, widths=0.6)
bplot2 = ax.boxplot(urban_gardens_data, vert=False, patch_artist=True, positions=np.arange(3)*3 + 1, widths=0.6)
bplot3 = ax.boxplot(riverside_reserve_data, vert=False, patch_artist=True, positions=np.arange(3)*3 + 2, widths=0.6)

# Customize the appearance
colors = ['lightblue', 'lightgreen', 'lightcoral']
for bplot, color in zip([bplot1, bplot2, bplot3], colors):
    for patch in bplot['boxes']:
        patch.set_facecolor(color)
    for median in bplot['medians']:
        median.set(color='darkred', linewidth=2)

# Add legend
ax.legend([bplot1["boxes"][0], bplot2["boxes"][0], bplot3["boxes"][0]], parks, loc='upper right', title="Parks")

# Set title and labels
ax.set_title('Urban Birdwatching Trends:\nSightings Across Parks', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Sightings', fontsize=14)
ax.set_ylabel('Bird Species', fontsize=14)
ax.set_yticks([0.5, 3.5, 6.5])
ax.set_yticklabels(species)

# Add grid for readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()