import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define decades and civilizations
decades = np.array([1970, 1980, 1990])
civilizations = ['Mesopotamia', 'Indus Valley', 'Maya']

# Number of artifacts discovered for each civilization in each decade
artifacts_data = np.array([
    [500, 600, 750],  # Mesopotamia
    [400, 450, 550],  # Indus Valley
    [300, 500, 700]   # Maya
])

# Colors for each civilization
colors = ['#8D8741', '#659DBD', '#DAAD86']  # Mesopotamia, Indus Valley, Maya

# Create a figure and set the 3D projection
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting
for i, civilization in enumerate(civilizations):
    xs = decades
    ys = np.full(xs.shape, i * 3)  # Use a different spacing factor
    zs = np.zeros(decades.shape)

    # Cumulative stacking of bars
    for j, (color, decade) in enumerate(zip(colors, decades)):
        height = artifacts_data[i, j]
        ax.bar3d(xs[j], ys[j], zs[j], dx=8, dy=0.8, dz=height, color=color, alpha=0.8, label=civilization if j == 0 else "")
        zs[j] += height

# Set labels and titles
ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Civilization', fontsize=12, labelpad=10)
ax.set_zlabel('Artifacts Discovered', fontsize=12, labelpad=10)
ax.set_yticks([i * 3 for i in range(len(civilizations))])
ax.set_yticklabels(civilizations)

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=135)

# Unique legend for the plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:3], labels[:3], loc='upper left', fontsize=10)

# Title with multiple lines for clarity
plt.title('Artifacts Discovered from Ancient Civilizations\n'
          'Over Three Decades (1970s-1990s)', pad=20, fontsize=14, fontweight='bold')

# Automatically adjust the layout to prevent label overlap
plt.tight_layout()

# Show plot
plt.show()