import matplotlib.pyplot as plt
import numpy as np

# Feather length data for Arctic Larks in different regions
scandinavia_lengths = [12.5, 13.0, 13.5, 14.0, 14.5, 13.2, 13.8, 14.1, 12.9, 13.7]
greenland_lengths = [11.0, 11.5, 12.0, 12.5, 13.0, 12.3, 12.8, 11.9, 12.4, 12.6]
siberia_lengths = [13.5, 14.0, 14.5, 15.0, 15.5, 14.2, 14.8, 15.1, 13.9, 14.7]
alaska_lengths = [13.0, 13.5, 14.0, 14.5, 15.0, 13.3, 14.3, 13.8, 14.2, 14.9]

# Combine data into a list for easy plotting
data = [scandinavia_lengths, greenland_lengths, siberia_lengths, alaska_lengths]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal boxplot
boxplot_elements = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
           boxprops=dict(facecolor='lightblue', color='darkblue'),
           whiskerprops=dict(color='darkblue'),
           capprops=dict(color='darkblue'),
           medianprops=dict(color='darkred'),
           flierprops=dict(marker='o', color='darkred', alpha=0.5))

# Customize each box with a different shade for variety
colors = ['#aec7e8', '#ffbb78', '#98df8a', '#ff9896']
for patch, color in zip(boxplot_elements['boxes'], colors):
    patch.set_facecolor(color)

# Set y-axis labels to region names
ax.set_yticklabels(['Scandinavia', 'Greenland', 'Siberia', 'Alaska'])

# Title and axis labels
ax.set_title('Variation in Feather Length of Arctic Larks Across\nNorthern Regions', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Feather Length (cm)', fontsize=12)
ax.set_ylabel('Region', fontsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding annotations for specific insights
ax.annotate('Longest median\nfeathers', xy=(14.5, 3), xytext=(15, 3.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black', ha='center')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()