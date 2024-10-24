import matplotlib.pyplot as plt
import numpy as np

# Define battle types and their corresponding impact values
battle_types = ['Land Battles', 'Naval Battles', 'Siege Battles', 'Guerrilla Battles']
impact = [8, 10, 6, 9]  # Impact values from 1 to 10

# Calculate the angles for each sector
num_categories = len(battle_types)
sector_angle = (2 * np.pi) / num_categories
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Repeat the first values to close the plot
impact += impact[:1]
angles += angles[:1]

# Colors for each category
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Create a polar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw bars with proportional height and equal angle width
bars = ax.bar(angles[:-1], impact[:-1], width=sector_angle, color=colors, alpha=0.6)

# Add text annotations for impact values at the end of each sector
for angle, im, color in zip(angles[:-1], impact[:-1], colors):
    ax.text(angle, im + 0.5, f'{im} impact', ha='center', color=color, fontsize=10, fontweight='bold')

# Set chart title and remove y-axis labels
ax.set_title("Impact of Historical Battle Types\n(A Fictional Analysis)", fontsize=14, fontweight='bold')
ax.set_yticklabels([])

# Customize the grid
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend
ax.legend(bars, battle_types, loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Battle Type", fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()