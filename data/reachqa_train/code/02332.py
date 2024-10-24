import matplotlib.pyplot as plt
import numpy as np

# Enhanced data for mythical creatures and their various abilities
creatures = ['Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Mermaid']
attributes = {
    'strength': [95, 70, 60, 85, 50],
    'speed': [80, 90, 65, 75, 60],
    'intelligence': [90, 85, 80, 70, 95],
    'magic': [100, 85, 75, 80, 90],
    'wisdom': [85, 78, 88, 65, 82],
    'agility': [75, 92, 68, 73, 80]
}

# Normalize and weight the attributes
weights = {
    'strength': 1.2,
    'speed': 1.0,
    'intelligence': 1.1,
    'magic': 1.3,
    'wisdom': 1.0,
    'agility': 0.9
}
normalized_power = {}
for creature in creatures:
    normalized_power[creature] = sum(
        (attributes[attr][idx] / 100) * weights[attr]
        for attr, idx in zip(attributes, range(len(creatures)))
    )

# Calculate total normalized power levels
total_power = np.array([normalized_power[creature] for creature in creatures])

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))

# Colors for each attribute
attribute_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']

# Plot stacked bars for each attribute
bottoms = np.zeros(len(creatures))
for idx, (attr, color) in enumerate(zip(attributes, attribute_colors)):
    values = np.array(attributes[attr])
    ax.barh(creatures, values, left=bottoms, color=color, edgecolor='black', label=attr)
    bottoms += values

# Annotate each total power level
for i, (creature, power) in enumerate(normalized_power.items()):
    ax.annotate(f'{total_power[i]:.2f}',
                xy=(total_power[i], i),
                xytext=(5, 0),
                textcoords='offset points',
                ha='left', va='center', fontsize=10, fontweight='bold')

# Set title and labels
ax.set_title('Power Levels of Mythical Creatures\nin the Realm of Eldoria', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Total Attribute Value (Normalized)', fontsize=12)
ax.set_ylabel('Mythical Creature', fontsize=12)

# Add legend
ax.legend(title='Attributes', bbox_to_anchor=(1.05, 1), loc='upper left')

# Improve layout and visibility
plt.tight_layout()

# Display the plot
plt.show()