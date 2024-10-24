import matplotlib.pyplot as plt
import numpy as np

# Define character attributes and labels
labels = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Charisma', 
          'Endurance', 'Perception', 'Luck', 'Dexterity', 'Arcane Knowledge']
num_vars = len(labels)

# Define data for each character's attributes
warrior = [9, 7, 3, 5, 6, 10, 4, 8, 9, 2]
wizard = [2, 4, 10, 9, 5, 3, 8, 5, 3, 10]
rogue = [5, 10, 6, 4, 8, 7, 9, 6, 10, 3]
paladin = [8, 5, 5, 6, 7, 9, 6, 7, 5, 7]
necromancer = [3, 3, 9, 9, 4, 4, 10, 6, 4, 10]

# Extend data to close the radar chart loop
data = np.array([warrior, wizard, rogue, paladin, necromancer])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Function to plot each character's attributes
def plot_character(ax, data, angles, label, color, linestyle):
    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Plot each character's data
plot_character(ax, data[0], angles, 'Warrior', 'crimson', 'solid')
plot_character(ax, data[1], angles, 'Wizard', 'royalblue', 'dashdot')
plot_character(ax, data[2], angles, 'Rogue', 'forestgreen', 'dotted')
plot_character(ax, data[3], angles, 'Paladin', 'gold', 'dashed')
plot_character(ax, data[4], angles, 'Necromancer', 'purple', 'solid')

# Customization
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10, color='navy', wrap=True)
ax.set_title("Comparative Analysis of Fantasy Characters' Attributes", size=16, color='midnightblue', wrap=True)

# Legend setup
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15))

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()