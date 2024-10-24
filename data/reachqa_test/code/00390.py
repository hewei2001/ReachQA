import matplotlib.pyplot as plt
import numpy as np

# Create lists for years and sales data
years = np.arange(2010, 2021)

# Sales data for Battery Electric Vehicles (BEVs)
bev_sales = np.array([0.04, 0.13, 0.39, 0.69, 1.18, 1.53, 2.18, 3.18, 4.35, 6.18, 8.21])

# Sales data for Plug-in Hybrid Electric Vehicles (PHEVs)
phev_sales = np.array([0.27, 0.49, 0.69, 0.99, 1.43, 1.81, 2.43, 3.13, 3.93, 4.81, 5.79])

# Sales data for Hybrid Electric Vehicles (HEVs)
hev_sales = np.array([2.85, 2.95, 3.13, 2.91, 2.75, 2.61, 2.53, 2.41, 2.31, 2.19, 2.09])

# Calculate total sales for bar chart subplot
total_sales = bev_sales + phev_sales + hev_sales

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [2, 1]})

# Line chart subplot
ax = axs[0]
ax.plot(years, bev_sales, label='Battery Electric Vehicles (BEVs)', marker='o', linestyle='-', color='#4CAF50', linewidth=2)
ax.plot(years, phev_sales, label='Plug-in Hybrid Electric Vehicles (PHEVs)', marker='s', linestyle='--', color='#FF9800', linewidth=2)
ax.plot(years, hev_sales, label='Hybrid Electric Vehicles (HEVs)', marker='D', linestyle='-.', color='#2196F3', linewidth=2)
ax.set_xlabel('Year')
ax.set_ylabel('Sales (in millions)')
ax.set_title('Evolution of Electric Vehicle Sales in the United States:\nA Decade of Growth (2010-2020)')
ax.set_yticks(np.arange(0, 10, 1))
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Electric Vehicle Type')

# Bar chart subplot
ax = axs[1]
ax.bar(years, total_sales, color='#FFC107', alpha=0.8)
ax.set_xlabel('Year')
ax.set_ylabel('Total Sales (in millions)')
ax.set_title('Total Electric Vehicle Sales per Year')
ax.set_yticks(np.arange(0, 20, 2))
ax.grid(True, linestyle='--', alpha=0.5)
for i, value in enumerate(total_sales):
    ax.text(years[i], value + 0.5, f'{value:.2f}', ha='center', va='bottom')

# Layout adjustments
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()