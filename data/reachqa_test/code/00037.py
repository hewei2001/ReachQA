import matplotlib.pyplot as plt
import numpy as np

# Extended data with categories
dishes = [
    "Elven Stew", "Elven Salad", "Dwarf Bread", "Dwarf Ale",
    "Fairy Tea", "Fairy Cake", "Dragon Pie", "Dragon Flame Soup",
    "Goblin Delight", "Goblin Brew"
]
popularity = [150, 90, 80, 110, 100, 130, 120, 140, 90, 85]
average_ratings = [4.2, 3.9, 3.5, 4.8, 4.5, 4.1, 4.7, 4.3, 3.8, 4.0]

# Categories for bars (e.g., race or type of dish)
categories = ["Elven", "Elven", "Dwarven", "Dwarven", "Fairy", "Fairy", "Dragon", "Dragon", "Goblin", "Goblin"]
category_colors = {
    "Elven": '#4CAF50', "Dwarven": '#FFEB3B', "Fairy": '#9C27B0',
    "Dragon": '#FF5722', "Goblin": '#FFC107'
}

# Create bar chart with grouped bars
fig, ax = plt.subplots(figsize=(14, 8))
x_positions = np.arange(len(dishes))

# Plot bars with category colors and add error bars
bar_width = 0.4
for i, (dish, pop, cat) in enumerate(zip(dishes, popularity, categories)):
    ax.bar(x_positions[i], pop, color=category_colors[cat], width=bar_width, label=cat if i in (0, 2, 4, 6, 8) else "")
    ax.errorbar(x_positions[i], pop, yerr=pop * 0.1, fmt='none', ecolor='gray', capsize=5)

# Annotate bars with popularity values and average ratings
for bar in ax.patches:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9, color='black')

# Secondary axis to display ratings
ax2 = ax.twinx()
ax2.plot(x_positions, average_ratings, 'k--o', label='Average Rating', color='blue')
ax2.set_ylim(3, 5)
ax2.set_ylabel('Average Rating (1 to 5)', color='blue', fontsize=12)

# Add legends
ax.legend(title='Category', loc='upper left')
ax2.legend(loc='upper right')

# Titles and labels
ax.set_title('Popularity and Ratings of Magical Dishes\nat the Talendoria Harvest Festival', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Guests Sampling', fontsize=12)

# Set x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(dishes, rotation=45, ha='right', fontsize=10)

# Grid and layout adjustments
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
plt.tight_layout()

# Display the chart
plt.show()