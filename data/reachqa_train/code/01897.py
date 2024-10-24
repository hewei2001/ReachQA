import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories (abilities)
categories = ['Strength', 'Intelligence', 'Agility', 'Magic', 'Endurance']

# Number of variables
num_vars = len(categories)

# Define the abilities of each creature (normalized to a scale of 1-10)
dragon = [8, 7, 6, 9, 8]
unicorn = [5, 9, 7, 8, 6]
griffin = [7, 6, 8, 5, 9]
phoenix = [6, 8, 7, 10, 7]

# List of creatures' abilities
creatures = [dragon, unicorn, griffin, phoenix]
creature_names = ['Dragon', 'Unicorn', 'Griffin', 'Phoenix']

# Angles for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the circle

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each creature
for i, creature in enumerate(creatures):
    data = creature + creature[:1]  # Complete the loop
    ax.plot(angles, data, label=creature_names[i], linewidth=2, linestyle='solid')
    ax.fill(angles, data, alpha=0.25)

# Configure the chart's appearance
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Add title and adjust its position
ax.set_title("Fantasy Creature Ability Comparison\nin the Realm of Eldoria", fontsize=14, fontweight='bold', pad=30)

# Add a legend, positioned to avoid overlap
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.2), title="Creatures")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()