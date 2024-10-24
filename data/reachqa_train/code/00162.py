import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define countries and data
countries = ["Finland", "Netherlands", "United States", "Brazil", "Italy", 
             "Germany", "Japan", "Australia", "India", "China"]

# Data
coffee_consumption = np.array([12, 9, 5, 6, 5, 8, 3, 4, 1, 2])  # kg per capita
productivity_index = np.array([85, 80, 75, 70, 77, 78, 72, 74, 68, 70])  # Fictional scores
economic_growth = np.array([2.5, 2.0, 1.8, 3.1, 1.5, 1.9, 1.2, 2.3, 7.1, 6.0])  # Fictional % growth

# Sort the coffee consumption and corresponding productivity index for interpolation
sorted_indices = np.argsort(coffee_consumption)
coffee_consumption_sorted = coffee_consumption[sorted_indices]
productivity_index_sorted = productivity_index[sorted_indices]

# Removing duplicates by averaging their corresponding productivity index values
unique_coffee_consumption, indices = np.unique(coffee_consumption_sorted, return_inverse=True)
mean_productivity_index = np.array([productivity_index_sorted[indices == i].mean() 
                                    for i in range(len(unique_coffee_consumption))])

# Smooth fitting line using cubic spline interpolation
x_smooth = np.linspace(unique_coffee_consumption.min(), unique_coffee_consumption.max(), 300)
spl = make_interp_spline(unique_coffee_consumption, mean_productivity_index, k=3)
productivity_smooth = spl(x_smooth)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# First subplot: Scatter and smooth line
ax1.scatter(coffee_consumption, productivity_index, color='brown', s=100, alpha=0.7, label='Data Points')
ax1.plot(x_smooth, productivity_smooth, color='blue', linestyle='-', linewidth=2, label='Smooth Fit')
ax1.set_title('Impact of Coffee Consumption on\nNational Productivity', fontsize=14, fontweight='bold')
ax1.set_xlabel('Average Coffee Consumption\n(kg per capita)', fontsize=12)
ax1.set_ylabel('Productivity Index', fontsize=12)
for i, country in enumerate(countries):
    ax1.annotate(country, (coffee_consumption[i], productivity_index[i]), fontsize=9,
                 textcoords="offset points", xytext=(-10,5), ha='right')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='lower right', fontsize=10)

# Second subplot: Bar chart of economic growth
ax2.bar(countries, economic_growth, color='green', alpha=0.7)
ax2.set_title('Economic Growth Rates by Country', fontsize=14, fontweight='bold')
ax2.set_xlabel('Country', fontsize=12)
ax2.set_ylabel('Economic Growth (%)', fontsize=12)
ax2.tick_params(axis='x', rotation=45)  # Rotate x labels for better readability

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()