import numpy as np
import matplotlib.pyplot as plt

# Define months and product categories
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
categories = ['Electronics', 'Clothing', 'Home Goods', 'Toys', 'Groceries']

# Sales data: rows are product categories, columns are months
sales_data = np.array([
    [200, 150, 250, 300, 350, 400],  # Electronics
    [300, 400, 350, 250, 200, 150],  # Clothing
    [100, 200, 300, 250, 150, 100],  # Home Goods
    [50, 100, 200, 150, 300, 350],   # Toys
    [500, 450, 400, 500, 550, 600]   # Groceries
])

# Calculate cumulative sales data for the line plot
cumulative_sales = np.cumsum(sales_data, axis=1)

# Create a figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 1.2]})

# First subplot: Heatmap
ax1 = axs[0]
cax = ax1.imshow(sales_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')
fig.colorbar(cax, ax=ax1, label='Sales (Units)', shrink=0.8)

ax1.set_title('Retail Heatmap:\nMonthly Sales Distribution Across Categories', fontsize=12, pad=10)
ax1.set_xticks(np.arange(len(months)))
ax1.set_yticks(np.arange(len(categories)))
ax1.set_xticklabels(months, fontsize=9)
ax1.set_yticklabels(categories, fontsize=9)
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

# Display sales values on the heatmap
for i in range(len(categories)):
    for j in range(len(months)):
        ax1.text(j, i, str(sales_data[i, j]), ha='center', va='center', color='black', fontsize=8, fontweight='bold')

# Second subplot: Line plot for cumulative sales
ax2 = axs[1]
for idx, category in enumerate(categories):
    ax2.plot(months, cumulative_sales[idx], marker='o', label=category)

ax2.set_title('Cumulative Sales Trend\nAcross Categories', fontsize=12)
ax2.set_xlabel('Month', fontsize=10)
ax2.set_ylabel('Cumulative Sales (Units)', fontsize=10)
ax2.legend(title='Categories', fontsize=8, title_fontsize=9, loc='upper left', bbox_to_anchor=(1, 1))
ax2.grid(visible=True, linestyle='--', alpha=0.7)

# Enhance layout
plt.tight_layout()

# Show plot
plt.show()