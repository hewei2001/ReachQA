import matplotlib.pyplot as plt
import numpy as np

# Original coffee blend data
blends = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Macchiato', 'Flat White']
percentages = [20, 25, 15, 10, 12, 8, 10]
colors = ['#8B4513', '#D2B48C', '#A52A2A', '#D2691E', '#8A3324', '#CD853F', '#F4A460']

# Additional data for the bar chart (average customer ratings out of 5)
ratings = [4.8, 4.5, 4.6, 4.2, 4.7, 4.3, 4.4]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 3]})

# First subplot: Donut chart for coffee blends
wedges, texts, autotexts = axes[0].pie(percentages, labels=blends, autopct='%1.1f%%', startangle=90,
                                       colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'),
                                       textprops={'fontsize': 10, 'weight': 'bold'}, pctdistance=0.85)
axes[0].set_title('The Artistry of Coffee Blends\nin Caféville', fontsize=16, fontweight='bold')
axes[0].text(0, 0, 'Caféville\nCoffee Culture', ha='center', va='center', fontsize=12, weight='bold', color='grey')

# Second subplot: Bar chart for average customer ratings
axes[1].bar(blends, ratings, color=colors, edgecolor='black')
axes[1].set_title('Customer Ratings\nof Coffee Blends', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Coffee Blends', fontsize=12)
axes[1].set_ylabel('Average Rating', fontsize=12)
axes[1].set_ylim(4, 5)
axes[1].set_yticks(np.arange(4, 5.1, 0.2))
for i, v in enumerate(ratings):
    axes[1].text(i, v + 0.02, f"{v:.1f}", ha='center', va='bottom', fontsize=10, weight='bold')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()