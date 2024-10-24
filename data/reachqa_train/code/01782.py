import matplotlib.pyplot as plt
import numpy as np

# Cereal names
cereals = ['Crunchy Flakes', 'Sweetened Oats', 'Fruit Rings', 'Nut Clusters', 'Wheat Squares']

# Nutrient breakdown for each cereal (Carbs, Protein, Fat)
carbohydrates = np.array([30, 28, 25, 22, 35])  # in grams
proteins = np.array([3, 4, 2, 5, 4])  # in grams
fats = np.array([2, 1, 1, 3, 2])  # in grams

# Total calorie calculation: 
# Carbs and proteins = 4 kcal/g, Fats = 9 kcal/g
calories = carbohydrates * 4 + proteins * 4 + fats * 9

# Positions on the X-axis
positions = np.arange(len(cereals))

# Plotting a stacked bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked bars for nutrients
bar1 = ax1.bar(positions, carbohydrates, color='goldenrod', label='Carbohydrates', alpha=0.8)
bar2 = ax1.bar(positions, proteins, color='skyblue', bottom=carbohydrates, label='Proteins', alpha=0.8)
bar3 = ax1.bar(positions, fats, color='salmon', bottom=carbohydrates + proteins, label='Fats', alpha=0.8)

# Twin axes for the calorie line plot
ax2 = ax1.twinx()
ax2.plot(positions, calories, color='darkgreen', marker='o', linestyle='-', linewidth=2, markersize=8, label='Total Calories')

# Add labels, titles, and ticks
ax1.set_xlabel('Cereal Brands', fontsize=12)
ax1.set_ylabel('Nutrient Content (grams)', fontsize=12)
ax2.set_ylabel('Total Calories', fontsize=12, color='darkgreen')
ax1.set_title('Nutrient Composition\nand Calorie Count of Popular Breakfast Cereals', fontsize=16, fontweight='bold', pad=20)

# Customize X-axis ticks
ax1.set_xticks(positions)
ax1.set_xticklabels(cereals, rotation=45, ha='right', fontsize=10)

# Legends
bars_legend = ax1.legend(loc='upper left', fontsize=10)
calories_legend = ax2.legend(loc='upper right', fontsize=10)
ax1.add_artist(bars_legend)

# Add values above bars and line plot
for bar in bar1 + bar2 + bar3:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f'{int(height)}g',
        ha='center',
        va='bottom',
        fontsize=9
    )

for i, cal in enumerate(calories):
    ax2.text(
        positions[i], cal + 10, f'{int(cal)} kcal',
        ha='center', va='bottom', fontsize=9, color='darkgreen'
    )

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()