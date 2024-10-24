import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2025
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])

# Electric vehicle sales in thousands
# Assuming steady growth in urban areas due to higher demand and infrastructure
urban_sales = np.array([40, 55, 70, 90, 120, 160])
# Assuming slower but steady growth in rural areas
rural_sales = np.array([15, 20, 30, 45, 65, 85])

# Create the line chart
plt.figure(figsize=(12, 8))

# Plot the urban sales line
plt.plot(years, urban_sales, marker='o', linestyle='-', linewidth=2, color='teal', label='Urban Areas')

# Annotate urban sales data points
for i, value in enumerate(urban_sales):
    plt.annotate(f'{value}k', (years[i], urban_sales[i]), textcoords="offset points", xytext=(-5, 10),
                 ha='center', fontsize=10, color='teal')

# Plot the rural sales line
plt.plot(years, rural_sales, marker='s', linestyle='--', linewidth=2, color='orange', label='Rural Areas')

# Annotate rural sales data points
for i, value in enumerate(rural_sales):
    plt.annotate(f'{value}k', (years[i], rural_sales[i]), textcoords="offset points", xytext=(-5, 10),
                 ha='center', fontsize=10, color='orange')

# Customize axes labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Electric Vehicle Sales (in thousands)', fontsize=12)
plt.title('Evolution of Electric Vehicle Sales\nin Urban vs. Rural Areas (2020-2025)', fontsize=16, fontweight='bold', pad=20)

# Add gridlines to the plot for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend to distinguish between urban and rural data
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust the layout for better text visibility
plt.tight_layout()

# Display the plot
plt.show()