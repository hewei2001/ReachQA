import matplotlib.pyplot as plt
import numpy as np

# Data for the stacked bar chart
platforms = ['Amazon', 'eBay', 'Walmart', 'Alibaba', 'Etsy']
electronics_sales = np.array([120, 85, 65, 90, 45])  # in thousands
fashion_sales = np.array([200, 150, 100, 80, 60])  # in thousands
home_goods_sales = np.array([75, 60, 50, 40, 30])  # in thousands
books_sales = np.array([50, 40, 45, 35, 25])  # in thousands

# Data for the second plot (growth rates)
growth_rates = np.array([10, 15, 5, 20, 10])  # in percentage

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Create the stacked bar chart
x = np.arange(len(platforms))
ax1.bar(x, electronics_sales, color='dodgerblue', label='Electronics', alpha=0.85)
ax1.bar(x, fashion_sales, bottom=electronics_sales, color='orange', label='Fashion', alpha=0.85)
ax1.bar(x, home_goods_sales, bottom=electronics_sales + fashion_sales, color='lightgreen', label='Home Goods', alpha=0.85)
ax1.bar(x, books_sales, bottom=electronics_sales + fashion_sales + home_goods_sales, color='salmon', label='Books', alpha=0.85)

# Add labels and title for the first plot
ax1.set_xlabel('E-Commerce Platforms', fontsize=14)
ax1.set_ylabel('Units Sold (in thousands)', fontsize=14)
ax1.set_title('E-Commerce Sales by Product Type in Q1 2023', fontsize=16, pad=20)
ax1.set_xticks(x)
ax1.set_xticklabels(platforms, fontsize=12, rotation=45, ha='right')
ax1.set_yticks(ax1.get_yticks())  # Fixed
ax1.set_ylim(0, 500)
ax1.legend(title='Product Types', fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Create the line chart for growth rates
ax2.plot(platforms, growth_rates, marker='o', color='purple', label='Growth Rate (%)', linewidth=2, markersize=8)
ax2.set_xlabel('E-Commerce Platforms', fontsize=14)
ax2.set_ylabel('Growth Rate (%)', fontsize=14)
ax2.set_title('Growth Rate of Sales by Platform\nQ1 2023', fontsize=16, pad=20)
ax2.set_ylim(0, 25)
ax2.set_yticks(ax2.get_yticks())  # Fixed
ax2.set_xticks(platforms)  # Fixed
ax2.set_xticklabels(platforms, fontsize=12, rotation=45, ha='right')
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(title='Sales Growth', fontsize=12)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()