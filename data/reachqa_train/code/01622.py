import matplotlib.pyplot as plt
import numpy as np

# Define the attributes
attributes = [
    'Strength', 'Agility', 'Endurance', 'Intelligence', 
    'Charisma', 'Wisdom', 'Tactics', 'Stealth', 
    'Speed', 'Magic Resistance'
]
num_attributes = len(attributes)

# Warrior data
elven_archer = [40, 90, 60, 80, 55, 70, 85, 95, 90, 65]
dwarven_berserker = [90, 55, 95, 50, 60, 45, 65, 25, 40, 30]
human_paladin = [70, 70, 70, 75, 85, 65, 80, 50, 60, 55]
orc_shaman = [60, 40, 65, 85, 50, 90, 70, 30, 45, 95]
troll_warrior = [85, 60, 80, 40, 50, 55, 60, 20, 75, 35]

# Complete the loop for radar chart
for data in [elven_archer, dwarven_berserker, human_paladin, orc_shaman, troll_warrior]:
    data += data[:1]

# Create angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each warrior's attributes
warriors = {
    'Elven Archer': (elven_archer, 'forestgreen'),
    'Dwarven Berserker': (dwarven_berserker, 'darkgoldenrod'),
    'Human Paladin': (human_paladin, 'royalblue'),
    'Orc Shaman': (orc_shaman, 'purple'),
    'Troll Warrior': (troll_warrior, 'indianred')
}

for warrior, (stats, color) in warriors.items():
    ax.plot(angles, stats, linewidth=2, linestyle='solid', label=warrior, color=color)
    ax.fill(angles, stats, color=color, alpha=0.25)

# Add attribute labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10)

# Title and legend
ax.set_title(
    "Heroic Attributes of Fantasy Warriors in the Realm of Eldoria\n"
    "Exploring Strengths Across Multiple Dimensions", 
    fontsize=16, weight='bold', pad=40
)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1))

# Set the radial ticks and labels
ax.set_yticklabels([])
ax.set_ylim(0, 100)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()