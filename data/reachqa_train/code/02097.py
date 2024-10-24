import matplotlib.pyplot as plt
import numpy as np

# Urban wildlife species
species = ["Sparrow", "Squirrel", "Pigeon", "Crow", "Raccoon"]

# Sound level data (in decibels) for different city parks
# Each sublist represents a city's park sound level measurements for a particular species
sound_levels_park_a = [45, 50, 40, 65, 55]
sound_levels_park_b = [50, 55, 42, 70, 60]
sound_levels_park_c = [48, 52, 41, 68, 58]
sound_levels_park_d = [46, 53, 43, 66, 56]

# Combine sound levels into a nested list for box plotting
sound_data = [sound_levels_park_a, sound_levels_park_b, sound_levels_park_c, sound_levels_park_d]

# Transpose the data to group by species
sound_data_transposed = list(map(list, zip(*sound_data)))

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot horizontal box plots
bp = ax.boxplot(sound_data_transposed, vert=False, patch_artist=True, labels=species, notch=True)

# Customize boxplot colors
colors = ['#76b900', '#ff7f0e', '#1f77b4', '#ff4f79', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and axis labels
ax.set_title('Sound Levels of Urban Wildlife in City Parks\nComparative Analysis', fontsize=16, fontweight='bold')
ax.set_xlabel('Sound Levels (Decibels)', fontsize=12)
ax.set_ylabel('Urban Wildlife Species', fontsize=12)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.5)

# Adjust layout to prevent text overlap and ensure clarity
plt.tight_layout()

# Adding a legend outside the plot for better visibility
legend_labels = ['Park A', 'Park B', 'Park C', 'Park D']
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_patches, legend_labels, title="City Parks", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Display the plot
plt.show()