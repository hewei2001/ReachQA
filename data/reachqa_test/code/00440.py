import matplotlib.pyplot as plt
import numpy as np

# Define neighborhoods and energy sources
neighborhoods = ['Downtown', 'Uptown', 'Midtown', 'Suburban', 'Oldtown']
energy_sources = ['Solar', 'Wind', 'Geothermal', 'Natural Gas', 'Coal']

# Adjusted percentage usage of each energy source per neighborhood
data = np.array([
    [35, 22, 15, 18, 10],  # Downtown
    [30, 25, 20, 15, 10],  # Uptown
    [25, 30, 25, 10, 10],  # Midtown
    [20, 15, 35, 20, 10],  # Suburban
    [15, 20, 15, 15, 35]   # Oldtown
])

# Create a figure with two subplots
fig = plt.figure(figsize=(18, 8))  # Increased figure size

# 3D Bar Plot
ax1 = fig.add_subplot(121, projection='3d')
_x = np.arange(len(neighborhoods))
_y = np.arange(len(energy_sources))
_xx, _yy = np.meshgrid(_x, _y, indexing="ij")
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros_like(x)
dx = dy = 0.8  # Further increased width for better spacing
dz = data.ravel()

colors = ['#FFD700', '#87CEEB', '#8B4513', '#FF4500', '#708090']
ax1.bar3d(x, y, z, dx, dy, dz, color=[colors[i % len(colors)] for i in range(len(dz))], alpha=0.8)

ax1.set_xticks(_x + dx / 2)
ax1.set_xticklabels(neighborhoods, rotation=15, ha='right', fontsize=10)
ax1.set_yticks(_y + dy / 2)
ax1.set_yticklabels(energy_sources, fontsize=10)
ax1.set_zlabel('Percentage Usage (%)', fontsize=10)
ax1.set_title('Energy Source Distribution Across\nEcoCity Neighborhoods', fontsize=14, pad=20)
legend_labels = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(legend_labels, energy_sources, title="Energy Sources", loc='upper right', bbox_to_anchor=(1.25, 1.0))
ax1.view_init(elev=20., azim=-30) 

# Heatmap Plot
ax2 = fig.add_subplot(122)
cax = ax2.imshow(data.T, cmap='viridis', aspect='auto')
ax2.set_xticks(np.arange(len(neighborhoods)))
ax2.set_xticklabels(neighborhoods, rotation=15, ha='right', fontsize=10)
ax2.set_yticks(np.arange(len(energy_sources)))
ax2.set_yticklabels(energy_sources, fontsize=10)
ax2.set_title('Energy Source Usage Heatmap', fontsize=14, pad=20)
fig.colorbar(cax, ax=ax2, orientation='vertical', label='Usage')

plt.subplots_adjust(wspace=0.4)  # Increased spacing between subplots
plt.tight_layout()
plt.show()