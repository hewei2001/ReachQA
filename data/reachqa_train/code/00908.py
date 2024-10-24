import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the creatures and their attributes
categories = ['Strength', 'Speed', 'Intelligence', 'Magic', 'Stealth', 'Charisma']
creatures = {
    'Dragon': [9, 5, 7, 8, 4, 6],
    'Unicorn': [5, 8, 9, 7, 6, 9],
    'Goblin': [4, 7, 5, 3, 8, 4]
}

# Number of variables we're plotting.
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

# Complete the loop by joining the first angle to the end
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, size=10)

# Y-axis labels
ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot each creature's data and fill area
colors = ['#FF6347', '#4682B4', '#32CD32']  # Colors for Dragon, Unicorn, Goblin
for idx, (creature, values) in enumerate(creatures.items()):
    values += values[:1]  # Re-add the first value to close the loop
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=creature, color=colors[idx])
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

# Add title and legend
plt.title('Attributes of Fantasy Creatures in Eldoria', size=15, y=1.1, va='center')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()