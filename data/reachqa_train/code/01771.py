import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the eras and civilizations
eras = ['Bronze Age', 'Iron Age', 'Classical Age']
civilizations = ['Mesopotamia', 'Ancient China', 'Ancient Egypt']

# Hypothetical patent data for each civilization across different eras
patent_data = np.array([
    [120, 90, 150],   # Mesopotamia
    [80, 200, 300],   # Ancient China
    [100, 120, 170]   # Ancient Egypt
])

# Create the figure and a 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define bar dimensions and colors
dx = dy = 0.4
colors = ['#8B0000', '#FF8C00', '#4682B4']

# Iterate over each era and civilization to plot the bars
for i, (era, patents) in enumerate(zip(eras, patent_data.T)):
    xpos = np.arange(len(civilizations))
    ypos = np.full_like(xpos, i, dtype=float)
    zpos = np.zeros_like(xpos)
    dz = patents

    # Plot each era's data with distinct colors
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8, label=era)

# Set labels and titles
ax.set_xlabel('Civilization', fontsize=12, labelpad=10)
ax.set_ylabel('Era', fontsize=12, labelpad=10)
ax.set_zlabel('Hypothetical Patents Count', fontsize=12, labelpad=10)
ax.set_title('Chronicles of Ancient Innovations:\nEvolution of Invention Patents Across Civilizations', fontsize=16, pad=30)

# Set ticks and tick labels
ax.set_xticks(np.arange(len(civilizations)) + dx/2)
ax.set_xticklabels(civilizations, fontsize=11, rotation=15)
ax.set_yticks(np.arange(len(eras)) + dy/2)
ax.set_yticklabels(eras, fontsize=11, rotation=15)

# Adjust the viewing angle
ax.view_init(elev=25, azim=45)

# Enable legend
ax.legend(loc='upper right', fontsize=10, title='Historical Eras', bbox_to_anchor=(1.15, 1))

# Enable grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)

# Automatically adjust layout to avoid overlapping
plt.tight_layout()

# Show the plot
plt.show()