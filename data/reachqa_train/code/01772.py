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

# Construct a related dataset for the innovation index
innovation_index = np.array([
    [30, 40, 60],    # Mesopotamia
    [50, 70, 80],    # Ancient China
    [45, 55, 65]     # Ancient Egypt
])

# Create the figure and subplots
fig = plt.figure(figsize=(18, 8))

# 3D Bar Chart - Original Plot
ax1 = fig.add_subplot(121, projection='3d')
dx = dy = 0.4
colors = ['#8B0000', '#FF8C00', '#4682B4']
for i, (era, patents) in enumerate(zip(eras, patent_data.T)):
    xpos = np.arange(len(civilizations))
    ypos = np.full_like(xpos, i, dtype=float)
    zpos = np.zeros_like(xpos)
    dz = patents
    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8, label=era)

ax1.set_xlabel('Civilization')
ax1.set_ylabel('Era')
ax1.set_zlabel('Patents Count')
ax1.set_title('Chronicles of Ancient Innovations:\nPatents Across Civilizations', fontsize=12)
ax1.set_xticks(np.arange(len(civilizations)) + dx/2)
ax1.set_xticklabels(civilizations, rotation=15)
ax1.set_yticks(np.arange(len(eras)) + dy/2)
ax1.set_yticklabels(eras, rotation=15)
ax1.view_init(elev=25, azim=45)
ax1.legend(loc='upper right', title='Historical Eras', bbox_to_anchor=(1.15, 1))
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# 2D Line Plot - New Subplot
ax2 = fig.add_subplot(122)
for idx, civ in enumerate(civilizations):
    ax2.plot(eras, innovation_index[idx], marker='o', label=civ, linewidth=2)

ax2.set_xlabel('Era')
ax2.set_ylabel('Innovation Index')
ax2.set_title('Trend of Innovation Index\nby Civilization', fontsize=12)
ax2.legend(loc='upper left', title='Civilizations')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()