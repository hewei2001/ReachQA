import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define the food consumption data in million tons
vegetables = np.array([2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 22])
grains = np.array([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5])
proteins = np.array([3, 4, 5, 6, 7, 9, 10, 12, 14, 16, 19])

# Define additional data for population growth (in millions)
population_growth = np.array([100, 102, 104, 106, 108, 110, 113, 115, 118, 121, 124])

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Stack plot for food consumption
ax1.stackplot(years, vegetables, grains, proteins, 
              labels=['Vegetables', 'Grains', 'Proteins'],
              colors=['#98FB98', '#FFD700', '#FF6347'], alpha=0.8)

# Set titles and labels
ax1.set_title('Dietary Shifts in Gastronomia: 2010-2020\nWith Population Growth Overlay', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Food Consumption (Million Tons)', fontsize=12)

# Adding grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Customize x-axis ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Secondary axis for population growth
ax2 = ax1.twinx()
ax2.plot(years, population_growth, color='b', linestyle='-', marker='o', label='Population Growth (Million)')
ax2.set_ylabel('Population (Million)', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

# Combine legends for both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Annotation for key years
ax1.annotate('Significant Shift', xy=(2015, 20), xytext=(2016, 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()