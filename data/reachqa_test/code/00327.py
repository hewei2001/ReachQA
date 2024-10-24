import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Extended Character attributes
attributes = [
    'Strength', 'Agility', 'Intelligence', 'Endurance', 'Charisma', 
    'Luck', 'Wisdom', 'Perception', 'Stamina', 'Dexterity'
]
n_attributes = len(attributes)

# Data for each character class with sum requirement: each sum to 60
warrior_scores = [9, 6, 4, 10, 5, 3, 4, 4, 8, 7]
mage_scores = [4, 3, 10, 5, 9, 6, 10, 4, 5, 4]
rogue_scores = [5, 10, 5, 7, 8, 8, 2, 5, 6, 4]
paladin_scores = [8, 5, 5, 9, 6, 4, 6, 6, 8, 3]

# Close the radar chart by appending the first value
warrior_scores += warrior_scores[:1]
mage_scores += mage_scores[:1]
rogue_scores += rogue_scores[:1]
paladin_scores += paladin_scores[:1]

# Angles for each attribute
angles = np.linspace(0, 2 * pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

# Create a radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each character class
ax.plot(angles, warrior_scores, linewidth=2, linestyle='solid', label='Warrior', color='red')
ax.fill(angles, warrior_scores, 'red', alpha=0.25)

ax.plot(angles, mage_scores, linewidth=2, linestyle='dashed', label='Mage', color='blue')
ax.fill(angles, mage_scores, 'blue', alpha=0.25)

ax.plot(angles, rogue_scores, linewidth=2, linestyle='dotted', label='Rogue', color='green')
ax.fill(angles, rogue_scores, 'green', alpha=0.25)

ax.plot(angles, paladin_scores, linewidth=2, linestyle='dashdot', label='Paladin', color='purple')
ax.fill(angles, paladin_scores, 'purple', alpha=0.25)

# Set the attribute labels
plt.xticks(angles[:-1], attributes, color='black', size=10)

# Set radial limits
ax.set_ylim(0, 10)

# Customize gridlines
ax.yaxis.grid(True, color='grey', linestyle='-', linewidth=0.5)

# Add a title
ax.set_title(
    "Character Attribute Distribution in Eldoria\nChoose Your Class Wisely",
    fontsize=14, fontweight='bold', pad=20
)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Ensure everything fits well without overlap
plt.tight_layout()

# Display the chart
plt.show()