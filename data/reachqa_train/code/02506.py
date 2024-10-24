import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)
revenues = np.array([5, 7, 10, 12, 15, 18, 22, 25, 28, 30, 35])  # in million USD
employee_count = np.array([1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 15])  # in hundreds
product_launches = np.array([1, 2, 4, 6, 7, 7, 8, 10, 12, 15, 18])  # number of products

# Initialize figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot areas with overlays
ax1.fill_between(years, revenues, color='#ff9999', alpha=0.4)
ax1.plot(years, revenues, color='red', linestyle='-', marker='o', label='Revenues (Million USD)')

ax1.fill_between(years, employee_count, color='#66b3ff', alpha=0.4)
ax1.plot(years, employee_count, color='blue', linestyle='--', marker='^', label='Employee Count (Hundreds)')

ax2 = ax1.twinx()
ax2.fill_between(years, product_launches, color='#99ff99', alpha=0.4)
ax2.plot(years, product_launches, color='green', linestyle='-.', marker='s', label='Product Launches')

# Annotations
ax1.annotate('Start of rapid growth', xy=(2015, 15), xytext=(2016, 25),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax2.annotate('Peak Launch Year', xy=(2020, 18), xytext=(2019, 20),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Enhance grid
ax1.grid(linestyle='--', alpha=0.6)

# Customizing axes and labels
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenues & Employee Count', fontsize=12, color='red')
ax2.set_ylabel('Product Launches', fontsize=12, color='green')

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Legends
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Title with multi-line support for clarity
plt.title('Tech Startup Growth Over a Decade\n(2010-2020)', fontsize=16, fontweight='bold', loc='center')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()