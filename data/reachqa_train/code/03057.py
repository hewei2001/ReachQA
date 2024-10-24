import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories and data for each character
categories = ['Magic', 'Stealth', 'Strength', 'Wisdom', 'Agility', 'Charisma']
num_vars = len(categories)

# Scores for each character
character_scores = {
    'Elven Wizard': [0.9, 0.4, 0.3, 0.8, 0.5, 0.6],
    'Dwarven Warrior': [0.2, 0.5, 0.9, 0.6, 0.4, 0.7],
    'Halfling Rogue': [0.3, 0.9, 0.4, 0.5, 0.8, 0.6],
    'Orcish Berserker': [0.3, 0.2, 0.9, 0.3, 0.6, 0.8],
    'Human Paladin': [0.6, 0.6, 0.6, 0.7, 0.6, 0.6],
}

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Create angles for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Plot each character's data
colors = ['#8a2be2', '#ff4500', '#4682b4', '#32cd32', '#ffa500']
for idx, (character, scores) in enumerate(character_scores.items()):
    scores += scores[:1]  # Close the loop
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=character, color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

# Add labels and title
plt.xticks(angles[:-1], categories, color='grey', size=10)
ax.set_rlabel_position(30)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=8)
plt.ylim(0, 1)

# Add a legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=9)
plt.title('Fantasy Character Attributes Analysis\nCouncil of the Six Realms', size=15, color='darkgreen', ha='center')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()