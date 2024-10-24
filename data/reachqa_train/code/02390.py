import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
sectors = ['Exploration', 'Defense', 'Science', 'Colonization', 'Communication']
resource_allocation = [30, 20, 25, 15, 10]

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a horizontal bar chart
bars = ax.barh(sectors, resource_allocation, color=colors, edgecolor='black', alpha=0.7)

# Set limits and labels
ax.set_xlim(0, 100)
ax.set_xlabel('Percentage of Total Resources', fontsize=12)
ax.set_title('Resource Allocation in the Galactic Exploration Federation\n(2073)', fontsize=14, pad=15)

# Annotate bars with percentage values
for bar in bars:
    width = bar.get_width()
    label_y = bar.get_y() + bar.get_height() / 2
    ax.annotate(f'{width}%', xy=(width, label_y), xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

# Enhance visibility by adjusting y-tick labels
ax.set_yticklabels(sectors, fontsize=12)

# Set gridlines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', label=sectors[i]) for i in range(len(sectors))]
ax.legend(handles=legend_elements, loc='upper right', title="Sectors")

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()