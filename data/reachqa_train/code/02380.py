import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data
years = np.array([3021, 3022, 3023])
colonies = ['Neridia', 'Zephyria', 'Polaris Prime']
quantum_crystals = np.array([[150, 180, 210], [200, 220, 250], [180, 230, 270]])
stellar_silks = np.array([[100, 120, 140], [130, 150, 170], [120, 160, 180]])
antimatter_capsules = np.array([[50, 60, 70], [80, 90, 110], [70, 80, 90]])

# Stack the data layers
bottom_layer = np.zeros_like(quantum_crystals)
middle_layer = bottom_layer + quantum_crystals
top_layer = middle_layer + stellar_silks

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and color schemes
width = 0.2
colors = ['#33AFFF', '#FF33A3', '#33FF8E']

# Plot stacked bars
for idx, colony in enumerate(colonies):
    xpos = np.arange(len(years))  # Year positions
    ax.bar3d(xpos, idx, bottom_layer[idx], width, width, quantum_crystals[idx], color=colors[0], alpha=0.8, label='Quantum Crystals' if idx == 0 else "")
    ax.bar3d(xpos, idx, middle_layer[idx], width, width, stellar_silks[idx], color=colors[1], alpha=0.8, label='Stellar Silks' if idx == 0 else "")
    ax.bar3d(xpos, idx, top_layer[idx], width, width, antimatter_capsules[idx], color=colors[2], alpha=0.8, label='Antimatter Capsules' if idx == 0 else "")

# Set axis labels and ticks
ax.set_xlabel('Year', labelpad=20, fontsize=10)
ax.set_ylabel('Colony', labelpad=20, fontsize=10)
ax.set_zlabel('Trade Volume (Thousands)', labelpad=10, fontsize=10)
ax.set_xticks(xpos + width / 2)
ax.set_xticklabels(years, fontsize=10)
ax.set_yticks(np.arange(len(colonies)) + width / 2)
ax.set_yticklabels(colonies, fontsize=10)

# Title and Legend
ax.set_title('Intergalactic Commodity Trade Volumes\nFrom 3021 to 3023', fontsize=14, pad=30)
ax.legend(loc='upper left', fontsize=10)

# Enhance grid and appearance
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='-', linewidth=0.5)
ax.set_facecolor('whitesmoke')

# Adjust the view angle
ax.view_init(elev=20, azim=30)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()