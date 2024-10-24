import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Simulated extended temperature data for a 20x20 grid representing the city
temperature_data = np.array([
    [26, 27, 29, 30, 31, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 24, 25, 26, 27, 28],
    [25, 26, 28, 30, 32, 33, 32, 31, 29, 27, 26, 25, 24, 23, 22, 23, 24, 25, 26, 27],
    [24, 25, 27, 29, 31, 34, 33, 32, 30, 28, 27, 26, 25, 24, 23, 24, 25, 26, 27, 28],
    [23, 25, 26, 28, 30, 35, 34, 33, 31, 29, 28, 27, 26, 25, 24, 25, 26, 27, 28, 29],
    [22, 23, 25, 27, 29, 33, 35, 34, 32, 30, 29, 28, 27, 26, 25, 26, 27, 28, 29, 30],
    [21, 23, 24, 26, 28, 32, 34, 35, 33, 31, 30, 29, 28, 27, 26, 27, 28, 29, 30, 31],
    [20, 22, 23, 25, 27, 31, 33, 34, 34, 32, 31, 30, 29, 28, 27, 28, 29, 30, 31, 32],
    [19, 21, 22, 24, 26, 30, 32, 33, 33, 33, 32, 31, 30, 29, 28, 29, 30, 31, 32, 33],
    [18, 20, 21, 23, 25, 29, 31, 32, 32, 32, 31, 30, 29, 28, 27, 28, 29, 30, 31, 32],
    [17, 19, 20, 22, 24, 28, 30, 31, 31, 31, 30, 29, 28, 27, 26, 27, 28, 29, 30, 31],
    [16, 18, 19, 21, 23, 27, 29, 30, 30, 30, 29, 28, 27, 26, 25, 26, 27, 28, 29, 30],
    [15, 17, 18, 20, 22, 26, 28, 29, 29, 29, 28, 27, 26, 25, 24, 25, 26, 27, 28, 29],
    [14, 16, 17, 19, 21, 25, 27, 28, 28, 28, 27, 26, 25, 24, 23, 24, 25, 26, 27, 28],
    [13, 15, 16, 18, 20, 24, 26, 27, 27, 27, 26, 25, 24, 23, 22, 23, 24, 25, 26, 27],
    [12, 14, 15, 17, 19, 23, 25, 26, 26, 26, 25, 24, 23, 22, 21, 22, 23, 24, 25, 26],
    [11, 13, 14, 16, 18, 22, 24, 25, 25, 25, 24, 23, 22, 21, 20, 21, 22, 23, 24, 25],
    [10, 12, 13, 15, 17, 21, 23, 24, 24, 24, 23, 22, 21, 20, 19, 20, 21, 22, 23, 24],
    [ 9, 11, 12, 14, 16, 20, 22, 23, 23, 23, 22, 21, 20, 19, 18, 19, 20, 21, 22, 23],
    [ 8, 10, 11, 13, 15, 19, 21, 22, 22, 22, 21, 20, 19, 18, 17, 18, 19, 20, 21, 22],
    [ 7,  9, 10, 12, 14, 18, 20, 21, 21, 21, 20, 19, 18, 17, 16, 17, 18, 19, 20, 21]
])

fig, ax = plt.subplots(figsize=(12, 10))

# Plot the heatmap with a custom colormap for enhanced visibility
cax = ax.imshow(temperature_data, cmap='YlOrRd', interpolation='bicubic', aspect='auto')

# Add a color bar with custom ticks
cbar = fig.colorbar(cax, ax=ax, orientation='vertical', shrink=0.8)
cbar.set_label('Temperature (°C)', rotation=270, labelpad=20)
cbar.set_ticks(range(7, 37, 5))  # Custom tick marks

# Axis labels
ax.set_xlabel('Neighborhoods (East to West)', fontsize=12)
ax.set_ylabel('Neighborhoods (North to South)', fontsize=12)

# Set x and y ticks
ax.set_xticks(range(0, 20, 2))
ax.set_yticks(range(0, 20, 2))
ax.set_xticklabels([f'E{i+1}' for i in range(0, 20, 2)], rotation=45, ha='right', fontsize=10)
ax.set_yticklabels([f'N{i+1}' for i in range(0, 20, 2)], fontsize=10)

# Title
ax.set_title('Urban Heat Map of Metropolis:\nAnalyzing Urban Heat Islands with Expanded Data', fontsize=14, pad=20)

# Annotate specific neighborhoods with mathematical symbols
annotations = {
    (6, 10): r'$\Delta T \approx 5^\circ C$',  # Delta temperature
    (13, 14): r'$\nabla \cdot \mathbf{E} = 0$',  # Divergence
    (9, 8): r'$T_{avg} = 30^\circ C$'  # Average temperature
}

for (i, j), text in annotations.items():
    ax.text(j, i, text, ha='center', va='center', color='blue', fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))

# Contour lines for additional detail
contours = ax.contour(temperature_data, levels=range(10, 36, 5), colors='black', linewidths=0.5)
ax.clabel(contours, inline=True, fontsize=8, fmt='%d°C')

# Automatically adjust layout to avoid clipping and overlapping
plt.tight_layout()

# Display the plot
plt.show()