import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the creatures and their attributes
categories = ['Strength', 'Intelligence', 'Agility', 'Magic', 'Resilience']
creatures = {
    "Dragon": [9, 7, 6, 8, 9],
    "Phoenix": [5, 8, 7, 10, 6],
    "Unicorn": [4, 9, 9, 7, 5],
    "Gryphon": [7, 6, 8, 5, 7]
}

num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define color scheme for the creatures
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
line_styles = ['solid', 'dashed', 'dotted', 'dashdot']
markers = ['o', '^', 's', 'd']

# Plot each creature
for i, (creature, values) in enumerate(creatures.items()):
    values += values[:1]  # Close the loop
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=creature)
    ax.plot(angles, values, color=colors[i], linewidth=2, linestyle=line_styles[i], marker=markers[i])

# Customize the grid
ax.set_yticks(range(1, 11))
ax.set_yticklabels(map(str, range(1, 11)), color='grey', size=10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Set the range for the axes
ax.set_ylim(0, 10)

# Enhance grid style
ax.yaxis.grid(True, color='grey', linestyle='dashed', linewidth=0.5)
ax.xaxis.grid(True, color='lightgrey', linestyle='dashed', linewidth=0.5)

# Add title with line breaks for better layout
plt.title('Abilities of Mythical Creatures\nin the World of Eldoria', size=16, color='navy', pad=20)

# Add legend outside the plot area
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Creatures', title_fontsize='13')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()