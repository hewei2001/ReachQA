import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define data for ancient civilizations
civilizations = ['Egyptian Empire', 'Roman Empire', 'Greek City-States', 'Persian Empire', 'Chinese Han Dynasty', 'Indus Valley Civilization']

# Influence scale (0-100)
influence = np.array([85, 95, 70, 90, 88, 65])

# Trade reach (number of regions)
trade_reach = np.array([40, 60, 35, 50, 55, 30])

# Innovation level (0-100)
innovation = np.array([80, 95, 85, 75, 92, 78])

# Population in millions (for bubble size)
population = np.array([10, 56, 5, 40, 60, 4])

# Plotting the 3D scatter chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data with varying size for bubbles
scatter = ax.scatter(influence, trade_reach, innovation, s=population * 20, c=population, cmap='plasma', alpha=0.6, edgecolors='w', linewidth=0.5)

# Annotate each point with the civilization name
for i, civilization in enumerate(civilizations):
    ax.text(influence[i], trade_reach[i], innovation[i], civilization, fontsize=9, ha='right')

# Customize the axes
ax.set_title('Dimensions of Ancient Civilizations:\nInfluence, Trade, and Innovation', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Influence (0-100)', fontsize=12)
ax.set_ylabel('Trade Reach (Regions)', fontsize=12)
ax.set_zlabel('Innovation Level (0-100)', fontsize=12)

# Adjust viewing angle
ax.view_init(elev=20, azim=135)

# Add color bar to indicate population
cbar = plt.colorbar(scatter, ax=ax, shrink=0.5, aspect=10, pad=0.1)
cbar.set_label('Population (millions)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()