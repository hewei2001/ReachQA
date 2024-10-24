import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.colors import LinearSegmentedColormap

# Data for the chart
sectors = ['Exploration', 'Defense', 'Science', 'Colonization', 'Communication']
resource_allocation = [30, 20, 25, 15, 10]
growth_forecast = [5, 3, 4, 2, 1]  # Additional metric for illustration

# Gradient colors for the bars
cmap = LinearSegmentedColormap.from_list("custom", ['#1f77b4', '#a6cee3'])

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart with gradient fill
bars = ax.barh(sectors, resource_allocation, color=[cmap(0.5 + 0.02*i) for i in range(len(sectors))],
               edgecolor='black', alpha=0.7)

# Set limits and labels
ax.set_xlim(0, 100)
ax.set_xlabel('Percentage of Total Resources', fontsize=12)
ax.set_title('Resource Allocation in the Galactic Exploration Federation\nProspective Developments 2073', 
             fontsize=14, pad=20)

# Annotate bars with percentage values and growth forecasts
for idx, bar in enumerate(bars):
    width = bar.get_width()
    label_y = bar.get_y() + bar.get_height() / 2
    ax.annotate(f'{width}%\n(+{growth_forecast[idx]}%)', xy=(width, label_y), xytext=(5, 0), 
                textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

# Enhance visibility by adjusting y-tick labels and adding pattern
ax.set_yticklabels(sectors, fontsize=12)
for i, bar in enumerate(bars):
    ax.text(50, i, '+++', ha='center', va='center', color='gray', alpha=0.1, fontsize=28)

# Set gridlines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.grid(False)

# Add legend with additional context
legend_elements = [Patch(facecolor=cmap(0.5 + 0.02*i), edgecolor='black', label=f'{sectors[i]} ({growth_forecast[i]}% growth)')
                   for i in range(len(sectors))]
ax.legend(handles=legend_elements, loc='upper right', title="Sectors & Growth Forecast", fontsize=10)

# Create secondary subplot for additional data visualization (hypothetical context)
ax_secondary = ax.twiny()
ax_secondary.plot(growth_forecast, sectors, 'o--', color='green', label='Growth Trend', markersize=6)
ax_secondary.set_xlabel('Growth Forecast (%)', fontsize=12)
ax_secondary.set_xlim(0, max(growth_forecast) + 1)
ax_secondary.grid(False)

# Add decorative background for thematic relevance
fig.patch.set_facecolor('#f0f8ff')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()