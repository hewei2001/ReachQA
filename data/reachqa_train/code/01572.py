import matplotlib.pyplot as plt
import numpy as np

# Define the years for which data is available
years = np.arange(2010, 2020)

# Energy production data in GWh for each renewable source
solar = [5, 10, 20, 40, 70, 100, 150, 230, 310, 400]
wind = [50, 60, 75, 90, 115, 140, 175, 220, 265, 320]
hydroelectric = [200, 210, 215, 220, 225, 230, 235, 240, 245, 250]
biomass = [30, 32, 36, 40, 44, 49, 55, 60, 67, 75]

# Aggregate data for stack plotting
energy_data = np.vstack([solar, wind, hydroelectric, biomass])

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'],
             colors=['#FFD700', '#32CD32', '#4682B4', '#8B4513'], alpha=0.8)

# Add title and labels
ax.set_title('Renewable Energy Production by Source:\nA Decade of Growth and Transition', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)

# Customize the legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=12)

# Adding a grid and formatting the x-axis
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)  # Rotate x-axis labels for better visibility

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()