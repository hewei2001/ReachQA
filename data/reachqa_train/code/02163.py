import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Energy consumption data in quadrillion BTUs for each sector
transportation = np.array([28.3, 29.0, 29.5, 30.0, 30.5, 30.8, 31.2, 31.5, 31.8, 32.0, 32.5])
residential = np.array([21.5, 21.3, 21.1, 21.0, 20.8, 20.6, 20.4, 20.3, 20.2, 20.1, 20.0])
industrial = np.array([22.7, 22.9, 23.1, 23.3, 23.5, 23.6, 23.8, 24.0, 24.1, 24.3, 24.5])
commercial = np.array([18.2, 18.5, 18.9, 19.2, 19.5, 19.7, 20.0, 20.2, 20.4, 20.6, 20.8])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, transportation, residential, industrial, commercial, 
             labels=['Transportation', 'Residential', 'Industrial', 'Commercial'], 
             colors=['#FF9999', '#66B2FF', '#99FF99', '#FFD700'], 
             alpha=0.8)

# Title and labels
ax.set_title('Energy Consumption Trends Across Different Sectors\n2010-2020', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (Quadrillion BTUs)', fontsize=12)

# Customize x-axis ticks to prevent overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, title='Sectors')

# Add grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()