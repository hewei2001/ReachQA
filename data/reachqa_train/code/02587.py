import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)

# Sales data (in thousands) for each product category with seasonal patterns
organic_cotton_sales = np.array([75, 82, 85, 80, 95, 110, 130, 125, 105, 95, 85, 78])
recycled_polyester_sales = np.array([60, 62, 68, 70, 82, 100, 115, 110, 90, 80, 70, 65])
bamboo_fabric_sales = np.array([40, 45, 50, 55, 60, 75, 85, 83, 78, 68, 58, 50])

# Error margins to reflect sales variability
organic_cotton_error = np.array([5, 4, 6, 5, 7, 6, 8, 9, 7, 5, 6, 5])
recycled_polyester_error = np.array([3, 4, 5, 5, 6, 7, 7, 8, 6, 5, 4, 3])
bamboo_fabric_error = np.array([2, 3, 3, 4, 4, 5, 6, 6, 5, 4, 3, 3])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line with error bars for each product category
ax.errorbar(months, organic_cotton_sales, yerr=organic_cotton_error, label='Organic Cotton', fmt='-o', capsize=5, color='green', ecolor='lightgreen', alpha=0.8)
ax.errorbar(months, recycled_polyester_sales, yerr=recycled_polyester_error, label='Recycled Polyester', fmt='-s', capsize=5, color='blue', ecolor='lightblue', alpha=0.8)
ax.errorbar(months, bamboo_fabric_sales, yerr=bamboo_fabric_error, label='Bamboo Fabrics', fmt='-d', capsize=5, color='orange', ecolor='peachpuff', alpha=0.8)

# Customize the plot
ax.set_title("Monthly Sales Performance with Seasonal Fluctuations\nin the Eco-friendly Clothing Industry (2023)", fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales (in thousands)', fontsize=14)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Add a legend
ax.legend(title='Product Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, frameon=False)

# Set grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()