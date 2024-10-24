import matplotlib.pyplot as plt
import numpy as np

# Define the continents and sub-regions
regions = [
    'Northern Africa', 'Southern Africa', 'North America', 'South America',
    'East Asia', 'South Asia', 'Western Europe', 'Eastern Europe',
    'Australia', 'New Zealand'
]

# Define the fruit categories
fruit_categories = ['Citrus Fruits', 'Berries', 'Tropical Fruits', 'Stone Fruits']

# Define the consumption rates for each region and fruit category
consumption_rates = [
    [15, 20, 30, 35],  # Northern Africa
    [25, 15, 40, 20],  # Southern Africa
    [20, 25, 25, 30],  # North America
    [10, 35, 30, 25],  # South America
    [30, 20, 25, 25],  # East Asia
    [35, 15, 20, 30],  # South Asia
    [25, 30, 20, 25],  # Western Europe
    [15, 25, 30, 30],  # Eastern Europe
    [30, 10, 35, 25],  # Australia
    [20, 30, 25, 25]   # New Zealand
]

# Colors for each fruit category
colors = ['#FF4500', '#ADFF2F', '#FF69B4', '#9370DB']

# Set up the figure and axis for a more complex chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define positions for the bars
x_positions = np.arange(len(regions))
bar_width = 0.7

# Create stacked bars with annotations
bottoms = np.zeros(len(regions))

for i, (fruit_category, color) in enumerate(zip(fruit_categories, colors)):
    values = [rate[i] for rate in consumption_rates]
    ax.bar(x_positions, values, bar_width, label=fruit_category, color=color, bottom=bottoms)
    bottoms += values
    
    for j, val in enumerate(values):
        ax.text(j, bottoms[j] - val / 2, f"{val}%", ha='center', va='center', fontsize=9, color='white')

# Customize the plot
ax.set_xlabel('Region', fontsize=12, labelpad=10)
ax.set_ylabel('Consumption Rate (%)', fontsize=12, labelpad=10)
ax.set_title('Fruit Consumption Patterns Across Regions\nDetailed Analysis for 2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_positions)
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.set_ylim(0, 100)
ax.legend(title='Fruit Category', loc='upper left', fontsize=10, title_fontsize=11)

# Enhance layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()