import matplotlib.pyplot as plt
import numpy as np

# Define months and sales data for each product type
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Sales data in units for each product category over the year
fruits_sales = np.array([120, 130, 140, 160, 180, 200, 220, 210, 190, 170, 150, 130])
vegetables_sales = np.array([150, 160, 170, 180, 200, 220, 210, 200, 190, 180, 170, 160])
grains_sales = np.array([180, 190, 200, 210, 220, 230, 240, 230, 220, 210, 200, 190])

# Variability (error) data for each category
fruits_error = np.array([10, 15, 12, 18, 20, 15, 22, 18, 15, 12, 10, 14])
vegetables_error = np.array([12, 10, 15, 20, 18, 22, 15, 20, 18, 15, 12, 10])
grains_error = np.array([15, 12, 18, 20, 22, 18, 20, 15, 22, 18, 15, 12])

# Calculate cumulative sales for all products
cumulative_sales = fruits_sales + vegetables_sales + grains_sales

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each line with error bars
ax1.errorbar(months, fruits_sales, yerr=fruits_error, fmt='-o', label='Fruits',
             color='forestgreen', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
ax1.errorbar(months, vegetables_sales, yerr=vegetables_error, fmt='-s', label='Vegetables',
             color='darkorange', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
ax1.errorbar(months, grains_sales, yerr=grains_error, fmt='-^', label='Grains',
             color='royalblue', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)

# Add a secondary y-axis to show cumulative sales
ax2 = ax1.twinx()
ax2.plot(months, cumulative_sales, 'p-', color='mediumpurple', linewidth=2, label='Cumulative Sales', alpha=0.7)
ax2.set_ylabel('Cumulative Sales (in units)', color='mediumpurple', fontsize=12)
ax2.tick_params(axis='y', labelcolor='mediumpurple')

# Enhance the plot with a title and labels
ax1.set_title("Monthly Sales Trends of Organic Products\nHighlighting Cumulative Trends and Variability", fontsize=16, pad=20)
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Sales (in units)", fontsize=12)

# Add annotations for significant peaks or changes
ax1.annotate('Peak Sales',
             xy=('Jun', 230), xytext=('May', 250),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

# Displaying legends for both y-axes
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10, frameon=False)

# Grid and aesthetic improvements
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(months)
ax1.set_xticklabels(months, fontsize=11)
ax1.yaxis.set_tick_params(labelsize=11)
ax2.yaxis.set_tick_params(labelsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()