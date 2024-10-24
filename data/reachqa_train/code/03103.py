import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the attributes and character classes
attributes = ['Strength', 'Agility', 'Intelligence', 'Endurance', 'Charisma']
character_classes = ['Warrior', 'Rogue', 'Mage', 'Paladin', 'Bard']

# Define the attribute values for each class
attribute_values = {
    'Warrior': [8, 5, 3, 9, 4],
    'Rogue': [5, 9, 4, 6, 5],
    'Mage': [3, 5, 9, 4, 6],
    'Paladin': [7, 4, 6, 8, 7],
    'Bard': [4, 7, 5, 5, 9]
}

# Number of attributes
num_attributes = len(attributes)

# Calculate angle for each attribute on the radar chart
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axis per attribute and add labels
ax.set_theta_offset(pi / 2)  # Rotate chart so first attribute is at the top
ax.set_theta_direction(-1)  # Draw the chart clockwise
plt.xticks(angles[:-1], attributes, color='grey', size=10)

# Draw ylabels
ax.set_rscale('log')  # Logarithmic scale for better visual differentiation
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color='grey', size=7)
plt.ylim(0, 10)

# Plot data and fill
for char_class, values in attribute_values.items():
    values += values[:1]  # Repeat the first value to close the circle
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=char_class)
    ax.fill(angles, values, alpha=0.25)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Add a title
plt.title("Fantasy RPG Character Attributes\nClass Strengths and Weaknesses", size=15, fontweight='bold', pad=20)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()