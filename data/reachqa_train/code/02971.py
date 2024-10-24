import matplotlib.pyplot as plt
import numpy as np

# Set the data
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
energy_usage = np.array([
    [5.2, 5.5, 5.1, 5.3],  # Residential
    [6.8, 7.0, 6.7, 7.1],  # Commercial
    [9.5, 9.8, 9.6, 9.9],  # Industrial
    [4.1, 4.3, 4.2, 4.4]   # Transportation
])

# Create a meshgrid for the positions
x_pos = np.arange(len(quarters))
y_pos = np.arange(len(sectors))
x_pos_mesh, y_pos_mesh = np.meshgrid(x_pos, y_pos)
x_pos_mesh = x_pos_mesh.flatten()
y_pos_mesh = y_pos_mesh.flatten()
z_pos = np.zeros_like(x_pos_mesh)

# Bar heights
bar_heights = energy_usage.flatten()

# Color map for different sectors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bars
dx = dy = 0.5  # width and depth of each bar
ax.bar3d(x_pos_mesh, y_pos_mesh, z_pos, dx, dy, bar_heights, 
         color=np.repeat(colors, len(quarters)), alpha=0.8, zsort='average')

# Setting the labels and title
ax.set_xlabel('Quarters', fontsize=10)
ax.set_ylabel('Sectors', fontsize=10)
ax.set_zlabel('Energy Consumption (TWh)', fontsize=10)
ax.set_title('Energy Consumption by Sector\nFuturapolis 2050', fontsize=14, fontweight='bold')

# Set tick labels
ax.set_xticks(x_pos + dx/2)
ax.set_xticklabels(quarters)
ax.set_yticks(y_pos + dy/2)
ax.set_yticklabels(sectors)

# Adjust the viewing angle for better visibility
ax.view_init(elev=20, azim=135)

# Automatically adjust the layout
plt.tight_layout()

# Display plot
plt.show()