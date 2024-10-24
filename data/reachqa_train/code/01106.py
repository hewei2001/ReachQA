import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Planetary data
planets = ['Zyra', 'Orion', 'Xanthe', 'Eclipse', 'Nebulon']
tech_feasibility = np.array([7, 6, 8, 5, 9])
resource_richness = np.array([8, 7, 6, 9, 5])
habitation_potential = np.array([6, 8, 5, 7, 9])
population_capacity = np.array([200, 180, 150, 300, 120])  # in millions

# Set up the figure and 3D axis
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Create a 3D scatter plot
scatter = ax.scatter(
    tech_feasibility, resource_richness, habitation_potential,
    s=population_capacity*10,  # Bubble size scaled for visibility
    c=population_capacity,  # Bubble color
    cmap='viridis', alpha=0.8, edgecolor='k', linewidth=0.8
)

# Adding labels and title
ax.set_title('Space Colonization Efforts in 2150:\nEvaluation of Potential Planets', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Technological Feasibility (Scale 1-10)', fontsize=10, labelpad=12)
ax.set_ylabel('Resource Richness (Scale 1-10)', fontsize=10, labelpad=12)
ax.set_zlabel('Habitation Potential (Scale 1-10)', fontsize=10, labelpad=12)

# Annotate each planet
for i, planet in enumerate(planets):
    ax.text(tech_feasibility[i], resource_richness[i], habitation_potential[i],
            planet, fontsize=9, weight='bold', ha='left', va='bottom')

# Colorbar
colorbar = fig.colorbar(scatter, ax=ax, shrink=0.6, aspect=15)
colorbar.set_label('Estimated Population Capacity (millions)', fontsize=10, labelpad=10)

# Adjust viewing angle for better perspective
ax.view_init(elev=20, azim=130)

# Automatically adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()