import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for the celestial bodies
bodies = ['Mars', 'Europa', 'Titan', 'Ganymede', 'Callisto', 'Mercury', 'Venus']
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42])  # million km
colonization_time = np.array([20, 40, 50, 60, 70, 30, 10])  # years
population_capacity = np.array([10, 5, 15, 8, 7, 3, 12])  # millions
tech_readiness = np.array([8, 5, 6, 4, 3, 7, 9])  # scale 1 to 10

# Normalize colors based on technological readiness
colors = tech_readiness / tech_readiness.max()

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Bubble plot
sc = ax.scatter(distances, colonization_time, tech_readiness,
                s=population_capacity*50, c=colors, cmap='plasma', alpha=0.7, edgecolors='w')

# Set viewing angle for better perspective
ax.view_init(elev=30, azim=120)

# Title and labels
ax.set_title('Prospective Celestial Bodies for Human Colonization\nBased on Distance, Time, and Readiness', fontsize=16, pad=20)
ax.set_xlabel('Distance from Earth (Million km)', fontsize=12, labelpad=10)
ax.set_ylabel('Colonization Time (Years)', fontsize=12, labelpad=10)
ax.set_zlabel('Tech Readiness (Scale 1-10)', fontsize=12, labelpad=10)

# Annotate each point
for i, body in enumerate(bodies):
    ax.text(distances[i], colonization_time[i], tech_readiness[i] + 0.5, body, fontsize=9)

# Color bar legend for technological readiness
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Technological Readiness (Scale 1-10)', fontsize=12)

# Legend for population capacity
pop_sizes = [3, 5, 10, 15]
pop_labels = [plt.Line2D([0], [0], marker='o', color='w', label=f'{v}M Capacity',
                         markerfacecolor='gray', markersize=np.sqrt(v*50), alpha=0.5)
              for v in pop_sizes]
ax.legend(title='Population Capacity', handles=pop_labels, loc='upper right', fontsize=9)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the chart
plt.show()