import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the island names and magical elements
islands = ['Avalon', 'Eldoria', 'Lumina', 'Noxterra', 'Vespera']
elements = ['Mana', 'Ether', 'Elixir', 'Aura']

# Percentage data for each element on each island
percentage_data = np.array([
    [30, 25, 20, 25],  # Avalon
    [20, 30, 35, 15],  # Eldoria
    [25, 25, 30, 20],  # Lumina
    [15, 35, 25, 25],  # Noxterra
    [35, 15, 20, 30]   # Vespera
])

# Setup the figure and axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Configure the positions for the bars
x_pos, y_pos = np.meshgrid(np.arange(len(islands)), np.arange(len(elements)), indexing='ij')
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Bar dimensions
width = depth = 0.5

# Generate colors for each element
colors = plt.cm.tab20(np.arange(len(elements)))

# Create the bars
for i, color in enumerate(colors):
    ax.bar3d(x_pos[y_pos == i], y_pos[y_pos == i], z_pos[y_pos == i], 
             width, depth, percentage_data[:, i], 
             color=color, alpha=0.7, label=elements[i])

# Set the axes labels
ax.set_xlabel('Islands')
ax.set_ylabel('Magical Elements')
ax.set_zlabel('Abundance (%)')

# Customize tick labels
ax.set_xticks(np.arange(len(islands)))
ax.set_xticklabels(islands, rotation=15, ha='right')
ax.set_yticks(np.arange(len(elements)))
ax.set_yticklabels(elements)

# Add the title
ax.set_title('Magical Element Distribution\nAcross Fantasia Archipelago', fontsize=14, fontweight='bold', pad=20)

# Normalize z-axis to percentage
ax.set_zlim(0, 40)

# Add a legend with a title
ax.legend(title="Elements", loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()