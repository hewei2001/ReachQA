import matplotlib.pyplot as plt
import numpy as np

# Define character attributes with additional categories
categories = ['Strength', 'Dexterity', 'Intelligence', 'Charisma', 'Wisdom', 'Endurance', 'Perception', 'Luck']
N = len(categories)

# Data for each RPG character (new characters and more complex attribute values)
warrior_stats = [8, 6, 3, 5, 4, 7, 6, 5]
mage_stats = [2, 4, 9, 5, 7, 3, 5, 6]
rogue_stats = [5, 8, 5, 6, 5, 5, 9, 6]
paladin_stats = [7, 5, 5, 8, 6, 8, 4, 5]

# Close the loop by appending the first attribute to the end for each character
warrior_stats += warrior_stats[:1]
mage_stats += mage_stats[:1]
rogue_stats += rogue_stats[:1]
paladin_stats += paladin_stats[:1]

# Create the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot data for each character with enhanced visual features
colors = ['red', 'blue', 'green', 'purple']
characters = ['Warrior', 'Mage', 'Rogue', 'Paladin']
character_stats = [warrior_stats, mage_stats, rogue_stats, paladin_stats]

for stats, color, character in zip(character_stats, colors, characters):
    ax.fill(angles, stats, color=color, alpha=0.2)
    ax.plot(angles, stats, color=color, linewidth=2, linestyle='-', marker='o', label=character)

# Configure the labels and title
ax.set_yticks(range(1, 11))
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=9, weight='bold')

title = "Comparative Attribute Analysis of RPG Characters"
ax.set_title(title, size=14, weight='bold', pad=40)

# Add a legend with an adjusted position
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize='medium')

# Customize the grid
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()