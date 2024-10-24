import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2025
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])

# Electric vehicle sales in thousands
urban_sales = np.array([40, 55, 70, 90, 120, 160])
rural_sales = np.array([15, 20, 30, 45, 65, 85])

# Calculate year-over-year growth rates
urban_growth = np.diff(urban_sales) / urban_sales[:-1] * 100
rural_growth = np.diff(rural_sales) / rural_sales[:-1] * 100

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Line chart of sales
ax[0].plot(years, urban_sales, marker='o', linestyle='-', linewidth=2, color='teal', label='Urban Areas')
ax[0].plot(years, rural_sales, marker='s', linestyle='--', linewidth=2, color='orange', label='Rural Areas')

# Annotate sales data points
for i, value in enumerate(urban_sales):
    ax[0].annotate(f'{value}k', (years[i], urban_sales[i]), textcoords="offset points", xytext=(-5, 10),
                   ha='center', fontsize=10, color='teal')

for i, value in enumerate(rural_sales):
    ax[0].annotate(f'{value}k', (years[i], rural_sales[i]), textcoords="offset points", xytext=(-5, 10),
                   ha='center', fontsize=10, color='orange')

# Customize axes, title, and grid for subplot 1
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Electric Vehicle Sales (in thousands)', fontsize=12)
ax[0].set_title('Electric Vehicle Sales in Urban vs. Rural Areas\n(2020-2025)', fontsize=14, fontweight='bold')
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(loc='upper left', fontsize=12)

# Subplot 2: Bar chart of year-over-year growth rates
x_positions = np.arange(len(urban_growth))
bar_width = 0.35
ax[1].bar(x_positions, urban_growth, width=bar_width, color='teal', alpha=0.7, label='Urban Growth')
ax[1].bar(x_positions + bar_width, rural_growth, width=bar_width, color='orange', alpha=0.7, label='Rural Growth')

# Customize axes, title, and legend for subplot 2
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Growth Rate (%)', fontsize=12)
ax[1].set_title('Year-over-Year Growth Rates of EV Sales\n(2021-2025)', fontsize=14, fontweight='bold')
ax[1].set_xticks(x_positions + bar_width / 2)
ax[1].set_xticklabels(years[1:])
ax[1].legend(loc='upper left', fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout for better text visibility
plt.tight_layout()

# Display the plots
plt.show()