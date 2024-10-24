import matplotlib.pyplot as plt
import numpy as np

# Urban wildlife species
species = ["Sparrow", "Squirrel", "Pigeon", "Crow", "Raccoon"]

# Sound level data (in decibels) for different city parks
sound_levels_park_a = [45, 50, 40, 65, 55]
sound_levels_park_b = [50, 55, 42, 70, 60]
sound_levels_park_c = [48, 52, 41, 68, 58]
sound_levels_park_d = [46, 53, 43, 66, 56]

# Combine sound levels into a nested list for box plotting
sound_data = [sound_levels_park_a, sound_levels_park_b, sound_levels_park_c, sound_levels_park_d]

# Transpose the data to group by species
sound_data_transposed = list(map(list, zip(*sound_data)))

# Calculate the average sound level for each species across all parks
avg_sound_levels = [np.mean(levels) for levels in sound_data_transposed]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot horizontal box plots
bp = ax.boxplot(sound_data_transposed, vert=False, patch_artist=True, labels=species, notch=True)

# Customize boxplot colors
colors = ['#76b900', '#ff7f0e', '#1f77b4', '#ff4f79', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot the average sound levels as a line plot overlay
ax.plot(avg_sound_levels, range(1, len(species) + 1), color='black', marker='o', linestyle='-', linewidth=2, label='Average Sound Level')

# Set title and axis labels
ax.set_title('Comparative Analysis of Urban Wildlife Sound Levels in City Parks\nBox Plot with Average Sound Level Overlay', fontsize=16, fontweight='bold')
ax.set_xlabel('Sound Levels (Decibels)', fontsize=12)
ax.set_ylabel('Urban Wildlife Species', fontsize=12)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.5)

# Adding a legend for both the parks and the overlay
legend_labels = ['Park A', 'Park B', 'Park C', 'Park D', 'Average Sound Level']
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
legend_patches.append(plt.Line2D([0], [0], color='black', marker='o', lw=2))

ax.legend(legend_patches, legend_labels, title="City Parks & Averages", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()