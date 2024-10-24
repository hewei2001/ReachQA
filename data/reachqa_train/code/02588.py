import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Months of the year
months = np.arange(1, 13)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Sales data (in thousands) for each product category with seasonal patterns
organic_cotton_sales = np.array([75, 82, 85, 80, 95, 110, 130, 125, 105, 95, 85, 78])
recycled_polyester_sales = np.array([60, 62, 68, 70, 82, 100, 115, 110, 90, 80, 70, 65])
bamboo_fabric_sales = np.array([40, 45, 50, 55, 60, 75, 85, 83, 78, 68, 58, 50])

# Error margins
organic_cotton_error = np.array([5, 4, 6, 5, 7, 6, 8, 9, 7, 5, 6, 5])
recycled_polyester_error = np.array([3, 4, 5, 5, 6, 7, 7, 8, 6, 5, 4, 3])
bamboo_fabric_error = np.array([2, 3, 3, 4, 4, 5, 6, 6, 5, 4, 3, 3])

# Hypothetical average temperature data (in degrees Celsius)
average_temperature = np.array([3, 4, 7, 12, 17, 20, 22, 21, 18, 13, 8, 4])

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot line with error bars for each product category
ax1.errorbar(months, organic_cotton_sales, yerr=organic_cotton_error, label='Organic Cotton', fmt='-o', capsize=5, color='green', ecolor='lightgreen', alpha=0.8)
ax1.errorbar(months, recycled_polyester_sales, yerr=recycled_polyester_error, label='Recycled Polyester', fmt='-s', capsize=5, color='blue', ecolor='lightblue', alpha=0.8)
ax1.errorbar(months, bamboo_fabric_sales, yerr=bamboo_fabric_error, label='Bamboo Fabrics', fmt='-d', capsize=5, color='orange', ecolor='peachpuff', alpha=0.8)

# Add polynomial trend lines
p1 = Polynomial.fit(months, organic_cotton_sales, 3)
p2 = Polynomial.fit(months, recycled_polyester_sales, 3)
p3 = Polynomial.fit(months, bamboo_fabric_sales, 3)

ax1.plot(months, p1(months), '--', color='darkgreen', alpha=0.6)
ax1.plot(months, p2(months), '--', color='darkblue', alpha=0.6)
ax1.plot(months, p3(months), '--', color='darkorange', alpha=0.6)

# Bar chart for average temperature
ax2 = ax1.twinx()
ax2.bar(months, average_temperature, alpha=0.2, color='grey', width=0.4, align='center')
ax2.set_ylabel('Average Temperature (°C)', fontsize=12)
ax2.yaxis.label.set_color('grey')

# Customize the plot
ax1.set_title("Monthly Sales Performance with Seasonal Fluctuations\nand Weather Impact in the Eco-friendly Clothing Industry (2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Sales (in thousands)', fontsize=14)
ax1.set_xticks(months)
ax1.set_xticklabels(month_labels)
ax1.legend(title='Product Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, frameon=False)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()