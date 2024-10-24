import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Energy sources and their colors
energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Solar', 'Wind']
colors = ['#808080', '#FFD700', '#FF6347', '#FF4500', '#32CD32']

# Energy consumption data for each month (in GWh)
consumption_data = np.array([
    [420, 460, 430, 410, 400, 380, 390, 420, 450, 470, 480, 500],  # Coal
    [300, 310, 320, 330, 350, 340, 330, 320, 310, 300, 290, 280],  # Natural Gas
    [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],  # Nuclear
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75],              # Solar
    [60, 65, 70, 75, 80, 85, 90, 95, 100, 95, 90, 85]              # Wind
])

# Create a 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
num_sources = len(energy_sources)
num_months = 12
x_pos = np.arange(num_sources)
y_pos = np.arange(num_months)
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()

# Flatten the consumption data for plotting
z_pos = np.zeros_like(x_pos)
consumption_data_flat = consumption_data.T.flatten()

# Define bar width and depth
dx = dy = 0.5

# Plot the bars with distinct colors
for i in range(num_sources):
    ax.bar3d(x_pos[i::num_sources], y_pos[i::num_sources], z_pos[i::num_sources], dx, dy, consumption_data[i], color=colors[i], alpha=0.8)

# Add labels and title
ax.set_xlabel('Energy Source', fontsize=12, labelpad=10)
ax.set_ylabel('Month', fontsize=12, labelpad=10)
ax.set_zlabel('Energy Consumption (GWh)', fontsize=12, labelpad=10)
ax.set_title('Annual Energy Consumption by Source\nin Fictional City X (2023)', fontsize=16, fontweight='bold', pad=30)

# Customize ticks and labels
ax.set_xticks(np.arange(num_sources) + dx/2)
ax.set_xticklabels(energy_sources, rotation=45, ha='right')
ax.set_yticks(np.arange(num_months) + dy/2)
ax.set_yticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Set the viewing angle for better visibility
ax.view_init(elev=30, azim=120)

# Add a grid for clarity
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

# Add a legend
proxy_rects = [plt.Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(proxy_rects, energy_sources, loc='upper right', bbox_to_anchor=(1.15, 1), title='Energy Sources')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()