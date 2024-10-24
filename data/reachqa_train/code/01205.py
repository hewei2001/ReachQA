import matplotlib.pyplot as plt
import numpy as np

# Expanded battle types and their corresponding impact values
battle_types = ['Land Battles', 'Naval Battles', 'Siege Battles', 'Guerrilla Battles', 
                'Aerial Battles', 'Cyber Battles', 'Space Battles']
impact_medieval = [8, 10, 6, 9, 4, 2, 0]  # Impact values for medieval scenarios
impact_modern = [5, 7, 3, 8, 9, 10, 6]    # Impact values for modern scenarios

# Calculate the angles for each sector
num_categories = len(battle_types)
sector_angle = (2 * np.pi) / num_categories
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Repeat the first values to close the plot
impact_medieval += impact_medieval[:1]
impact_modern += impact_modern[:1]
angles += angles[:1]

# Colors for each category
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF69B4', '#20B2AA']

# Create a polar plot with two subplots
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), nrows=1, ncols=2)

# Medieval scenario
bars_medieval = ax[0].bar(angles[:-1], impact_medieval[:-1], width=sector_angle, color=colors, alpha=0.6, label='Medieval Impact')
ax[0].set_title("Medieval Era\nImpact Analysis", fontsize=12, fontweight='bold', va='bottom')
for angle, im, color in zip(angles[:-1], impact_medieval[:-1], colors):
    ax[0].text(angle, im + 0.5, f'{im}', ha='center', color=color, fontsize=8)

# Modern scenario
bars_modern = ax[1].bar(angles[:-1], impact_modern[:-1], width=sector_angle, color=colors, alpha=0.6, label='Modern Impact')
ax[1].set_title("Modern Era\nImpact Analysis", fontsize=12, fontweight='bold', va='bottom')
for angle, im, color in zip(angles[:-1], impact_modern[:-1], colors):
    ax[1].text(angle, im + 0.5, f'{im}', ha='center', color=color, fontsize=8)

# Set grid, legend, and remove y-axis labels
for a in ax:
    a.set_yticklabels([])
    a.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)
    a.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Battle Types", fontsize=9)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()