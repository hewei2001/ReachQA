import numpy as np
import matplotlib.pyplot as plt

# Define categories and creatures data
categories = ['Speed', 'Strength', 'Wisdom', 'Camouflage', 'Healing']
n_categories = len(categories)

creatures = {
    'Elven Scout': [9, 5, 7, 6, 4],
    'Forest Troll': [4, 9, 5, 3, 5],
    'Owl Guardian': [6, 5, 10, 4, 4],
    'Camouflaged Dryad': [5, 4, 6, 10, 3],
    'Healing Unicorn': [4, 5, 5, 4, 10]
}

# Related dataset for comparison (e.g., Desert Creatures)
related_creatures = {
    'Desert Sprite': [8, 4, 6, 5, 7],
    'Sand Golem': [3, 8, 4, 2, 6],
    'Phoenix': [7, 6, 9, 4, 5],
    'Mimic Cactus': [5, 3, 7, 9, 4],
    'Healing Sphinx': [4, 6, 6, 3, 9]
}

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=True), constrained_layout=True)

# Radar Chart
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]

for creature, ability_scores in creatures.items():
    scores = ability_scores + ability_scores[:1]
    ax1.plot(angles, scores, linewidth=2, linestyle='solid', label=creature)
    ax1.fill(angles, scores, alpha=0.1)

ax1.set_yticklabels([])
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=10)
ax1.set_ylim(0, 10)
ax1.set_title("Abilities of Mystical Forest Creatures", size=13, fontweight='bold', pad=20)
ax1.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='small')

# Grouped Bar Chart
index = np.arange(n_categories)
bar_width = 0.35

for i, (creature, scores) in enumerate(related_creatures.items()):
    ax2.bar(index + i * bar_width, scores, bar_width, label=creature)

ax2.set_xticks(index + bar_width * (len(related_creatures) / 2 - 0.5))
ax2.set_xticklabels(categories, fontsize=10)
ax2.set_ylim(0, 10)
ax2.set_title("Traits of Mythical Desert Creatures", size=13, fontweight='bold', pad=20)
ax2.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='small')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()