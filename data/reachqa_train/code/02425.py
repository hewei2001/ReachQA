import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from numpy.polynomial.polynomial import Polynomial

# Data setup
years = np.arange(2010, 2021)
average_sales = np.array([5, 5.8, 6.5, 7.0, 7.6, 8.3, 9.1, 10.2, 11.0, 12.5, 14.0])
sales_variability = np.array([0.3, 0.4, 0.35, 0.5, 0.45, 0.6, 0.5, 0.55, 0.6, 0.65, 0.7])

# Calculate sales growth rate for subplot
sales_growth_rate = np.diff(average_sales) / average_sales[:-1] * 100
growth_years = years[1:]

# Fit polynomial trend line
p = Polynomial.fit(years, average_sales, 2)
trend_line = p(years)

# Plot creation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
fig.subplots_adjust(hspace=0.4)

# Main plot: Sales trends with error bars and polynomial trend
ax1.errorbar(years, average_sales, yerr=sales_variability, fmt='o', markersize=6, 
             color='#D9534F', ecolor='#FFADAD', elinewidth=2, capsize=4, label='Avg Sales ± Variability')
ax1.plot(years, trend_line, linestyle='--', color='navy', label='Trend Line (Polynomial Fit)')
ax1.fill_between(years, average_sales - sales_variability, average_sales + sales_variability, 
                 color='#FFCCCC', alpha=0.3)

# Add annotations and highlights
ax1.annotate('Major Game Release',
             xy=(2018, 11.0), 
             xytext=(2015, 13.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, 
             ha='center',
             backgroundcolor='w')
ax1.axvspan(2013, 2016, color='gray', alpha=0.1, label='Notable Growth Phase')

# Title and labels
ax1.set_title("The Renaissance of Board Games:\nSales Trends and Variability (2010-2020)", 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (in millions)", fontsize=12)

# Grid, legend, and layout
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10)

# Subplot: Sales growth rate
ax2.bar(growth_years, sales_growth_rate, color='#5CB85C', width=0.6, label='Annual Growth Rate')
ax2.set_title("Annual Sales Growth Rate (%)", fontsize=14)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.legend(loc='upper left', fontsize=10)

# Show plot
plt.tight_layout()
plt.show()