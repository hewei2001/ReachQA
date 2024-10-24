import numpy as np
import matplotlib.pyplot as plt

# Define the years and sectors
years = np.arange(2010, 2021)
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Renewable energy usage data in gigawatt-hours (GWh) for each sector over the years
residential_usage = np.array([10, 15, 23, 31, 40, 52, 66, 82, 100, 120, 145])
commercial_usage = np.array([8, 12, 18, 25, 34, 45, 59, 75, 95, 117, 142])
industrial_usage = np.array([20, 25, 33, 43, 56, 72, 91, 113, 138, 166, 198])
transportation_usage = np.array([5, 9, 15, 22, 32, 45, 60, 78, 99, 123, 150])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create the stacked area plot
ax.stackplot(years, residential_usage, commercial_usage, industrial_usage, transportation_usage,
             labels=sectors, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'], alpha=0.8)

# Customize the chart
ax.set_title("Greenovia's Renewable Revolution:\nA Decade of Sustainable Energy Adoption (2010-2020)",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, labelpad=10)
ax.set_ylabel("Renewable Energy Usage (GWh)", fontsize=12, labelpad=10)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Add a legend
ax.legend(loc='upper left', fontsize=10, title="Sectors", title_fontsize='12')

# Annotate a significant increase in the residential sector in 2020
ax.annotate('Residential Surge', xy=(2020, 545), xytext=(2018, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Add a grid to enhance readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and improve aesthetics
plt.tight_layout()

# Display the plot
plt.show()