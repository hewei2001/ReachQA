import matplotlib.pyplot as plt
import numpy as np

# Data setup
novels = ["Mystic Quest", "Dragon's Flight", "Enchanted Forest", "The Shadow King", "Eternal Light"]
editions_by_decade = np.array([
    [10, 25, 30, 45, 60],  # Mystic Quest
    [15, 20, 35, 50, 55],  # Dragon's Flight
    [5, 15, 25, 40, 45],   # Enchanted Forest
    [0, 10, 20, 30, 40],   # The Shadow King
    [0, 5, 20, 35, 50]     # Eternal Light
])
decades = ["1980s", "1990s", "2000s", "2010s", "2020s"]

# Calculate average editions released per decade
average_editions = editions_by_decade.mean(axis=0)

# Plot setup
fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.15
r = np.arange(len(novels))
colors = plt.cm.viridis(np.linspace(0, 1, len(decades)))

# Plot horizontal bars
for i, (decade, color) in enumerate(zip(decades, colors)):
    ax.barh(r + i * bar_width, editions_by_decade[:, i], height=bar_width, label=decade, color=color)

# Overlay line plot for average editions
ax2 = ax.twinx()
ax2.plot(average_editions, r + bar_width * (len(decades) / 2), marker='o', color='black', linestyle='-', linewidth=2, label='Average Editions')
ax2.set_ylabel('Average Number of Editions')

# Customize plot
ax.set_yticks(r + bar_width * (len(decades) / 2 - 0.5))
ax.set_yticklabels(novels)
ax.set_xlabel('Number of Editions Released', fontsize=12)
ax.set_title('Legendary Fantasy Novels:\nPopularity Across Decades with Average Editions Overlay', fontsize=16, fontweight='bold', pad=20)

# Add value labels on bars
for i, y in enumerate(r):
    for j in range(len(decades)):
        ax.text(editions_by_decade[i, j] + 1, y + j * bar_width, str(editions_by_decade[i, j]), va='center', fontsize=9)

# Add legends
ax.legend(title="Decades", loc='upper right', fontsize=10)
ax2.legend(loc='lower left', fontsize=10)

# Final adjustments
ax.invert_yaxis()
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show plot
plt.show()