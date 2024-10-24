import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the sectors and cloud solutions
sectors = ['Finance', 'Healthcare', 'Education', 'Retail']
cloud_solutions = ['IaaS', 'PaaS', 'SaaS']

# Percentage adoption data for each sector and cloud solution
adoption_data = np.array([
    [60, 45, 70],  # Finance
    [55, 50, 65],  # Healthcare
    [50, 60, 55],  # Education
    [65, 55, 75]   # Retail
])

# Colors for cloud solutions
colors = ['#FFD700', '#ADFF2F', '#87CEEB']  # Gold, GreenYellow, SkyBlue

# Create 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Set position indices for bars
x_positions = np.arange(len(cloud_solutions))
y_positions = np.arange(len(sectors))

# Plot each cloud solution as a different layer of bars
bar_width = 0.15
for i, solution in enumerate(cloud_solutions):
    for j, sector in enumerate(sectors):
        x_pos = x_positions[i]
        y_pos = y_positions[j]
        z_pos = 0
        dx = dy = bar_width
        dz = adoption_data[j, i]

        ax.bar3d(x_pos + i * bar_width, y_pos, z_pos, dx, dy, dz, color=colors[i], alpha=0.8)

# Labeling and title
ax.set_xlabel('Cloud Solution', fontsize=12, labelpad=10)
ax.set_ylabel('Sector', fontsize=12, labelpad=10)
ax.set_zlabel('Adoption (%)', fontsize=12, labelpad=10)
ax.set_xticks(x_positions + bar_width)
ax.set_xticklabels(cloud_solutions, rotation=45, ha='right', fontsize=11)
ax.set_yticks(y_positions + bar_width / 2)
ax.set_yticklabels(sectors, fontsize=11)
ax.set_zlim(0, 100)

# Title and legend
ax.set_title('Digital Transformation Trends:\nSector Adoption of Cloud Technologies', fontsize=16, fontweight='bold', pad=30)
ax.legend(cloud_solutions, title='Cloud Solutions', loc='upper left', fontsize=10)

# Enhance layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()