import matplotlib.pyplot as plt
import numpy as np

# Define character classes and their respective attribute scores
labels = ['Strength', 'Intelligence', 'Agility', 'Endurance', 'Charisma', 
          'Wisdom', 'Dexterity', 'Perception', 'Luck', 'Stealth']
num_vars = len(labels)

# Create the data for each class
warrior_stats = [9, 3, 6, 8, 4, 5, 7, 6, 3, 2]
wizard_stats = [3, 9, 5, 5, 8, 9, 4, 7, 6, 3]
rogue_stats = [5, 5, 9, 4, 7, 4, 8, 9, 7, 8]
paladin_stats = [8, 5, 5, 9, 6, 6, 5, 5, 4, 3]
ranger_stats = [7, 4, 8, 5, 5, 5, 8, 6, 7, 9]

# Completing the loop for each class
warrior_stats += warrior_stats[:1]
wizard_stats += wizard_stats[:1]
rogue_stats += rogue_stats[:1]
paladin_stats += paladin_stats[:1]
ranger_stats += ranger_stats[:1]

# Calculate angles for each axis in the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Completing the loop

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot data and fill area for each character class
ax.fill(angles, warrior_stats, color='red', alpha=0.2, label='Warrior')
ax.fill(angles, wizard_stats, color='blue', alpha=0.2, label='Wizard')
ax.fill(angles, rogue_stats, color='green', alpha=0.2, label='Rogue')
ax.fill(angles, paladin_stats, color='purple', alpha=0.2, label='Paladin')
ax.fill(angles, ranger_stats, color='orange', alpha=0.2, label='Ranger')

ax.plot(angles, warrior_stats, color='red', linewidth=1.5)
ax.plot(angles, wizard_stats, color='blue', linewidth=1.5)
ax.plot(angles, rogue_stats, color='green', linewidth=1.5)
ax.plot(angles, paladin_stats, color='purple', linewidth=1.5)
ax.plot(angles, ranger_stats, color='orange', linewidth=1.5)

# Configure the chart with labels and title
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9)

# Multi-line title for readability
plt.title('Fantasy RPG Character Classes\nExtended Attribute Distribution\nExploration', 
          fontsize=16, fontweight='bold', va='bottom')

# Add legend with adjusted positioning
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1.05), fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()