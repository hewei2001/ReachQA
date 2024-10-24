import matplotlib.pyplot as plt
import numpy as np

# Character Attributes and Labels
labels = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Charisma']
num_vars = len(labels)

# Data for each character's attributes
warrior = [9, 6, 3, 4, 7]
wizard = [3, 5, 9, 8, 4]
rogue = [4, 9, 6, 3, 8]

# Extend data to close the radar chart loop
data = np.array([warrior, wizard, rogue])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each character's attributes
def plot_character(ax, data, angles, label, color):
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Plot each character's data
plot_character(ax, data[0], angles, 'Warrior', 'crimson')
plot_character(ax, data[1], angles, 'Wizard', 'royalblue')
plot_character(ax, data[2], angles, 'Rogue', 'forestgreen')

# Customization
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12, color='navy')
ax.set_title("Fantasy Characters' Attributes\nComparative Analysis", size=16, color='midnightblue', va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()