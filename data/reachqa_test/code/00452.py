import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Constructed data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
smartphone_sales = np.array([300, 450, 700, 850, 900, 1100, 1500, 1800])  # in thousands
laptop_sales = np.array([250, 300, 450, 600, 750, 800, 900, 950])       # in thousands
tablet_sales = np.array([100, 150, 200, 250, 300, 350, 380, 400])      # in thousands

# Market share data (in percentage)
smartphone_market_share = smartphone_sales / (smartphone_sales + laptop_sales + tablet_sales) * 100
laptop_market_share = laptop_sales / (smartphone_sales + laptop_sales + tablet_sales) * 100
tablet_market_share = tablet_sales / (smartphone_sales + laptop_sales + tablet_sales) * 100

# Create a new figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Left Plot: Sales Trends
axs[0].scatter(years, smartphone_sales, color='blue', label='Smartphones', s=100, alpha=0.7, edgecolor='k')
axs[0].scatter(years, laptop_sales, color='orange', label='Laptops', s=100, alpha=0.7, edgecolor='k')
axs[0].scatter(years, tablet_sales, color='green', label='Tablets', s=100, alpha=0.7, edgecolor='k')

# Smooth line fitting
years_smooth = np.linspace(years.min(), years.max(), 500)
axs[0].plot(years_smooth, make_interp_spline(years, smartphone_sales)(years_smooth), color='blue', linewidth=2, alpha=0.8, linestyle='-')
axs[0].plot(years_smooth, make_interp_spline(years, laptop_sales)(years_smooth), color='orange', linewidth=2, alpha=0.8, linestyle='-')
axs[0].plot(years_smooth, make_interp_spline(years, tablet_sales)(years_smooth), color='green', linewidth=2, alpha=0.8, linestyle='-')

# Customizing the left plot
axs[0].set_title("Consumer Electronics Sales Trends\n(2015 - 2022)", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Year", fontsize=14)
axs[0].set_ylabel("Sales Volume (in thousands)", fontsize=14)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 2001, 200))
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].legend(loc='upper left', fontsize=12)

# Right Plot: Market Share
axs[1].bar(years - 0.2, smartphone_market_share, width=0.2, color='blue', label='Smartphones')
axs[1].bar(years, laptop_market_share, width=0.2, color='orange', label='Laptops')
axs[1].bar(years + 0.2, tablet_market_share, width=0.2, color='green', label='Tablets')

# Customizing the right plot
axs[1].set_title("Market Share of Consumer Electronics\n(2015 - 2022)", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Year", fontsize=14)
axs[1].set_ylabel("Market Share (%)", fontsize=14)
axs[1].set_xticks(years)
axs[1].set_ylim(0, 100)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)
axs[1].legend(loc='upper left', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()