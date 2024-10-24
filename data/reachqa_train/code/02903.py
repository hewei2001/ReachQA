import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Countries in Candyland
countries = ['Sweetopia', 'Chocoria', 'Cocotown', 'Nougatville', 'Truffleheim']
# Annual chocolate consumption per person in kilograms
consumption = [35, 40, 22, 30, 45]

# Set positions and width for the bars
x_pos = np.arange(len(countries))
width = 0.6

# Create the bar chart with enhanced features
fig, ax = plt.subplots(figsize=(12, 7))

# Apply gradient effect using a colormap
colors = plt.cm.BuGn(np.linspace(0.5, 1, len(countries)))

bars = ax.bar(x_pos, consumption, width, color=colors, edgecolor='darkgrey', linewidth=1.5, hatch='/')

# Title and labels with enhanced styling
ax.set_title('Annual Chocolate Consumption per Country in Candyland\nMeasured in Kilograms per Person', 
             fontsize=16, fontweight='bold', pad=20, color='saddlebrown')
ax.set_xlabel('Countries', fontsize=12, fontweight='bold', color='darkgreen')
ax.set_ylabel('Chocolate Consumption (kg/person)', fontsize=12, fontweight='bold', color='darkgreen')
ax.set_xticks(x_pos)
ax.set_xticklabels(countries, fontsize=11, rotation=15, ha='right', color='chocolate')

# Adding data labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval} kg', ha='center', va='bottom', fontsize=10, color='brown')

# Highlight the bar with the highest consumption
max_index = consumption.index(max(consumption))
bars[max_index].set_edgecolor('gold')
bars[max_index].set_linewidth(2.5)

# Customize grid lines
ax.set_ylim(0, 50)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add subtle background gradient
ax.set_facecolor('#fff9e6')

# Annotated markers above each bar (using simple text as placeholders for markers)
for idx, bar in enumerate(bars):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2.5, 
            "🍫", ha='center', va='bottom', fontsize=14)

# Add a legend for the patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='darkgrey', hatch='/', label=countries[i]) for i in range(len(countries))]
ax.legend(handles=legend_elements, title='Countries', loc='upper right', fontsize=10)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()