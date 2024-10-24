import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
agencies = ['NASA', 'ESA', 'ROSCOSMOS', 'CNSA', 'ISRO']
sectors = ['Human Spaceflight', 'Planetary Exploration', 'Satellite Tech', 'Space R&D', 'International Collaboration']

# Budget allocations in percentage for each sector by each space agency (adjusted data)
allocations_percentage = np.array([
    [35, 25, 20, 15, 5],   # NASA
    [30, 20, 25, 15, 10],  # ESA
    [40, 10, 20, 20, 10],  # ROSCOSMOS
    [50, 10, 15, 15, 10],  # CNSA
    [20, 30, 20, 25, 5]    # ISRO
])

# Absolute budget in billions for illustration purpose (fictional data)
budgets_billion = np.array([
    [30, 14, 10, 8, 5],    # NASA
    [22, 18, 14, 10, 8],   # ESA
    [25, 8, 12, 12, 7],    # ROSCOSMOS
    [35, 9, 13, 11, 8],    # CNSA
    [15, 16, 20, 15, 7]    # ISRO
])

# Set up the figure with two subplots
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# 3D Bar chart setup
xpos, ypos = np.meshgrid(np.arange(len(agencies)), np.arange(len(sectors)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.8
dz = allocations_percentage.flatten()
colors = plt.cm.viridis(np.linspace(0, 1, len(sectors)))

for i in range(len(sectors)):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
              color=colors[i], alpha=0.8)

ax1.set_xlabel('Space Agencies', labelpad=15)
ax1.set_ylabel('Sectors', labelpad=15)
ax1.set_zlabel('Budget Allocation (%)', labelpad=10)
ax1.set_xticks(np.arange(len(agencies)) + dx/2)
ax1.set_xticklabels(agencies, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(len(sectors)) + dy/2)
ax1.set_yticklabels(sectors, fontsize=10)
ax1.set_zlim(0, 50)
ax1.set_title('2023 Global Space Agency Funding\nAllocation by Sector', fontsize=14, fontweight='bold', pad=20)

legend_elements = [plt.Rectangle((0,0),1,1, fc=colors[i]) for i in range(len(sectors))]
ax1.legend(legend_elements, sectors, title='Sectors', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

ax1.view_init(elev=20, azim=45)

# 2D Heatmap setup
heatmap = ax2.imshow(budgets_billion, cmap='YlGnBu')

ax2.set_xticks(np.arange(len(sectors)))
ax2.set_xticklabels(sectors, rotation=45, ha='right', fontsize=10)
ax2.set_yticks(np.arange(len(agencies)))
ax2.set_yticklabels(agencies, fontsize=10)
ax2.set_title('Agency Budgets in Billion USD by Sector', fontsize=14, fontweight='bold', pad=20)

# Colorbar for heatmap
cbar = fig.colorbar(heatmap, ax=ax2, orientation='vertical')
cbar.set_label('Budget (Billion USD)', fontsize=10)

plt.subplots_adjust(wspace=0.5)  # Increase space between subplots
plt.show()