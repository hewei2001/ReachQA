import matplotlib.pyplot as plt
import numpy as np

# Define years for the urban garden observation
years = np.arange(2015, 2024)

# Define the garden area (in square meters) covered by different plant types over the years
vegetable_area = np.array([10, 15, 25, 35, 50, 60, 70, 80, 100])
flower_area = np.array([5, 8, 12, 20, 30, 40, 45, 50, 55])
herb_area = np.array([2, 4, 8, 12, 18, 22, 25, 28, 30])
fruit_area = np.array([1, 2, 4, 8, 10, 15, 20, 25, 30])

# Stack the area data
plant_areas = np.vstack([vegetable_area, flower_area, herb_area, fruit_area])

# Set up the plot
plt.figure(figsize=(12, 8))

# Define colors for each plant type
colors = ['#76c7c0', '#ff9999', '#77b300', '#ffcc00']

# Create the stacked area plot
plt.stackplot(years, plant_areas, labels=['Vegetables', 'Flowers', 'Herbs', 'Fruits'], colors=colors, alpha=0.8)

# Set titles and labels
plt.title('Urban Garden Growth Patterns (2015-2023)\nArea Coverage by Plant Types', fontsize=16, fontweight='bold', color='darkgreen')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Garden Area Covered (Square Meters)', fontsize=12)

# Add legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid for better readability
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# Annotate a notable year
plt.annotate('Boom in Vegetable Planting', xy=(2019, 40), xytext=(2017, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()