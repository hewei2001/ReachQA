import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the years of interest
years = np.arange(2010, 2021)

# Artificial sales data for e-books and printed books (in millions)
ebook_sales = np.array([15, 18, 21, 25, 31, 34, 37, 39, 43, 46, 49])
printed_sales = np.array([82, 80, 76, 74, 71, 69, 66, 64, 61, 59, 56])

# Standard deviation representing uncertainties in sales data
ebook_uncertainty = np.array([1, 1.2, 1.5, 2, 2.5, 3, 2.8, 3.2, 3.5, 3.8, 4])
printed_uncertainty = np.array([3, 3.2, 3.8, 4, 4.2, 4.5, 4.8, 5, 5.5, 5.8, 6])

# Calculate growth rate
ebook_growth_rate = 100 * np.diff(ebook_sales) / ebook_sales[:-1]
printed_growth_rate = 100 * np.diff(printed_sales) / printed_sales[:-1]
growth_years = years[1:]

# Setup plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot e-book and printed book sales with error bars
ax1.errorbar(years, ebook_sales, yerr=ebook_uncertainty, fmt='o-', color='orange', 
             capsize=4, linewidth=2, alpha=0.7, label='E-Book Sales (Millions)')
ax1.errorbar(years, printed_sales, yerr=printed_uncertainty, fmt='s-', color='green', 
             capsize=4, linewidth=2, alpha=0.7, label='Printed Book Sales (Millions)')

# Titles and labels
ax1.set_title("E-Book vs. Printed Book Sales and Growth Rates\n2010-2020", fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales (Millions)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, frameon=False)

# Dual y-axis for growth rates
ax2 = ax1.twinx()
ax2.plot(growth_years, ebook_growth_rate, 'o--', color='purple', label='E-Book Growth Rate (%)')
ax2.plot(growth_years, printed_growth_rate, 's--', color='blue', label='Printed Book Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Linear regression to highlight trends
# Linear regression for e-book sales
X_years = years.reshape(-1, 1)
ebook_model = LinearRegression().fit(X_years, ebook_sales)
ebook_trend = ebook_model.predict(X_years)
ax1.plot(years, ebook_trend, linestyle='--', color='red', linewidth=1, alpha=0.8, label='E-Book Trend')

# Linear regression for printed sales
printed_model = LinearRegression().fit(X_years, printed_sales)
printed_trend = printed_model.predict(X_years)
ax1.plot(years, printed_trend, linestyle='--', color='brown', linewidth=1, alpha=0.8, label='Printed Trend')

# Adjust ticks, grid, and layout
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(10, 101, 10))
ax1.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show plot
plt.show()