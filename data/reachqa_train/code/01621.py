import matplotlib.pyplot as plt
import numpy as np

# Define the attributes
attributes = ['Strength', 'Agility', 'Endurance', 'Intelligence', 'Charisma']
num_attributes = len(attributes)

# Warrior data
elven_archer = [40, 90, 60, 80, 55]
dwarven_berserker = [90, 55, 95, 50, 60]
human_paladin = [70, 70, 70, 75, 85]

# Complete the loop for radar chart
elven_archer += elven_archer[:1]
dwarven_berserker += dwarven_berserker[:1]
human_paladin += human_paladin[:1]

# Create angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each warrior's attributes
ax.plot(angles, elven_archer, linewidth=2, linestyle='solid', label='Elven Archer', color='forestgreen')
ax.fill(angles, elven_archer, color='forestgreen', alpha=0.25)

ax.plot(angles, dwarven_berserker, linewidth=2, linestyle='solid', label='Dwarven Berserker', color='darkgoldenrod')
ax.fill(angles, dwarven_berserker, color='darkgoldenrod', alpha=0.25)

ax.plot(angles, human_paladin, linewidth=2, linestyle='solid', label='Human Paladin', color='royalblue')
ax.fill(angles, human_paladin, color='royalblue', alpha=0.25)

# Add attribute labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10)

# Title and legend
ax.set_title("Heroic Attributes of Fantasy Warriors\nin Eldoria", fontsize=16, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Set the radial ticks and labels
ax.set_yticklabels([])
ax.set_ylim(0, 100)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()