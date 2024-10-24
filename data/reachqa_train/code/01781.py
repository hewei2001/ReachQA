import matplotlib.pyplot as plt
import numpy as np

# Cereal names
cereals = ['Crunchy Flakes', 'Sweetened Oats', 'Fruit Rings', 'Nut Clusters', 'Wheat Squares']

# Nutrient breakdown for each cereal (Carbs, Protein, Fat)
carbohydrates = np.array([30, 28, 25, 22, 35])  # in grams
proteins = np.array([3, 4, 2, 5, 4])  # in grams
fats = np.array([2, 1, 1, 3, 2])  # in grams

# Positions on the X-axis
positions = np.arange(len(cereals))

# Plotting a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Stacked bars
bar1 = ax.bar(positions, carbohydrates, color='goldenrod', label='Carbohydrates', alpha=0.8)
bar2 = ax.bar(positions, proteins, color='skyblue', bottom=carbohydrates, label='Proteins', alpha=0.8)
bar3 = ax.bar(positions, fats, color='salmon', bottom=carbohydrates+proteins, label='Fats', alpha=0.8)

# Add labels, title, and ticks
ax.set_xlabel('Cereal Brands', fontsize=12)
ax.set_ylabel('Nutrient Content (grams)', fontsize=12)
ax.set_title('Nutrient Composition\nin Popular Breakfast Cereals', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(positions)
ax.set_xticklabels(cereals, rotation=45, ha='right', fontsize=10)

# Adding legend
ax.legend(loc='upper right', fontsize=10)

# Add values above bars
for bar in bar1 + bar2 + bar3:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f'{int(height)}g',
        ha='center',
        va='bottom',
        fontsize=9
    )

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()