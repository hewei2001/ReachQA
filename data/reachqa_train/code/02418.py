import numpy as np
import matplotlib.pyplot as plt

# Define the sectors in the Martian colony
sectors = ['Agriculture', 'Research', 'Engineering', 'Entertainment']

# Construct data for hours spent on work and leisure for each sector
# (Assuming each list represents weekly hours for different individuals within the sector)
data = {
    'Agriculture': [45, 50, 52, 48, 49, 55, 47, 51, 50, 53],
    'Research': [40, 42, 39, 43, 41, 44, 38, 40, 42, 39],
    'Engineering': [50, 55, 53, 52, 56, 54, 51, 52, 55, 53],
    'Entertainment': [35, 36, 34, 38, 37, 39, 35, 34, 36, 35]
}

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Box plot drawing with colors specific to each box for clarity
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Draw the box plot
bp = ax.boxplot(data.values(), vert=False, patch_artist=True,
                boxprops=dict(facecolor='c', color='navy'),
                whiskerprops=dict(color='navy'),
                capprops=dict(color='navy'),
                flierprops=dict(markerfacecolor='red', marker='o', color='navy'),
                medianprops=dict(color='orange'),
                notch=True)

# Set specific colors for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add title and labels
ax.set_title("Productivity and Leisure Balance\nin a Futuristic Martian Colony", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Weekly Hours", fontsize=12)
ax.set_yticks(np.arange(1, len(sectors) + 1))
ax.set_yticklabels(sectors, fontsize=11)

# Add a grid for easier readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Set limits for the x-axis
ax.set_xlim(30, 60)

# Customize legend
legend_labels = ['Interquartile Range', 'Whiskers', 'Outliers', 'Median']
legend_patches = [plt.Line2D([0], [0], color=color, lw=2, marker='s', markersize=10, label=label)
                  for color, label in zip(colors + ['navy', 'red', 'orange'], legend_labels)]
ax.legend(handles=legend_patches, title='Box Plot Elements', fontsize=10, loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()