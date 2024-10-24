import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and the number of variables (spokes)
categories = ['Speed', 'Strength', 'Wisdom', 'Camouflage', 'Healing']
n_categories = len(categories)

# Create the data for each mystical creature
creatures = {
    'Elven Scout': [9, 5, 7, 6, 4],
    'Forest Troll': [4, 9, 5, 3, 5],
    'Owl Guardian': [6, 5, 10, 4, 4],
    'Camouflaged Dryad': [5, 4, 6, 10, 3],
    'Healing Unicorn': [4, 5, 5, 4, 10]
}

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Calculate the angles for each axis
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Plot each creature
for creature, ability_scores in creatures.items():
    scores = ability_scores + ability_scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=creature)
    ax.fill(angles, scores, alpha=0.1)

# Add labels for each category
ax.set_yticklabels([])  # Remove y-tick labels for a cleaner look
plt.xticks(angles[:-1], categories, fontsize=10)

# Set up the range for each axis
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color="grey", size=7)
plt.ylim(0, 10)

# Add a legend and title
plt.title("Abilities of Mystical Forest Creatures", size=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='small')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()