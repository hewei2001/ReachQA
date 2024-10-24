import numpy as np
import matplotlib.pyplot as plt

# Define decades and an expanded range of energy sources
decades = np.arange(1980, 2051, 5)
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Coal', 'Natural Gas', 'Nuclear']

# Hypothetical data for each energy source
solar = np.array([1, 2, 3, 5, 10, 15, 22, 28, 35, 40, 45, 50, 55, 60, 65])
wind = np.array([1, 2, 3, 4, 7, 12, 18, 25, 32, 38, 44, 48, 50, 52, 54])
hydroelectric = np.array([60, 58, 55, 53, 50, 48, 45, 42, 40, 38, 35, 33, 30, 28, 26])
geothermal = np.array([1, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
biomass = np.array([2, 3, 4, 6, 9, 11, 13, 16, 19, 22, 25, 28, 31, 34, 37])
tidal = np.array([0, 0, 0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11])
coal = np.array([30, 29, 28, 27, 25, 24, 22, 20, 18, 16, 15, 13, 10, 8, 6])
natural_gas = np.array([5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
nuclear = np.array([10, 10, 10, 10, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28])

# Combine the data for stacking, ensuring that the data sums up appropriately
data = np.vstack([solar, wind, hydroelectric, geothermal, biomass, tidal, coal, natural_gas, nuclear])

# Create a figure for the stacked area chart
fig, ax = plt.subplots(figsize=(14, 10))

# Plot the stacked area chart
ax.stackplot(decades, data, labels=energy_sources, alpha=0.8,
             colors=['#FFCC00', '#66CCFF', '#99FF99', '#FF6666', '#DDA0DD', '#8A2BE2', '#A9A9A9', '#4682B4', '#FFD700'])

# Title and labels
ax.set_title('Evolution of Energy Sources from 1980 to 2050\n(Renewable and Non-Renewable)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Production', fontsize=12)

# Set x-ticks to avoid overlap and rotate them
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45)

# Add grid and legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Energy Sources', fontsize=10)

# Add reference lines
ax.axhline(100, color='gray', linewidth=1.5, linestyle='--', alpha=0.6)

# Annotate key points in time
ax.annotate('Solar Surge Begins', xy=(2005, 15), xytext=(2000, 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Hydroelectric Decline', xy=(1995, 53), xytext=(1990, 75),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Ensure the layout is adjusted for better readability
plt.tight_layout()

# Show the plot
plt.show()