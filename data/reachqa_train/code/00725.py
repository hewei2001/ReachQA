import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data setup
regions = ['Europe', 'Asia', 'Americas', 'Africa']
festivals = ['Diwali', 'Carnival', 'Oktoberfest', 'Chinese New Year', 'African Drumming Festival']

# Participation percentages
participation_data = np.array([
    [15, 35, 5, 20],  # Diwali
    [10, 5, 30, 15],  # Carnival
    [25, 10, 10, 5],  # Oktoberfest
    [5, 40, 10, 10],  # Chinese New Year
    [5, 5, 5, 50]     # African Drumming Festival
])

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Grid positions for bars
xpos, ypos = np.meshgrid(np.arange(len(regions)), np.arange(len(festivals)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.4
dz = participation_data.flatten()

# Gradient color map
color_map = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5']
colors = []
for i in range(len(dz)):
    colors.append(color_map[ypos[i]])

# Plot each festival as a distinct color with lighting effect
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8, edgecolor='k')

# Label the data on the bars for clarity
for x, y, z, c in zip(xpos, ypos, dz, colors):
    ax.text(x + dx/2, y + dy/2, z + 1, f'{int(z)}%', color='black', ha='center', va='bottom', fontsize=9)

# Setting labels and ticks
ax.set_xticks(np.arange(len(regions)) + dx / 2)
ax.set_xticklabels(regions, rotation=45, ha='right')
ax.set_yticks(np.arange(len(festivals)) + dy / 2)
ax.set_yticklabels(festivals)
ax.set_zlabel('Participation (%)')
ax.set_title('Global Engagement in Cultural Festivals:\nParticipation Rates by Region', fontsize=16, weight='bold', pad=30)

# Create a background grid
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Legend setup
legend_labels = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in color_map]
ax.legend(legend_labels, festivals, loc='upper left', bbox_to_anchor=(1.05, 1))

# Enhancing layout for clarity
plt.tight_layout()

plt.show()