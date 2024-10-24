import matplotlib.pyplot as plt
import numpy as np

# Define character names
characters = ['Knight Lancelot', 'Ranger Elowen', 'Mage Alaric', 'Paladin Braelyn']

# Define the skill domains
categories = ['Strength', 'Agility', 'Intelligence', 'Defense', 'Magic']
num_vars = len(categories)

# Character abilities data
data = {
    'Knight Lancelot': [9, 5, 4, 8, 3],
    'Ranger Elowen': [5, 9, 6, 4, 7],
    'Mage Alaric': [3, 5, 9, 4, 10],
    'Paladin Braelyn': [7, 4, 5, 9, 6]
}

# Calculate angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Append first data point to close the plot
angles += angles[:1]

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each character
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot each character's data
for i, (character, values) in enumerate(data.items()):
    values += values[:1]  # Repeat the first value to close the circle
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=character, color=colors[i])
    ax.fill(angles, values, alpha=0.25, color=colors[i])

# Add labels for each axis
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=12)

# Add a title and legend
plt.title("Aeloria Heroes: Comparative Analysis\nof Character Abilities", size=15, fontweight='bold', va='top', pad=40)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Improve layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()