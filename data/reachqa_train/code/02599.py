import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and sales data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])
retail_sales = np.array([250, 245, 230, 210, 185, 160, 140, 120, 100])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot scatter points for e-commerce and retail sales
ax.scatter(years, e_commerce_sales, color='blue', label='E-commerce Sales', marker='o', s=100, alpha=0.8)
ax.scatter(years, retail_sales, color='red', label='Retail Sales', marker='x', s=100, alpha=0.8)

# Generate smooth lines using spline interpolation
years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)
retail_spline = make_interp_spline(years, retail_sales)(years_fine)

# Plot the smooth fitting lines
ax.plot(years_fine, e_commerce_spline, color='blue', linestyle='-', linewidth=2, alpha=0.6)
ax.plot(years_fine, retail_spline, color='red', linestyle='-', linewidth=2, alpha=0.6)

# Set titles and labels
ax.set_title("Evolution of E-commerce vs. Retail Sales\nin the Tech Gadget Sector", fontsize=14, weight='bold')
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Sales (in million USD)", fontsize=12)

# Add a legend
ax.legend(loc='upper right')

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()