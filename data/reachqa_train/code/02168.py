import matplotlib.pyplot as plt
import numpy as np

# Define the labels for the trading hubs (x-axis) and minerals (y-axis)
hubs = ['Mars', 'Moon', 'Europa', 'Titan']
minerals = ['Helium-3', 'Palladium', 'Tritium', 'Neptunium']

# Trade volumes in metric tons (hypothetical data)
trade_volumes = np.array([
    [200, 300, 150, 180],  # Mars
    [220, 280, 200, 150],  # Moon
    [250, 330, 180, 210],  # Europa
    [270, 310, 190, 220]   # Titan
])

# Create a meshgrid for the 3D bar positions
x_data, y_data = np.meshgrid(np.arange(trade_volumes.shape[0]), np.arange(trade_volumes.shape[1]), indexing='ij')

# Flatten the data for bar plotting
x_data_flat = x_data.flatten()
y_data_flat = y_data.flatten()
z_data_flat = np.zeros_like(x_data_flat)
volume_flat = trade_volumes.flatten()

# Plotting the 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Customize the colors for each mineral
colors = ['#FFD700', '#C0C0C0', '#8A2BE2', '#4682B4']  # Gold, Silver, BlueViolet, SteelBlue

# Plot each set of bars in the chart
for (x, y, z, volume, color) in zip(x_data_flat, y_data_flat, z_data_flat, volume_flat, np.repeat(colors, len(hubs))):
    ax.bar3d(x, y, z, dx=0.5, dy=0.5, dz=volume, color=color, alpha=0.7, edgecolor='black')

# Setting labels and title
ax.set_xticks(np.arange(len(hubs)))
ax.set_xticklabels(hubs, fontsize=10, rotation=15, ha='right')
ax.set_yticks(np.arange(len(minerals)))
ax.set_yticklabels(minerals, fontsize=10)
ax.set_zlabel('Trade Volume (Metric Tons)', fontsize=10)

# Adjust view angle for better visualisation
ax.view_init(elev=25, azim=140)

ax.set_title('Intergalactic Mineral Trade\nVolumes - 2123', fontsize=16, fontweight='bold', pad=20)

# Adding a legend
legend_elements = [plt.Line2D([0], [0], color=colors[i], lw=4, label=minerals[i]) for i in range(len(minerals))]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10, title='Minerals')

# Tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()