import matplotlib.pyplot as plt
import numpy as np

# Define character attributes and their corresponding values for each class
attributes = ['Strength', 'Agility', 'Intelligence', 'Stamina', 'Magic Power', 'Stealth']
classes = {
    'Warrior': [8, 5, 3, 9, 2, 4],
    'Mage': [3, 4, 9, 6, 10, 2],
    'Rogue': [5, 9, 4, 5, 3, 10]
}

# Number of attributes (spokes in the radar chart)
num_vars = len(attributes)

# Compute angle for each attribute on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart requires us to "close the loop" by appending the start to the end
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one area per character class
for class_name, values in classes.items():
    values += values[:1]  # Repeat the first value to close the loop
    ax.fill(angles, values, alpha=0.25, label=class_name)
    ax.plot(angles, values, linewidth=2)

# Customize the appearance of the radar chart
ax.set_yticklabels([])  # Hide radial tick labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=12, fontweight='bold')

# Adding a legend and title
plt.title('Fantasy RPG Character Attributes\nComparative Analysis', fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Ensure everything fits within the plot area
plt.tight_layout()

# Show the radar chart
plt.show()