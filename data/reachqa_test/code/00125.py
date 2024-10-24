import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Define the months and styles
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
styles = ['70s Boho Chic', '80s Bold Prints', '90s Grunge Revival']

# Monthly sales data (in thousands)
sales_data = np.array([
    [10, 12, 15, 18, 16, 20, 22, 24, 26, 28, 30, 35],  # 70s Boho Chic
    [5, 7, 8, 10, 12, 15, 17, 18, 19, 20, 21, 23],     # 80s Bold Prints
    [8, 9, 11, 12, 14, 13, 15, 18, 20, 22, 23, 25]     # 90s Grunge Revival
])

# Total annual sales for each style
total_sales = sales_data.sum(axis=1)

# Define colors for each style
colors = ['#FF6F61', '#6B5B95', '#88B04B']

# Set up the figure with GridSpec
fig = plt.figure(figsize=(15, 8))
gs = GridSpec(1, 2, figure=fig, width_ratios=[2, 1])

# Line chart for monthly sales trends
ax1 = fig.add_subplot(gs[0, 0])
for idx, (style, color) in enumerate(zip(styles, colors)):
    ax1.plot(months, sales_data[idx], marker='o', color=color, label=style, linewidth=2, markersize=8, alpha=0.8)

ax1.set_title('The Renaissance of Vintage Fashion:\nMonthly Sales Trends of Retro Apparel in 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Sales (Thousands)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Retro Styles', loc='upper left', fontsize=10)

# Data labels for the line chart
for idx in range(len(styles)):
    for month_idx, value in enumerate(sales_data[idx]):
        ax1.text(month_idx, value + 0.5, f'{value}', ha='center', va='bottom', fontsize=9, color=colors[idx])

# Bar chart for total annual sales
ax2 = fig.add_subplot(gs[0, 1])
bar_positions = np.arange(len(styles))
ax2.bar(bar_positions, total_sales, color=colors, alpha=0.7, edgecolor='black')

ax2.set_title('Total Annual Sales by Style', fontsize=14, fontweight='bold')
ax2.set_xlabel('Retro Styles', fontsize=12)
ax2.set_ylabel('Total Sales (Thousands)', fontsize=12)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(styles, rotation=15, ha='right')

# Annotate bars with total sales
for idx, total in enumerate(total_sales):
    ax2.text(idx, total + 1, f'{total}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()