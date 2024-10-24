import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.arange(2010, 2021)

# Artificial sales data for e-books and printed books (in millions)
ebook_sales = np.array([15, 18, 21, 25, 31, 34, 37, 39, 43, 46, 49])
printed_sales = np.array([82, 80, 76, 74, 71, 69, 66, 64, 61, 59, 56])

# Standard deviation representing uncertainties in sales data
ebook_uncertainty = np.array([1, 1.2, 1.5, 2, 2.5, 3, 2.8, 3.2, 3.5, 3.8, 4])
printed_uncertainty = np.array([3, 3.2, 3.8, 4, 4.2, 4.5, 4.8, 5, 5.5, 5.8, 6])

# Set up the plot
plt.figure(figsize=(12, 6))

# Plot e-book sales with error bars
plt.errorbar(years, ebook_sales, yerr=ebook_uncertainty, label='E-Book Sales', 
             fmt='o-', color='orange', capsize=4, linewidth=2, alpha=0.7)

# Plot printed book sales with error bars
plt.errorbar(years, printed_sales, yerr=printed_uncertainty, label='Printed Book Sales', 
             fmt='s-', color='green', capsize=4, linewidth=2, alpha=0.7)

# Add labels and title
plt.title("E-Book vs. Printed Book Sales:\nA Decade of Evolution with Uncertainty (2010-2020)", fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (Millions)', fontsize=12)

# Add a legend
plt.legend(loc='upper right', title='Sales Type', fontsize=10, frameon=False)

# Customize ticks and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 91, 10))
plt.grid(True, linestyle='--', alpha=0.5)

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()