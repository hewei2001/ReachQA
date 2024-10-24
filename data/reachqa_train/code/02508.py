import matplotlib.pyplot as plt
import numpy as np

# Define continents and devices
continents = ['North America', 'Europe', 'Asia']
devices = ['Laptops', 'Tablets', 'Smartphones']

# Define usage percentages for each continent and device
usage_percentages = {
    'North America': [40, 25, 35],
    'Europe': [45, 20, 35],
    'Asia': [50, 15, 35]
}

# Prepare data for plotting
xpos = np.arange(len(continents))
ypos = np.arange(len(devices))
xpos, ypos = np.meshgrid(xpos, ypos)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.6  # Width and depth of the bars

# Flatten the percentage data
dz = np.array([usage_percentages[continent][i] for continent in continents for i in range(len(devices))])

# Define colors
colors = np.array(['#1f77b4', '#ff7f0e', '#2ca02c'])  # Different colors for different devices

# Repeat colors to match the number of bars
color_assignments = np.repeat(colors, len(continents))

# Initialize the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color_assignments, alpha=0.8)

# Configure axis labels and ticks
ax.set_xlabel('Continent', fontsize=12, labelpad=10)
ax.set_ylabel('Device Type', fontsize=12, labelpad=15)
ax.set_zlabel('Usage Percentage (%)', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(continents)))
ax.set_xticklabels(continents, fontsize=10)
ax.set_yticks(np.arange(len(devices)))
ax.set_yticklabels(devices, fontsize=10)

# Set title and adjust text
ax.set_title("The Digital Nomad Lifestyle:\nDevice Usage Across the Globe", fontsize=16, fontweight='bold', pad=30)

# Legend for devices
device_legend = [plt.Rectangle((0, 0), 1, 1, color=color, ec="k") for color in colors]
ax.legend(device_legend, devices, title="Device Type", loc='upper left', fontsize=10)

# Set viewing angle
ax.view_init(elev=25, azim=135)

# Display grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()