import matplotlib.pyplot as plt
import numpy as np

# Define directions and signal strengths for the rose chart
directions = np.arange(0, 360, 45)  # 8 main directions
signal_strengths = [5, 15, 10, 20, 7, 12, 18, 9]  # Arbitrary strength values

# Create polar subplot for the rose chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Number of categories / directions
num_categories = len(directions)
sector_angle = (2 * np.pi) / num_categories

# Draw bars for each direction with varying lengths (strengths)
bars = ax.bar(np.deg2rad(directions), signal_strengths, width=sector_angle, bottom=0, edgecolor='black')

# Customization of bar colors using a colormap
for bar, strength in zip(bars, signal_strengths):
    bar.set_facecolor(plt.cm.plasma(strength / max(signal_strengths)))
    bar.set_alpha(0.75)

# Set title with line break for better visibility
ax.set_title("Zorath Rover Mission:\nEnergy Signal Frequencies by Direction", va='bottom', fontsize=16, weight='bold')

# Adjust direction and orientation of the compass
ax.set_theta_offset(np.pi / 2)  # North at the top
ax.set_theta_direction(-1)  # Clockwise

# Label compass directions
directions_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
ax.set_xticks(np.deg2rad(directions))
ax.set_xticklabels(directions_labels, fontsize=12, fontweight='bold')

# Add a legend
legend_labels = ['Weak', 'Moderate', 'Strong', 'Very Strong']
legend_colors = [plt.cm.plasma(x/max(signal_strengths)) for x in [5, 10, 15, 20]]
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in legend_colors]
ax.legend(legend_patches, legend_labels, loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Signal Intensity")

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()