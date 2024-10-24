import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.array([2000, 2005, 2010, 2015, 2020])

# Define energy source contributions in TWh (artificially generated data)
coal = [3000, 2800, 2600, 2300, 1800]
natural_gas = [1000, 1300, 1600, 1900, 2100]
hydroelectric = [600, 650, 700, 750, 800]
solar_wind = [100, 300, 800, 1300, 2000]
nuclear = [900, 950, 1000, 1100, 1150]

# Stacked area data
data = np.array([coal, natural_gas, hydroelectric, solar_wind, nuclear])

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, data, labels=['Coal', 'Natural Gas', 'Hydroelectric', 'Solar & Wind', 'Nuclear'],
              colors=['#8B4513', '#D2691E', '#4682B4', '#FFD700', '#DA70D6'], alpha=0.85)

# Title and labels
plt.title("Rising Tides:\nEnergy Source Contributions to Global Electricity Generation (2000-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Electricity Generation (TWh)", fontsize=14)

# Adding a legend
plt.legend(loc='upper left', title="Energy Sources", fontsize=10)

# Grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()