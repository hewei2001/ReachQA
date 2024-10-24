import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the original data
years = np.array([2025, 2026, 2027, 2028, 2029])
continents = ['North America', 'Europe', 'Asia']
na_sales = np.array([150, 180, 220, 260, 300])  # North America sales in thousands
eu_sales = np.array([170, 200, 240, 280, 320])  # Europe sales in thousands
as_sales = np.array([200, 250, 300, 360, 420])  # Asia sales in thousands

# Prepare cumulative data for stacking in 3D plot
na_cumulative = na_sales
eu_cumulative = eu_sales + na_cumulative
as_cumulative = as_sales + eu_cumulative

# Calculate growth rates for the second plot
na_growth_rate = np.diff(na_sales, prepend=na_sales[0]) / np.append(na_sales[0], na_sales[:-1]) * 100
eu_growth_rate = np.diff(eu_sales, prepend=eu_sales[0]) / np.append(eu_sales[0], eu_sales[:-1]) * 100
as_growth_rate = np.diff(as_sales, prepend=as_sales[0]) / np.append(as_sales[0], as_sales[:-1]) * 100

# Create a subplot layout
fig = plt.figure(figsize=(16, 8))

# 3D stacked bar chart
ax1 = fig.add_subplot(121, projection='3d')
_x = np.arange(len(years))
_y = np.arange(len(continents))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
dx = dy = 0.4

ax1.bar3d(x, y, np.zeros_like(x), dx, dy, na_sales.repeat(len(continents)), color='deepskyblue', alpha=0.9, label='North America')
ax1.bar3d(x, y, na_cumulative.repeat(len(continents)), dx, dy, eu_sales.repeat(len(continents)), color='limegreen', alpha=0.9, label='Europe')
ax1.bar3d(x, y, eu_cumulative.repeat(len(continents)), dx, dy, as_sales.repeat(len(continents)), color='gold', alpha=0.9, label='Asia')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Continent', fontsize=12)
ax1.set_zlabel('EV Sales (Thousands)', fontsize=12)
ax1.set_title("3D Stacked Bar Chart:\nEV Sales by Continent (2025-2029)", fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(_x)
ax1.set_xticklabels(years)
ax1.set_yticks(_y)
ax1.set_yticklabels(continents)
ax1.view_init(elev=30, azim=120)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='Continent', loc='upper left', fontsize=9)

# 2D line plot of growth rates
ax2 = fig.add_subplot(122)
ax2.plot(years, na_growth_rate, marker='o', color='deepskyblue', label='North America Growth Rate')
ax2.plot(years, eu_growth_rate, marker='o', color='limegreen', label='Europe Growth Rate')
ax2.plot(years, as_growth_rate, marker='o', color='gold', label='Asia Growth Rate')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_title("Annual Growth Rate of EV Sales\nby Continent (2025-2029)", fontsize=14, fontweight='bold', pad=20)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title='Continent', loc='upper left', fontsize=9)

# Adjust layout
plt.tight_layout()
plt.show()