import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define the food consumption data in million tons
# We will adjust the data slightly to ensure a clear narrative
vegetables = np.array([2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 22])
grains = np.array([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5])
proteins = np.array([3, 4, 5, 6, 7, 9, 10, 12, 14, 16, 19])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data using stackplot
ax.stackplot(years, vegetables, grains, proteins, 
             labels=['Vegetables', 'Grains', 'Proteins'],
             colors=['#98FB98', '#FFD700', '#FF6347'], alpha=0.8)

# Enhance the plot with a title, labels, and legend
ax.set_title('Dietary Shifts in Gastronomia: 2010-2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Food Consumption (Million Tons)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust x-axis ticks for clear reading
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()