import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define countries and data
countries = ["Finland", "Netherlands", "United States", "Brazil", "Italy", 
             "Germany", "Japan", "Australia", "India", "China"]

# Average coffee consumption per capita (in kilograms)
coffee_consumption = np.array([12, 9, 5, 6, 5, 8, 3, 4, 1, 2])

# Productivity index (fictional scores)
productivity_index = np.array([85, 80, 75, 70, 77, 78, 72, 74, 68, 70])

# Sort the data by coffee consumption
sorted_indices = np.argsort(coffee_consumption)
coffee_consumption_sorted = coffee_consumption[sorted_indices]
productivity_index_sorted = productivity_index[sorted_indices]

# Remove duplicates by averaging productivity index for duplicate coffee consumption values
unique_coffee_consumption = np.unique(coffee_consumption_sorted)
average_productivity_index = []

for value in unique_coffee_consumption:
    indices = np.where(coffee_consumption_sorted == value)[0]
    avg_index = np.mean(productivity_index_sorted[indices])
    average_productivity_index.append(avg_index)

average_productivity_index = np.array(average_productivity_index)

# Smooth fitting line using cubic spline interpolation
x_smooth = np.linspace(unique_coffee_consumption.min(), unique_coffee_consumption.max(), 300)
spl = make_interp_spline(unique_coffee_consumption, average_productivity_index, k=3)
productivity_smooth = spl(x_smooth)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot
ax.scatter(coffee_consumption, productivity_index, color='brown', s=100, alpha=0.7, label='Data Points')

# Smooth fitting line
ax.plot(x_smooth, productivity_smooth, color='blue', linestyle='-', linewidth=2, label='Smooth Fit')

# Title and labels
ax.set_title('Impact of Coffee Consumption on National Productivity', fontsize=16, fontweight='bold')
ax.set_xlabel('Average Coffee Consumption (kg per capita)', fontsize=12)
ax.set_ylabel('Productivity Index', fontsize=12)

# Annotate countries
for i, country in enumerate(countries):
    ax.annotate(country, (coffee_consumption[i], productivity_index[i]), fontsize=9, 
                textcoords="offset points", xytext=(-10,5), ha='right')

# Customize grid, legend, and layout
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='lower right', fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()