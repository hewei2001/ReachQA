import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Rectangle

# Define the districts and days of the week
districts = ['Downtown', 'Riverside', 'Uptown', 'Suburbia', 'Old Town']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Coffee consumption data: cups of coffee consumed in each district per day
coffee_data = np.array([
    [120, 130, 125, 140, 150, 200, 180],
    [90, 95, 100, 105, 110, 160, 150],
    [80, 85, 90, 95, 100, 140, 130],
    [60, 65, 70, 75, 80, 120, 110],
    [70, 75, 80, 85, 90, 130, 120]
])

fig, ax = plt.subplots(figsize=(12, 7))
cax = ax.imshow(coffee_data, cmap='RdYlGn', aspect='auto', interpolation='nearest')

# Set axis ticks
ax.set_xticks(np.arange(len(days)))
ax.set_yticks(np.arange(len(districts)))

# Label the axes with enhanced styling
ax.set_xticklabels(days, fontsize=10, fontweight='bold', color='navy')
ax.set_yticklabels(districts, fontsize=10, fontweight='bold', color='navy')

# Rotate the tick labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Add labels on each cell
for i in range(len(districts)):
    for j in range(len(days)):
        ax.text(j, i, coffee_data[i, j], ha='center', va='center', color='black', fontsize=9, fontweight='bold')

# Add a color bar with a label
cbar = ax.figure.colorbar(cax, ax=ax, format=ticker.FuncFormatter(lambda x, _: int(x)))
cbar.ax.set_ylabel('Cups of Coffee', rotation=-90, va='bottom', fontsize=12, color='navy')

# Highlight maximum and minimum values with special annotations
max_val = np.max(coffee_data)
min_val = np.min(coffee_data)

for i in range(len(districts)):
    for j in range(len(days)):
        if coffee_data[i, j] == max_val:
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor='red', lw=2))
        elif coffee_data[i, j] == min_val:
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor='blue', lw=2))

# Title with thematic annotation for added context
plt.title('Urban Coffee Consumption Patterns\nin Beanlandia by District and Day',
          fontsize=16, fontweight='bold', color='darkred', pad=25)

# Add subtle grid lines
ax.grid(which='major', color='gray', linestyle='--', linewidth=0.5)

# Adjust layout to avoid overlaps
plt.tight_layout()

# Show the plot
plt.show()