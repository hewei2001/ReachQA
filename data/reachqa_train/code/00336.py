import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2020)

# Fictional energy production data in TWh
solar_energy = np.array([5, 10, 18, 30, 50, 70, 85, 100, 115, 130])
wind_energy = np.array([20, 25, 30, 35, 40, 50, 60, 75, 85, 90])
hydro_energy = np.array([40, 42, 45, 47, 50, 52, 55, 58, 60, 62])
biomass_energy = np.array([10, 12, 15, 18, 20, 25, 28, 30, 32, 35])

# Stack the data for the area chart
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the area chart
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
             colors=['gold', 'skyblue', 'lightgreen', 'sienna'], alpha=0.8)

# Set titles and labels
ax.set_title("Renewable Energy Production Trends\nA Decade of Green Growth", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Customize the x-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a grid for better readability
ax.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax.minorticks_on()
ax.grid(visible=True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

# Add legend
ax.legend(loc='upper left', title='Energy Source')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()