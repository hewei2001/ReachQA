import matplotlib.pyplot as plt
import numpy as np

# Budget allocation data for each space agency
nasa_allocation = [25, 35, 25, 15]  # NASA
esa_allocation = [30, 30, 20, 20]   # ESA
roscosmos_allocation = [20, 40, 30, 10]  # Roscosmos
isro_allocation = [40, 25, 20, 15]  # ISRO

allocations = [nasa_allocation, esa_allocation, roscosmos_allocation, isro_allocation]
agencies = ['NASA', 'ESA', 'Roscosmos', 'ISRO']
categories = ['R&D', 'Space Exploration', 'Satellite Deployment', 'Administration']

fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal box plot
boxes = ax.boxplot(allocations, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(color='darkblue'),
                   whiskerprops=dict(color='darkblue'),
                   capprops=dict(color='darkblue'),
                   flierprops=dict(marker='o', color='red', alpha=0.5),
                   medianprops=dict(color='darkred'))

# Customizing box colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for i, patch in enumerate(boxes['boxes']):
    patch.set_facecolor(colors[i % len(colors)])

# Add annotations for insights
ax.annotate('High Space Exploration Investment', xy=(35, 1), xytext=(40, 0.5),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)
ax.annotate('Balanced Allocation Strategy', xy=(30, 2), xytext=(35, 1.5),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)

# Set y-tick labels and title
ax.set_yticklabels(agencies, fontsize=12, fontweight='bold')
ax.set_xlabel('Budget Allocation (%)', fontsize=13, fontweight='bold')
ax.set_title('Global Space Agency Budget Allocations\nby Category', fontsize=16, fontweight='bold', pad=20)

# Adding a legend to match categories with colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, categories, loc='upper right', title="Categories", fontsize=10)

# Adding grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()