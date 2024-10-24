import matplotlib.pyplot as plt
import numpy as np

# Data: Yearly cumulative reduction in carbon emissions (in metric tons) by region
years = np.array([2025, 2026, 2027, 2028, 2029, 2030])

# Artificial data for each region
urbania = np.array([50, 150, 300, 500, 750, 1000])
suburbiana = np.array([30, 90, 180, 300, 450, 600])
coastland = np.array([20, 60, 120, 200, 300, 420])
highland = np.array([10, 40, 90, 150, 230, 320])
plains = np.array([15, 55, 130, 220, 340, 470])

# Colors for the regions
colors = ['#6baed6', '#74c476', '#fd8d3c', '#9e9ac8', '#fdae6b']

# Create an area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, urbania, suburbiana, coastland, highland, plains, labels=['Urbania', 'Suburbiana', 'Coastland', 'Highland', 'Plains'], colors=colors, alpha=0.85)

# Adding a title with line break for clarity
plt.title('GreenFleet’s Journey: Cumulative Carbon Emissions\nReduction by Region (2025-2030)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Reduction in Emissions (Metric Tons)', fontsize=14)

# Adding a legend with a location setting to avoid overlap
plt.legend(loc='upper left', title="Regions", fontsize=11, frameon=False)

# Enhance the chart with grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better visibility
plt.xticks(years, rotation=45)

# Use tight layout to ensure elements are not overlapping
plt.tight_layout()

# Display the plot
plt.show()