import matplotlib.pyplot as plt
import numpy as np

# Simulated temperature data for a 10x10 grid representing the city
temperature_data = np.array([
    [26, 27, 29, 30, 31, 32, 31, 30, 29, 28],
    [25, 26, 28, 30, 32, 33, 32, 31, 29, 27],
    [24, 25, 27, 29, 31, 34, 33, 32, 30, 28],
    [23, 25, 26, 28, 30, 35, 34, 33, 31, 29],
    [22, 23, 25, 27, 29, 33, 35, 34, 32, 30],
    [21, 23, 24, 26, 28, 32, 34, 35, 33, 31],
    [20, 22, 23, 25, 27, 31, 33, 34, 34, 32],
    [19, 21, 22, 24, 26, 30, 32, 33, 33, 33],
    [18, 20, 21, 23, 25, 29, 31, 32, 32, 32],
    [17, 19, 20, 22, 24, 28, 30, 31, 31, 31],
])

fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap
cax = ax.imshow(temperature_data, cmap='hot', interpolation='nearest', aspect='auto')

# Add a color bar
cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Temperature (°C)', rotation=270, labelpad=20)

# Axis labels
ax.set_xlabel('Neighborhoods (East to West)', fontsize=12)
ax.set_ylabel('Neighborhoods (North to South)', fontsize=12)

# Set x and y ticks
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.set_xticklabels([f'E{i+1}' for i in range(10)], rotation=45, ha='right', fontsize=10)
ax.set_yticklabels([f'N{i+1}' for i in range(10)], fontsize=10)

# Title
ax.set_title('Urban Heat Map of Metropolis:\nAnalyzing Urban Heat Islands', fontsize=14, pad=20)

# Annotate specific neighborhoods
annotations = {
    (4, 5): 'CBD',  # Central Business District
    (7, 7): 'Old Town',
    (2, 4): 'Riverside'
}

for (i, j), text in annotations.items():
    ax.text(j, i, text, ha='center', va='center', color='blue', fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))

# Gridlines for better readability
ax.grid(False)

# Automatically adjust layout to avoid clipping and overlapping
plt.tight_layout()

# Display the plot
plt.show()