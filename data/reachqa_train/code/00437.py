import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2005 to 2035
years = np.arange(2005, 2036)

# Extended synthetic data for the percentage of total energy consumption from renewable sources
solar = np.array([2, 3, 5, 7, 10, 12, 15, 17, 20, 23, 25, 28, 30, 32, 35, 38, 40, 43, 45, 47, 50, 53, 55, 57, 60, 62, 65, 67, 70, 73, 75])
wind = np.array([1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 33, 35, 37, 38, 40, 42, 43, 45, 46])
hydro = np.array([8, 9, 10, 11, 11, 12, 13, 13, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 19, 20, 21, 21, 22, 23, 23, 23, 23, 24, 24, 25, 25])
biomass = np.array([1, 1.5, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 10.5, 11, 12, 12.5, 13, 13.5, 14, 15, 15, 16, 16.5, 17, 17, 18, 18.5, 19, 19.5, 20])
geothermal = np.array([0.5, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5])

# Stack the data vertically for the stackplot
data = np.vstack([solar, wind, hydro, biomass, geothermal])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'], 
             colors=['#ffd700', '#87ceeb', '#4682b4', '#8fbc8f', '#ff8c00'], alpha=0.8)

# Set title and labels
plt.title("Development and Distribution of Renewable Energy Sources\nin EcoCity: 2005-2035", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage of Total Energy Consumption (%)", fontsize=14)

# Add legend and customize its position
plt.legend(title='Renewable Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Add a line plot for the cumulative sum
cumulative_sum = np.sum(data, axis=0)
ax.plot(years, cumulative_sum, label='Cumulative Total', color='black', linestyle='--', linewidth=1.5)

# Adjust x-ticks to improve visibility and rotate x-labels if necessary
ax.set_xticks(np.arange(2005, 2036, 2))
plt.xticks(rotation=45)

# Automatically adjust layout for better visual representation
plt.tight_layout()

# Display the plot
plt.show()