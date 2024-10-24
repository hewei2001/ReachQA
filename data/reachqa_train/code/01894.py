import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Energy sources and their corresponding usage percentages
energy_sources = ['Solar', 'Fusion', 'Wind', 'Geothermal', 'Hydrogen', 'Fossil Fuels']
energy_usage = np.array([25, 20, 15, 10, 20, 10])

# Colors and patterns for each section of the donut pie chart
colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9400D3', '#D2691E']
patterns = ["//", "\\\\", "||", "-", "+", "x"]

# Explode the first and second slice
explode = (0.1, 0.1, 0, 0, 0, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with a hole in the center
wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', linestyle='--', hatch=patterns[0]),
    shadow=True
)

# Customize text size and style
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

# Enhanced title with a split line
plt.title(
    'Galactic Energy Consumption:\nA Stellar Analysis of Energy Resources in 2050',
    fontsize=16, weight='bold', pad=20
)

# Custom Legend with icons
custom_patches = [Patch(facecolor=colors[i], hatch=patterns[i]) for i in range(len(colors))]
ax.legend(
    custom_patches, energy_sources, title="Energy Sources",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Add a subtle radial grid in the background for better proportion visibility
ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.2)

# Add a secondary pie chart inset
ax_inset = fig.add_axes([0.75, 0.7, 0.15, 0.15], aspect='equal')
inset_data = np.array([15, 25, 30, 20, 10])
inset_labels = ['2020', '2025', '2030', '2035', '2040']
inset_colors = ['#FFE4B5', '#FFB6C1', '#87CEFA', '#98FB98', '#D8BFD8']
ax_inset.pie(
    inset_data, labels=inset_labels, startangle=140, colors=inset_colors, 
    autopct='%1.0f%%', wedgeprops=dict(width=0.3, edgecolor='w')
)
ax_inset.set_title('Future Projections', fontsize=8, weight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()