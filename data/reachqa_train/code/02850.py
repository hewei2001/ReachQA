import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data representing the nectar (in grams) collected by bee colonies in various floral zones
data = [
    [100, 120, 130, 140, 115, 125, 135],  # Meadow
    [80, 95, 100, 110, 120, 105],         # Orchard
    [50, 65, 70, 75, 60, 55],             # Forest
    [70, 85, 90, 100, 80, 95],            # Urban Garden
    [130, 145, 155, 160, 150, 140]        # Wetland
]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Create a boxplot and add a violin plot overlay
sns.violinplot(data=data, ax=ax, inner=None, linewidth=1.5, alpha=0.3, palette="muted", zorder=1)
sns.boxplot(data=data, ax=ax, whis=[5, 95], width=0.3, palette="husl", boxprops=dict(alpha=0.6), zorder=2)

# Adding jittered points to show individual data distributions
for i in range(len(data)):
    y = data[i]
    x = np.random.normal(i, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.7, color='black', edgecolor='white', zorder=3)

# Title and labels with automatic wrapping for long text
ax.set_title('Nectar Collection Patterns:\nInsights into Bee Colonies Across Various Floral Zones',
             fontsize=16, fontweight='bold', ha='center')
ax.set_ylabel('Nectar Collected (grams)', fontsize=12)
ax.set_xticklabels(['Meadow', 'Orchard', 'Forest', 'Urban Garden', 'Wetland'], fontsize=10)

# Enhancing grid and background for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f0f0f0')

# Annotating key statistics (median) for each category
medians = [np.median(zone) for zone in data]
for i, median in enumerate(medians):
    ax.text(i, median + 3, f'Med: {median}', ha='center', fontsize=9, color='black')

# Setting tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()