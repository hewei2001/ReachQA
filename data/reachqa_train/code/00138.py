import numpy as np
import matplotlib.pyplot as plt

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Data representing the percentage share of each energy source in total renewable energy supply
solar = np.array([5, 6, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70])
wind = np.array([15, 17, 19, 22, 24, 27, 29, 31, 33, 35, 36, 37, 38, 39, 40, 40, 40, 41, 42, 43, 43])
biomass = np.array([30, 29, 28, 26, 25, 23, 22, 21, 20, 18, 17, 16, 15, 14, 13, 12, 12, 12, 11, 10, 10])
hydropower = 100 - (solar + wind + biomass)  # Ensure the total adds up to 100%

# Plotting the Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, solar, wind, biomass, hydropower, 
             labels=['Solar', 'Wind', 'Biomass', 'Hydropower'], 
             colors=['#FFD700', '#87CEEB', '#32CD32', '#A9A9A9'], alpha=0.8)

# Customizing the plot
ax.set_title('Evolution of Renewable Energy Sources in Urban Areas\n(2000-2020)', fontsize=14, loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Renewable Energy Supply', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations for significant changes
ax.annotate('Rise of Solar Energy', xy=(2015, 35), xytext=(2005, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()