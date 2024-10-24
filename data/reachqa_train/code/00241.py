import matplotlib.pyplot as plt
import numpy as np

# Extended Data (2010-2030)
years = np.arange(2010, 2031)
solar = np.array([2, 3, 5, 7, 10, 14, 18, 22, 27, 32, 37, 43, 49, 55, 62, 70, 78, 87, 96, 105, 115])
wind = np.array([3, 5, 7, 10, 14, 19, 24, 30, 37, 45, 54, 63, 73, 84, 96, 108, 121, 135, 150, 165, 181])
hydro = np.array([15, 14, 14, 13, 13, 12, 12, 11, 10, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6])
biomass = np.array([4, 5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 26, 29])
geothermal = np.array([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20])

# Stacking the data for the area plot
data = np.vstack([solar, wind, hydro, biomass, geothermal])

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#32CD32', '#8B4513', '#FF6347']

# Plotting
fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'], colors=colors, alpha=0.8)

# Customizing the plot
ax.set_title("Evolution of Renewable Energy Usage in EcoLand\n(2010-2030)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Total Energy Consumption (%)", fontsize=12)
ax.set_xlim(2010, 2030)
ax.set_ylim(0, 300)  # Increased to account for the new energy source contributions

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', alpha=0.6)

# Rotating the x-axis labels for clarity
plt.xticks(years, rotation=45)

# Adding a legend
ax.legend(loc='upper left', fontsize=10)

# Use tight layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()