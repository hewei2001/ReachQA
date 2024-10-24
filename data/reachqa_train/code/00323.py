import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the regions and operating systems
regions = ['North America', 'Europe', 'Asia']
os_types = ['Android', 'iOS', 'Others']

# Market share data in percentages
market_share = [
    [40, 55, 5],  # North America
    [65, 30, 5],  # Europe
    [80, 15, 5]   # Asia
]

# Set up positions for the bars
x_pos = np.arange(len(regions))
y_pos = np.arange(len(os_types))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Heights of the bars
dx = dy = 0.3
dz = np.array(market_share).flatten()

# Create the 3D bar plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define color for each operating system
colors = ['#4CAF50', '#2196F3', '#FFC107']  # Android, iOS, Others

# Plot the bars with the assigned colors
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % 3] for i in y_pos], alpha=0.8)

# Setting axis labels and title with line breaks
ax.set_xlabel('Regions', labelpad=10)
ax.set_ylabel('Operating Systems', labelpad=10)
ax.set_zlabel('Market Share (%)', labelpad=10)
ax.set_title('Global Market Share of Smartphones\nby Operating System (2023)', fontsize=14, fontweight='bold')

# Configure ticks and labels to avoid overlap
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=25, ha='right')
ax.set_yticks(np.arange(len(os_types)))
ax.set_yticklabels(os_types)

# Adjust Z-axis to reflect percentage scale
ax.set_zlim(0, 100)

# Adding a legend for operating systems
legend_patches = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
ax.legend(legend_patches, os_types, title='Operating Systems', loc='upper left', bbox_to_anchor=(1.05, 1))

# Ensure layout is clear and elements don't overlap
plt.tight_layout()

# Show the plot
plt.show()