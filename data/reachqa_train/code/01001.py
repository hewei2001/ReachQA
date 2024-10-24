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

# Compute growth rates for each plant type
vegetable_growth_rate = np.diff(vegetable_area) / vegetable_area[:-1] * 100
flower_growth_rate = np.diff(flower_area) / flower_area[:-1] * 100
herb_growth_rate = np.diff(herb_area) / herb_area[:-1] * 100
fruit_growth_rate = np.diff(fruit_area) / fruit_area[:-1] * 100

growth_years = years[1:]

# Set up the subplot grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area plot on the left
colors = ['#76c7c0', '#ff9999', '#77b300', '#ffcc00']
ax1.stackplot(years, plant_areas, labels=['Vegetables', 'Flowers', 'Herbs', 'Fruits'], colors=colors, alpha=0.8)
ax1.set_title('Urban Garden Growth Patterns (2015-2023)\nArea Coverage by Plant Types', fontsize=14, fontweight='bold', color='darkgreen')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Garden Area Covered (Square Meters)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
ax1.annotate('Boom in Vegetable Planting', xy=(2019, 40), xytext=(2017, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Growth rate line plot on the right
ax2.plot(growth_years, vegetable_growth_rate, marker='o', linestyle='-', color='#76c7c0', label='Vegetables')
ax2.plot(growth_years, flower_growth_rate, marker='s', linestyle='-', color='#ff9999', label='Flowers')
ax2.plot(growth_years, herb_growth_rate, marker='^', linestyle='-', color='#77b300', label='Herbs')
ax2.plot(growth_years, fruit_growth_rate, marker='d', linestyle='-', color='#ffcc00', label='Fruits')
ax2.set_title('Annual Growth Rate of Plant Types (2016-2023)', fontsize=14, fontweight='bold', color='darkblue')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, frameon=False)
ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
ax2.set_xticks(growth_years)
ax2.set_xticklabels(growth_years, rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()