import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2024)

# Define the energy contributions in gigawatts (GW)
solar_energy = np.array([2, 3, 5, 7, 10, 15, 20, 28, 36, 45, 55, 66, 78, 91])
wind_energy = np.array([4, 6, 8, 10, 13, 16, 21, 25, 29, 35, 42, 50, 60, 72])
hydro_energy = np.array([5, 5, 6, 7, 9, 11, 14, 18, 22, 25, 28, 30, 31, 32])
bioenergy = np.array([1, 2, 3, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20, 24])

# Stack the energy sources
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

# Create the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Bioenergy'], 
              colors=['#FFD700', '#1E90FF', '#32CD32', '#A0522D'], alpha=0.8)

# Add titles and labels
plt.title("The Evolution of Renewable Energy Sources in\nGreenCity from 2010 to 2023", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Contribution (GW)", fontsize=12)

# Adding a legend to identify the energy sources
plt.legend(loc='upper left', title="Energy Source", fontsize=10, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Customize grid and layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(np.arange(0, 230, 20), fontsize=10)

# Automatically adjust the layout to fit elements within the figure
plt.tight_layout()

# Display the plot
plt.show()