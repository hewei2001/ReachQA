import matplotlib.pyplot as plt
import numpy as np

# Define the novels and corresponding editions released each decade
novels = ["Mystic Quest", "Dragon's Flight", "Enchanted Forest", "The Shadow King", "Eternal Light"]
editions_by_decade = np.array([
    [10, 25, 30, 45, 60],  # Mystic Quest
    [15, 20, 35, 50, 55],  # Dragon's Flight
    [5, 15, 25, 40, 45],   # Enchanted Forest
    [0, 10, 20, 30, 40],   # The Shadow King
    [0, 5, 20, 35, 50]     # Eternal Light
])

# Define the decades
decades = ["1980s", "1990s", "2000s", "2010s", "2020s"]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define the bar width
bar_width = 0.15

# Position of bars on y-axis
r = np.arange(len(novels))

# Colors for the bars
colors = plt.cm.viridis(np.linspace(0, 1, len(decades)))

# Plot each decade as a series of horizontal bars
for i, (decade, color) in enumerate(zip(decades, colors)):
    ax.barh(r + i * bar_width, editions_by_decade[:, i], height=bar_width, label=decade, color=color)

# Add labels, title, and customize ticks
ax.set_yticks(r + bar_width * (len(decades) / 2 - 0.5))
ax.set_yticklabels(novels)
ax.set_xlabel('Number of Editions Released', fontsize=12)
ax.set_title('Legendary Fantasy Novels:\nPopularity Across Decades', fontsize=16, fontweight='bold')

# Add value labels on the bars
for i, y in enumerate(r):
    for j in range(len(decades)):
        ax.text(editions_by_decade[i, j] + 1, y + j * bar_width, str(editions_by_decade[i, j]), va='center', fontsize=9)

# Add a legend
ax.legend(title="Decades", loc='upper right', fontsize=10)

# Invert y-axis for readability
ax.invert_yaxis()

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()