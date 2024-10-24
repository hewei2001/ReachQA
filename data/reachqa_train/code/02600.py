import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and sales data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])
retail_sales = np.array([250, 245, 230, 210, 185, 160, 140, 120, 100])

# Define market share percentage data
e_commerce_market_share = e_commerce_sales / (e_commerce_sales + retail_sales) * 100
retail_market_share = retail_sales / (e_commerce_sales + retail_sales) * 100

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: E-commerce vs Retail Sales
ax1.scatter(years, e_commerce_sales, color='blue', label='E-commerce Sales', marker='o', s=100, alpha=0.8)
ax1.scatter(years, retail_sales, color='red', label='Retail Sales', marker='x', s=100, alpha=0.8)

years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)
retail_spline = make_interp_spline(years, retail_sales)(years_fine)

ax1.plot(years_fine, e_commerce_spline, color='blue', linestyle='-', linewidth=2, alpha=0.6)
ax1.plot(years_fine, retail_spline, color='red', linestyle='-', linewidth=2, alpha=0.6)

ax1.set_title("Evolution of E-commerce vs. Retail Sales\nin the Tech Gadget Sector", fontsize=14, weight='bold')
ax1.set_xlabel("Years", fontsize=12)
ax1.set_ylabel("Sales (in million USD)", fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Market Share of E-commerce vs Retail
ax2.stackplot(years, e_commerce_market_share, retail_market_share, labels=['E-commerce', 'Retail'], colors=['lightblue', 'lightcoral'], alpha=0.7)
ax2.set_title("Market Share Evolution", fontsize=14, weight='bold')
ax2.set_xlabel("Years", fontsize=12)
ax2.set_ylabel("Market Share (%)", fontsize=12)
ax2.legend(loc='upper right')
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()