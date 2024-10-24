import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy generation in TWh (terawatt-hours)
solar_energy = np.array([2, 4, 7, 10, 15, 21, 30, 42, 58, 78, 100])
wind_energy = np.array([10, 13, 17, 21, 26, 33, 40, 46, 52, 59, 65])
hydro_energy = np.array([25, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])

# Create the stacked area chart
plt.figure(figsize=(14, 8))

# Plot stacked areas
plt.stackplot(years, solar_energy, wind_energy, hydro_energy, 
              labels=['Solar Energy', 'Wind Energy', 'Hydro Energy'],
              colors=['#FFD700', '#87CEEB', '#4682B4'],
              alpha=0.85)

# Add titles and labels
plt.title('Renewable Energy Generation in EcoLand\nfrom 2010 to 2020', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Generation (TWh)', fontsize=14)

# Customize legend and grid
plt.legend(loc='upper left', fontsize=12, frameon=True, framealpha=0.9, edgecolor='gray')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()