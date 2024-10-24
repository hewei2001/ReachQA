import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the sectors and energy types
sectors = ['Residential', 'Commercial', 'Industrial']
energy_types = ['Electricity', 'Natural Gas', 'Renewable', 'Oil']

# Percentage data of energy consumption for each sector
consumption_data = np.array([
    [40, 30, 20, 10],  # Residential
    [35, 25, 30, 10],  # Commercial
    [25, 40, 20, 15]   # Industrial
])

# Create a figure for the 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set the positions of the bars
x_pos = np.arange(len(sectors))
y_pos = np.arange(len(energy_types))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()

# Flatten the percentage data for easy plotting
z_pos = np.zeros_like(x_pos)
dx = dy = 0.3
dz = consumption_data.flatten()

# Choose colors for each energy type
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % len(colors)] for i in y_pos])

# Set labels
ax.set_xlabel('Sectors')
ax.set_ylabel('Energy Types')
ax.set_zlabel('Percentage (%)')
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors, rotation=45, ha='right')
ax.set_yticks(np.arange(len(energy_types)))
ax.set_yticklabels(energy_types)
ax.set_zlim(0, 100)

# Title and legend
ax.set_title('Energy Consumption Efficiency in Urban Areas:\nA Sector-Wise 3D Analysis', pad=20)
ax.view_init(elev=20, azim=210)

# Create a legend
bars = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(energy_types))]
ax.legend(bars, energy_types, title='Energy Types', loc='upper left', bbox_to_anchor=(0.8, 0.95))

# Automatically adjust layout for readability
plt.tight_layout()

# Show plot
plt.show()