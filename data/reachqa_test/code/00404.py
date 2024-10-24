import matplotlib.pyplot as plt
import numpy as np

# Given data
fruit_sales = {
    'Apples': 2500,
    'Grapes': 1800,
    'Pears': 1200,
    'Plums': 1000,
    'Melons': 1500,
    'Berries': 2000,
}

# Sorting by sales amount to emphasize the best sellers
sorted_fruits = sorted(fruit_sales, key=fruit_sales.get, reverse=True)

# Selecting distinct colors for each bar
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF', '#FFFF99'
]

# Creating a figure with subplots: one for the bar chart and another for the pie chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart subplot
bar_positions = np.arange(len(sorted_fruits))
bar_heights = [fruit_sales[fruit] for fruit in sorted_fruits]
ax1.bar(bar_positions, bar_heights, color=colors)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(sorted_fruits, rotation=45, ha='right')  # Changed '45' to 45
ax1.set_xlabel('Fruit Type')
ax1.set_ylabel('Total Sales ($)')
ax1.set_title('Fresh Produce Sales at the Farmer\'s Market\nSeptember 2023: A Snapshot of Local Agriculture')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
y_ticks = ax1.get_yticks()
ax1.set_yticklabels(['${:,.0f}'.format(y / 1000) + 'K' for y in y_ticks])
for i, v in enumerate(bar_heights):
    ax1.text(i, v + 50, '${:,.0f}'.format(v), color='blue', fontweight='bold', ha='center')

# Pie chart subplot
ax2.pie(fruit_sales.values(), labels=fruit_sales.keys(), colors=colors, autopct='%1.1f%%', startangle=140)
ax2.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax2.set_title('Market Share by Fresh Produce Type')

# Automatically adjust layout to accommodate both subplots
plt.tight_layout()

# Show the updated figure with both subplots
plt.show()