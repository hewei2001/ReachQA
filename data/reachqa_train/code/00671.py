import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data: percentage of spice usage across different regions
regions = ['Asia', 'Europe', 'America']
spices = ['Cumin', 'Turmeric', 'Chili Powder', 'Paprika', 'Cardamom']
percentages = [
    [35, 20, 25, 10, 10],  # Asia
    [15, 10, 20, 30, 25],  # Europe
    [10, 15, 35, 25, 15]   # America
]

# Setup the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define positions for the bars
x = np.arange(len(spices))
y = np.arange(len(regions))
x, y = np.meshgrid(x, y)
x = x.ravel()
y = y.ravel()
z = np.zeros_like(x)

# Heights of the bars
dz = [percentages[region][spice] for region in range(len(regions)) for spice in range(len(spices))]

# Colors for different regions
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Plotting bars
ax.bar3d(x, y, z, dx=0.6, dy=0.6, dz=dz, color=np.repeat(colors, len(spices)), alpha=0.8)

# Labeling
ax.set_xticks(np.arange(len(spices)))
ax.set_xticklabels(spices, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions, fontsize=10)

ax.set_xlabel('Spices', labelpad=10)
ax.set_ylabel('Regions', labelpad=10)
ax.set_zlabel('Usage (%)', labelpad=10)
ax.set_zlim(0, 40)

# Title
ax.set_title('Exploring Cultural Flavor Palettes:\nGlobal Spice Usage Study', pad=20, fontsize=14, weight='bold')

# Customize the view
ax.view_init(elev=20, azim=45)

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()