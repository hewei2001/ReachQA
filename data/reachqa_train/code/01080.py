import matplotlib.pyplot as plt
import numpy as np

# Define expanded product categories and their respective quarterly sales data (in thousands of dollars)
categories = ["Electronics", "Fashion", "Home & Kitchen", "Books", "Health & Beauty", "Sports & Outdoors", "Toys", "Automotive", "Garden", "Office Supplies"]
regions = ["North", "South", "East", "West"]
quarterly_sales = np.array([
    [120, 90, 150, 60, 70, 110, 80, 95, 105, 115],  # Q1
    [130, 100, 160, 55, 80, 120, 85, 100, 115, 125],  # Q2
    [140, 95, 155, 65, 75, 115, 90, 105, 120, 130],  # Q3
    [135, 85, 165, 70, 85, 125, 95, 110, 125, 135],  # Q4
])

# Define a color palette for the categories
colors = ['#FF5733', '#33FFCE', '#FF33A1', '#335BFF', '#B833FF', '#33FF57', '#FFC300', '#581845', '#900C3F', '#DAF7A6']

# Create figure and axes for subplots
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), constrained_layout=True)

# Subplot 1: Quarterly Sales by Category
axs[0].set_title('Quarterly Sales by Product Category and Region\n(in Thousands of Dollars)', fontsize=16, fontweight='bold')
x = np.arange(len(categories))

# Stack bars for each quarter
for i, (region_sales, color) in enumerate(zip(quarterly_sales, colors)):
    axs[0].bar(x + i*0.15, region_sales, width=0.15, label=f'Q{i+1}', color=color)

# Set labels and ticks
axs[0].set_xlabel('Product Categories', fontsize=12)
axs[0].set_ylabel('Sales (in $K)', fontsize=12)
axs[0].set_xticks(x + 0.15)
axs[0].set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
axs[0].legend(title='Quarter')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Cumulative Annual Sales
annual_sales = np.sum(quarterly_sales, axis=0)

axs[1].bar(categories, annual_sales, color=colors)
axs[1].set_title('Cumulative Annual Sales by Product Category\n(in Thousands of Dollars)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Product Categories', fontsize=12)
axs[1].set_ylabel('Cumulative Sales (in $K)', fontsize=12)
axs[1].set_xticklabels(categories, rotation=45, ha='right', fontsize=10)

# Annotate each bar with the cumulative sales figure
for bar, sale in zip(axs[1].containers[0], annual_sales):
    yval = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width()/2, yval + 10, f"${sale}K", ha='center', va='bottom', fontsize=10, color='black')

# Display the plot
plt.show()