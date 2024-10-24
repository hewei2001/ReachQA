import matplotlib.pyplot as plt
import numpy as np

# Define months and sales data for each product type
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Sales data in units for each product category over the year
# Fruits, Vegetables, and Grains sales respectively
fruits_sales = np.array([120, 130, 140, 160, 180, 200, 220, 210, 190, 170, 150, 130])
vegetables_sales = np.array([150, 160, 170, 180, 200, 220, 210, 200, 190, 180, 170, 160])
grains_sales = np.array([180, 190, 200, 210, 220, 230, 240, 230, 220, 210, 200, 190])

# Variability (error) data for each category
fruits_error = np.array([10, 15, 12, 18, 20, 15, 22, 18, 15, 12, 10, 14])
vegetables_error = np.array([12, 10, 15, 20, 18, 22, 15, 20, 18, 15, 12, 10])
grains_error = np.array([15, 12, 18, 20, 22, 18, 20, 15, 22, 18, 15, 12])

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each line with error bars
plt.errorbar(months, fruits_sales, yerr=fruits_error, fmt='-o', label='Fruits',
             color='forestgreen', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, vegetables_sales, yerr=vegetables_error, fmt='-s', label='Vegetables',
             color='darkorange', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, grains_sales, yerr=grains_error, fmt='-^', label='Grains',
             color='royalblue', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)

# Add titles and labels
plt.title("Monthly Sales Trends of Organic Products\nwith Seasonal Impact Analysis", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in units)", fontsize=12)

# Displaying a legend
plt.legend(loc='upper right', title='Product Categories')

# Grid and aesthetic improvements
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()