import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Define creatures and parameters
creatures = ["Frost Gryphon", "Ember Dragon", "Shadow Panther", "Thunder Elk", "Crystal Serpent"]
parameters = ["Flight Agility", "Fire Breath", "Stealth", "Thunderous Roar", "Crystal Manipulation"]

# Creature abilities on a 0 to 10 scale
ability_data = np.array([
    [8, 5, 9, 6, 4],
    [6, 10, 4, 8, 5],
    [5, 6, 10, 5, 7],
    [7, 4, 5, 9, 6],
    [5, 6, 8, 4, 10]
])

# Number of variables (parameters)
num_vars = len(parameters)

# Compute angles for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Define a color palette
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Function to plot each creature's data
for idx, (data, color) in enumerate(zip(ability_data, colors)):
    data = np.concatenate((data, [data[0]]))
    ax.plot(angles, data, linewidth=2, linestyle='solid', marker='o', color=color, label=creatures[idx])
    ax.fill(angles, data, color=color, alpha=0.25)
    for angle, val in zip(angles, data):
        ax.text(angle, val + 0.5, f'{val:.0f}', horizontalalignment='center', verticalalignment='center', fontsize=8, color=color)

# Add parameter labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(parameters, fontsize=12, fontweight='bold')

# Customize grid and radial labels
ax.set_yticks(range(1, 11))
ax.set_yticklabels([])
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)

# Add a title and subtitle
ax.set_title("Fantasy Ecosystems:\nLegendary Creature Abilities Comparison", fontsize=16, fontweight='bold', va='bottom')

# Add a legend outside the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1.1), title="Creatures", fontsize=10)

# Add background gradient
ax.set_facecolor('#f7f7f7')

# Automatically adjust layout
plt.tight_layout()

# Show the radar chart
plt.show()