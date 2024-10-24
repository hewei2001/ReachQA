import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Attributes we're comparing
attributes = ['Luminosity', 'Fragrance', 'Rarity', 'Healing', 'Growth']

# Data for the plants (each corresponds to the attributes in order)
data = {
    'Sunleaf': [8, 5, 6, 7, 5],
    'Moonblossom': [5, 9, 6, 6, 4],
    'Stardew Fern': [7, 4, 10, 5, 3],
    'Elven Lily': [6, 6, 7, 10, 5],
    'Dewdrop Vine': [5, 3, 6, 5, 9],
}

# Number of variables
num_vars = len(attributes)

# Compute angle for each attribute in radar chart
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each plant
for plant, values in data.items():
    values += values[:1]  # Repeat the first value to close the loop
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=plant)
    ax.fill(angles, values, alpha=0.25)

# Add labels for each attribute
plt.xticks(angles[:-1], attributes, color='grey', size=12)

# Set range for radial axes
ax.set_rscale('linear')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=10)
ax.set_ylim(0, 10)

# Title with line breaks for readability
plt.title("Mystical Properties of\nThe Enchanted Garden's Magical Plants", size=16, fontweight='bold', pad=40)

# Add a legend with a title
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Magical Plants")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()