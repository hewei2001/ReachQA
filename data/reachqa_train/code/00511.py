import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define labels for each coffee attribute
labels = np.array(['Aroma', 'Flavor', 'Acidity', 'Body', 'Aftertaste'])
num_vars = len(labels)

# Define attributes for each coffee type
espresso = [85, 90, 70, 95, 80]
latte = [75, 85, 60, 80, 70]
cappuccino = [80, 88, 65, 85, 75]
americano = [78, 80, 68, 75, 72]
cold_brew = [70, 78, 80, 70, 85]
data = np.array([espresso, latte, cappuccino, americano, cold_brew])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate angles for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
colors = ['#8B4513', '#D2B48C', '#A0522D', '#808080', '#008B8B']
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']

# Plot each coffee type with specific colors and add markers
for idx, coffee in enumerate(coffee_types):
    ax.fill(angles, data[idx], color=colors[idx], alpha=0.25)
    ax.plot(angles, data[idx], color=colors[idx], linewidth=2, linestyle='--', marker='o', markersize=7, label=coffee)

# Customization of the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)

# Draw concentric circles with annotations for clarity
for i in range(1, 6):
    ax.plot([0, 2 * np.pi], [i * 20, i * 20], linestyle='dotted', linewidth=1, color='gray')
ax.text(np.pi / 2, 105, 'Characteristic Intensity', horizontalalignment='center', size=10, color='gray')

# Enhance chart appearance
ax.spines['polar'].set_visible(False)
ax.grid(color='black', linewidth=0.5, linestyle=':')

# Title and legend
ax.set_title('Exploring Coffee Characteristics\nwith a Coffee Lover\'s Radar', size=15, color='#6B4423', pad=30, weight='bold')
legend_elements = [Patch(facecolor=colors[i], edgecolor='gray', label=coffee_types[i]) for i in range(len(coffee_types))]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.1, 1.15), fontsize=10)

# Improve layout
plt.tight_layout()

# Show the radar chart
plt.show()