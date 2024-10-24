import matplotlib.pyplot as plt
import numpy as np

# Mythical creatures and their folklore popularity scores
creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Kraken', 'Griffins', 'Mermaids', 'Minotaurs']
popularity_scores = [85, 70, 90, 60, 75, 65, 55]

# Synthetic data for popularity trend over five years
years = np.arange(2019, 2024)
popularity_trends = {
    'Dragons': [80, 82, 85, 87, 89],
    'Phoenix': [65, 68, 70, 72, 74],
    'Unicorns': [88, 89, 90, 91, 92],
    'Kraken': [55, 58, 60, 62, 64],
    'Griffins': [70, 73, 75, 77, 79],
    'Mermaids': [60, 62, 65, 67, 69],
    'Minotaurs': [50, 52, 55, 57, 59]
}

# Colors for each creature, consistent between plots
colors = ['#FF5733', '#FFC300', '#FF33FF', '#33DFFF', '#DAF7A6', '#33FF57', '#8E44AD']

# Create the figure and axes for two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14, 7))

# Bar plot
x_pos = np.arange(len(creatures))
bars = ax1.bar(x_pos, popularity_scores, color=colors, edgecolor='black')
ax1.set_title("Ancient Mythical Creatures\nFolklore Legend Popularity", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Mythical Creatures", fontsize=12)
ax1.set_ylabel("Popularity Score (Out of 100)", fontsize=12)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(creatures, fontsize=10, rotation=30, ha='right')

for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='white')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.set_ylim(0, 100)

# Line plot
for creature, trend in popularity_trends.items():
    ax2.plot(years, trend, marker='o', label=creature)

ax2.set_title("Trend of Mythical Creatures' Popularity (2019-2023)", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Popularity Score", fontsize=12)
ax2.legend(title="Creatures", fontsize=9, title_fontsize='10', loc='upper left', bbox_to_anchor=(1, 1))
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Display the plot
plt.show()