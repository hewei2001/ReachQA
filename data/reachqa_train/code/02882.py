import matplotlib.pyplot as plt
import numpy as np

# Define the attributes and character classes
attributes = ['Strength', 'Intelligence', 'Agility', 'Stamina', 'Charisma']
num_attrs = len(attributes)

# Data for each character class representing their attributes
warrior = [90, 30, 70, 85, 50]
mage = [20, 95, 60, 40, 70]
rogue = [60, 40, 95, 50, 65]
healer = [40, 80, 50, 70, 85]

# Extend data to close the radar chart loop
data = np.array([warrior, mage, rogue, healer])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_attrs, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each character class's attributes
def plot_character(ax, data, angles, label, color):
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Plot each character class's data with unique colors
plot_character(ax, data[0], angles, 'Warrior', 'firebrick')
plot_character(ax, data[1], angles, 'Mage', 'royalblue')
plot_character(ax, data[2], angles, 'Rogue', 'darkgreen')
plot_character(ax, data[3], angles, 'Healer', 'goldenrod')

# Customize chart features
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, color='navy', ha='center', va='center')
ax.set_title("Valoria's Champions:\nComparative Analysis of Character Class Attributes", size=14, color='darkviolet', va='bottom')

# Place legend outside the plot for better readability
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()