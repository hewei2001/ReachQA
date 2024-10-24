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

# Total reductions across all regions for line plot
total_reduction = urbania + suburbiana + coastland + highland + plains

# Colors for the regions with gradients
colors = ['#6baed6', '#74c476', '#fd8d3c', '#9e9ac8', '#fdae6b']

# Create an area chart
plt.figure(figsize=(14, 9))
plt.stackplot(years, urbania, suburbiana, coastland, highland, plains, 
              labels=['Urbania', 'Suburbiana', 'Coastland', 'Highland', 'Plains'], 
              colors=colors, alpha=0.85)

# Add line plot for total reductions
plt.plot(years, total_reduction, color='black', linestyle='--', linewidth=2, label='Total Reduction')

# Adding annotations for key data points
for i, year in enumerate(years):
    plt.annotate(f'{total_reduction[i]}', 
                 (year, total_reduction[i]), 
                 textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=9, color='black', fontweight='bold')

# Adding a title with line breaks for clarity
plt.title('GreenFleet’s Journey: Cumulative Carbon Emissions\nReduction by Region (2025-2030)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Reduction in Emissions (Metric Tons)', fontsize=14)

# Adding a legend with a location setting to avoid overlap
plt.legend(loc='upper left', title="Regions", fontsize=11, frameon=False)

# Highlighting specific years with vertical lines
plt.axvline(x=2027, color='grey', linestyle=':', linewidth=1)
plt.text(2027, plt.ylim()[1]*0.9, 'Policy Update', rotation=90, color='grey', fontsize=10, ha='center')

# Enhance the chart with grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better visibility
plt.xticks(years, rotation=45)

# Use tight layout to ensure elements are not overlapping
plt.tight_layout()

# Display the plot
plt.show()