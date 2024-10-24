import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.array([1980, 1990, 2000, 2010, 2020])

# Define the adoption rates for each renewable energy type as percentages of total energy consumption
solar = np.array([2, 5, 12, 25, 40])
wind = np.array([1, 6, 15, 30, 35])
hydro = np.array([20, 22, 23, 24, 25])
geothermal = np.array([1, 3, 5, 6, 7])

# Stack the data for the area plot
adoption_rates = np.vstack([solar, wind, hydro, geothermal])

# Create the stacked area plot
plt.figure(figsize=(14, 8))
plt.stackplot(years, adoption_rates, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#f4a582', '#92c5de', '#0571b0', '#ca0020'])

# Title and labels
plt.title('Global Renewable Energy Adoption: 1980-2020\nThe Transition Towards Sustainable Power', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (% of Total Energy Consumption)', fontsize=12)

# Legend
plt.legend(loc='upper left', fontsize=10, title='Energy Type', title_fontsize=12, bbox_to_anchor=(1, 1), borderaxespad=0.)

# Enhance the grid and background
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years, fontsize=10)
plt.yticks(np.arange(0, 101, 10), fontsize=10)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()