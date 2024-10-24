import matplotlib.pyplot as plt
import numpy as np

# Years over a decade
years = np.arange(2010, 2020)

# Production in GWh for each energy source
solar_energy = [20, 25, 30, 40, 50, 55, 60, 70, 80, 85]  # Solar energy production
wind_energy = [30, 35, 40, 45, 55, 60, 65, 75, 85, 90]  # Wind energy production
hydro_energy = [50, 52, 54, 53, 55, 56, 58, 60, 62, 64] # Hydroelectric energy production

# Stack the data for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric'], colors=['#FDBF6F', '#1F78B4', '#33A02C'])

# Set title and labels
ax.set_title('Renewable Energy Production: Solar, Wind, and Hydroelectric\n2010-2019', fontsize=14, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend and position it outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source')

# Enhance plot aesthetics
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()