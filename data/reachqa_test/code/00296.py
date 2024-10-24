import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Patch

# Genres and their sales data (in millions of units)
genres = ['Action', 'Role-Playing', 'Strategy', 'Simulation', 'Sports']
sales_data = [250, 180, 120, 150, 200]  # Total sales from 2013 to 2023

# Setting up positions for the bars
x_pos = np.arange(len(genres))

# Create a figure and a bar chart with two subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot bars with patterns (hatching)
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFDB33']
hatches = ['/', '\\', '|', '-', '+']

# Create bars with gradient-like effect using hatching
bars = ax.bar(x_pos, sales_data, color=colors, alpha=0.9, width=0.6, hatch=hatches[0])

# Annotate each bar with its height (sales in millions) and percentage contribution
total_sales = sum(sales_data)
for i, bar in enumerate(bars):
    height = bar.get_height()
    percentage = (height / total_sales) * 100
    ax.annotate(f'{height}M\n({percentage:.1f}%)',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

# Title and axis labels with adjusted text
ax.set_title('Decade of Gaming: \nSales Evolution by Genre\n(2013-2023)', fontsize=16, fontweight='bold', pad=30)
ax.set_xlabel('Video Game Genre', fontsize=13, labelpad=15)
ax.set_ylabel('Sales in Millions of Units', fontsize=13, labelpad=15)

# Set x-ticks and labels
ax.set_xticks(x_pos)
ax.set_xticklabels(genres, fontsize=12)

# Customize y-axis limits and grid lines
ax.set_ylim(0, 300)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add a legend
legend_elements = [Patch(facecolor=colors[i], hatch=hatches[i], label=genres[i]) for i in range(len(genres))]
ax.legend(handles=legend_elements, title='Genres', loc='upper right', fontsize=10)

# Display horizontal benchmark line for average sales
average_sales = total_sales / len(sales_data)
ax.axhline(y=average_sales, color='gray', linestyle='--', linewidth=1.2)
ax.text(len(genres) - 0.5, average_sales + 5, 'Avg Sales', fontsize=10, va='center', ha='center', backgroundcolor='w')

# Enhance layout for better readability
plt.tight_layout()

# Display the plot
plt.show()