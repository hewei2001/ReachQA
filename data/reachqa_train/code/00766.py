import matplotlib.pyplot as plt
import numpy as np

# Define species habitats
species = ['Fairies', 'Unicorns', 'Phoenixes']

# Define seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Resource distribution data for each species habitat across the seasons
mana_stones = np.array([
    [30, 40, 50, 60],  # Fairies
    [60, 70, 80, 90],  # Unicorns
    [40, 30, 20, 10]   # Phoenixes
])

potion_ingredients = np.array([
    [50, 60, 70, 80],  # Fairies
    [20, 30, 25, 35],  # Unicorns
    [30, 35, 40, 50]   # Phoenixes
])

mystical_relics = np.array([
    [20, 30, 40, 50],  # Fairies
    [30, 20, 15, 20],  # Unicorns
    [50, 55, 60, 70]   # Phoenixes
])

# Set plot size and parameters
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.5
colors = ['#7FC97F', '#BEAED4', '#FDC086']  # Distinct colors for each resource

# Plot stacked bars for each species habitat
for i, species_name in enumerate(species):
    bottom = np.zeros_like(seasons, dtype=float)  # Start stacking from zero
    ax.bar(seasons, mana_stones[i], width, label='Mana Stones' if i == 0 else "", color=colors[0], alpha=0.9, bottom=bottom)
    bottom += mana_stones[i]
    ax.bar(seasons, potion_ingredients[i], width, label='Potion Ingredients' if i == 0 else "", color=colors[1], alpha=0.9, bottom=bottom)
    bottom += potion_ingredients[i]
    ax.bar(seasons, mystical_relics[i], width, label='Mystical Relics' if i == 0 else "", color=colors[2], alpha=0.9, bottom=bottom)

# Labeling and titles
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Resource Allocation (Units)', fontsize=12)
ax.set_title('Magical Forest Conservation:\nResource Allocation in Mystic Woodland', fontsize=16, fontweight='bold', pad=20)

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Resources', fontsize=10)

# Customize grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure space between bars and edges
ax.margins(y=0.1)

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()