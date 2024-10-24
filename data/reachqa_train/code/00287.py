import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the attributes and their values for each creature
attributes = ['Strength', 'Agility', 'Intelligence', 'Wisdom', 'Charisma']
n_attributes = len(attributes)

# Attributes scores for each mythical creature
dragon_stats = [8, 6, 9, 7, 5]
unicorn_stats = [5, 9, 7, 8, 9]
griffin_stats = [7, 8, 6, 6, 8]

# Calculate angle for each attribute
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

def plot_creature(ax, stats, label, color):
    # Add the first attribute value to the end to close the circle
    stats += stats[:1]
    ax.plot(angles, stats, color=color, linewidth=2, label=label)
    ax.fill(angles, stats, color=color, alpha=0.25)

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each mythical creature
plot_creature(ax, dragon_stats, 'Dragon', 'firebrick')
plot_creature(ax, unicorn_stats, 'Unicorn', 'forestgreen')
plot_creature(ax, griffin_stats, 'Griffin', 'royalblue')

# Configure the chart
plt.xticks(angles[:-1], attributes, color='gray', size=10)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="gray", size=8)
plt.ylim(0, 10)

# Adding legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title("Attributes of Mythical Creatures\nin the World of Eldoria", size=14, color='navy', pad=20)

# Optimize layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()