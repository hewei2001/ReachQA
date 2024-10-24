import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Define regions and technology types
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America']
technologies = ['AI', 'Blockchain', 'IoT']

# Adoption scores data (0 to 100 scale)
adoption_data = np.array([
    [85, 70, 90],  # North America
    [75, 60, 80],  # Europe
    [80, 75, 85],  # Asia-Pacific
    [65, 55, 60]   # Latin America
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotting parameters
num_regions = len(regions)
num_technologies = len(technologies)
colors = plt.cm.plasma(np.linspace(0.2, 0.8, num_technologies))  # Use a vibrant color map

# Plot each region's data
for i in range(num_regions):
    x_positions = np.arange(num_technologies)
    y_positions = [i] * num_technologies
    z_positions = np.zeros(num_technologies)
    
    # Bar plot
    ax.bar3d(
        x_positions, y_positions, z_positions, 
        dx=0.4, dy=0.4, dz=adoption_data[i], 
        color=colors, alpha=0.9, edgecolor='k'
    )
    
    # Add annotations
    for j in range(num_technologies):
        ax.text(
            x_positions[j], y_positions[j], adoption_data[i, j] + 2,
            f'{adoption_data[i, j]}%', ha='center', va='bottom', fontsize=8, color='black'
        )

# Set axis labels and title
ax.set_xlabel('Technology Type', labelpad=15, fontsize=11)
ax.set_ylabel('Region', labelpad=15, fontsize=11)
ax.set_zlabel('Adoption Score (%)', labelpad=15, fontsize=11)
ax.set_title('Tech Innovation Adoption in Global Markets (2023)', pad=30, fontsize=14)

# Set ticks and labels
ax.set_xticks(np.arange(num_technologies))
ax.set_xticklabels(technologies, rotation=30, ha='right', fontsize=10)
ax.set_yticks(np.arange(num_regions))
ax.set_yticklabels(regions, fontsize=10)

# Customize the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Manually create legend
legend_handles = [Patch(color=colors[i], label=technologies[i]) for i in range(num_technologies)]
ax.legend(handles=legend_handles, loc='upper left', fontsize=10, title="Technologies", title_fontsize=12, edgecolor='k')

# Adjust view angle for optimal visibility
ax.view_init(elev=30, azim=45)

# Adjust layout for optimal fit
plt.tight_layout()

# Display the plot
plt.show()