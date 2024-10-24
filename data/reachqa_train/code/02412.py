import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define years and destinations
years = np.array(['2050', '2051', '2052', '2053', '2054'])
destinations = ['Moon', 'Mars', 'Orbital Hotels']

# Artificial data: Number of tourists in thousands
tourists_data = np.array([
    [20, 25, 30, 35, 40],  # Moon
    [5, 10, 15, 22, 30],   # Mars
    [15, 20, 28, 36, 45],  # Orbital Hotels
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for each destination
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot each destination with bars
for dest_idx, destination in enumerate(destinations):
    # Define positions for the bars for each destination
    x_pos = np.arange(len(years))
    y_pos = np.full_like(x_pos, dest_idx)  # y_pos is fixed for each destination
    z_pos = np.zeros_like(x_pos)
    
    dz = tourists_data[dest_idx]
    ax.bar3d(x_pos, y_pos, z_pos, dx=0.5, dy=0.5, dz=dz, color=colors[dest_idx], alpha=0.8, label=destination)

# Labeling the axes
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(destinations)))
ax.set_yticklabels(destinations, fontsize=10)
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Destination', labelpad=10)
ax.set_zlabel('Tourists (Thousands)', labelpad=10)

# Title and legend
ax.set_title('Space Tourism:\nThe Rise of Interplanetary Travel\n(2050-2054)', pad=30, fontsize=14, weight='bold')
ax.legend(title='Destinations', loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=-45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()