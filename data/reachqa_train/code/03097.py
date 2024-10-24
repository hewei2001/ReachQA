import matplotlib.pyplot as plt
import numpy as np

# Define character attributes and their corresponding values for each class
attributes = ['Strength', 'Agility', 'Intelligence', 'Stamina', 'Magic Power', 'Stealth']
classes = {
    'Warrior': [8, 5, 3, 9, 2, 4],
    'Mage': [3, 4, 9, 6, 10, 2],
    'Rogue': [5, 9, 4, 5, 3, 10]
}

num_vars = len(attributes)

# Compute angle for each attribute
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ['#FF5733', '#33FF57', '#3357FF']

# Plot each class
for idx, (class_name, values) in enumerate(classes.items()):
    values += values[:1]
    ax.fill(angles, values, color=colors[idx], alpha=0.2, label=class_name)
    ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='solid', marker='o', markersize=8)

# Adding grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)
ax.xaxis.grid(True, linestyle='-', linewidth=0.5)

# Set attribute labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, fontweight='bold')

# Set y-labels with radial scale information
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', fontsize=10)

# Title and legend configuration
ax.set_title('Fantasy RPG Character Attributes\nComparative Analysis', size=15, weight='bold', va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05), fontsize=9, frameon=False)

# Background gradient
ax.set_facecolor('#f0f0f0')

# Ensure everything fits
plt.tight_layout()

plt.show()