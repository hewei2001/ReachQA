import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Define city parks and wildlife types
parks = ['Central Park', 'Riverside Park', 'Liberty Park', 'Greenfield Park']
wildlife_types = ['Birds', 'Mammals', 'Reptiles']

# Wildlife encounters data (number of encounters)
encounters_data = np.array([
    [120, 80, 45],  # Central Park
    [95, 70, 60],   # Riverside Park
    [150, 50, 35],  # Liberty Park
    [85, 90, 55]    # Greenfield Park
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotting parameters
num_parks = len(parks)
num_wildlife_types = len(wildlife_types)
colors = plt.cm.viridis(np.linspace(0.2, 0.8, num_wildlife_types))  # Use a color map for better aesthetics

# Plot each park's data
for i in range(num_parks):
    x_positions = np.arange(num_wildlife_types)
    y_positions = [i] * num_wildlife_types
    z_positions = np.zeros(num_wildlife_types)
    
    # Bar plot
    ax.bar3d(
        x_positions, y_positions, z_positions, 
        dx=0.4, dy=0.4, dz=encounters_data[i], 
        color=colors, alpha=0.9, edgecolor='k'
    )
    
    # Add annotations
    for j in range(num_wildlife_types):
        ax.text(
            x_positions[j], y_positions[j], encounters_data[i, j] + 3,
            f'{encounters_data[i, j]}', ha='center', va='bottom', fontsize=8, color='black'
        )

# Set axis labels and title
ax.set_xlabel('Wildlife Type', labelpad=15, fontsize=11)
ax.set_ylabel('City Park', labelpad=15, fontsize=11)
ax.set_zlabel('Number of Encounters', labelpad=15, fontsize=11)
ax.set_title('Urban Wildlife Activity Tracking:\nEncounters in City Parks (2023)', pad=30, fontsize=14)

# Set ticks and labels
ax.set_xticks(np.arange(num_wildlife_types))
ax.set_xticklabels(wildlife_types, rotation=20, ha='right', fontsize=10)
ax.set_yticks(np.arange(num_parks))
ax.set_yticklabels(parks, fontsize=10)

# Customize the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Manually create legend
legend_handles = [Patch(color=colors[i], label=wildlife_types[i]) for i in range(num_wildlife_types)]
ax.legend(handles=legend_handles, loc='upper left', fontsize=10, title="Wildlife Types", title_fontsize=12, edgecolor='k')

# Adjust view angle for optimal visibility
ax.view_init(elev=35, azim=45)

# Adjust layout for optimal fit
plt.tight_layout()

# Display the plot
plt.show()