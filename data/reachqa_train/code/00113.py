import matplotlib.pyplot as plt
import numpy as np

# Define years and data for different energy sources (in terawatt-hours)
years = np.arange(2010, 2021)
solar_energy = np.array([15, 22, 30, 50, 80, 110, 150, 200, 260, 330, 400])
wind_energy = np.array([60, 75, 95, 120, 150, 180, 220, 270, 340, 420, 510])
hydro_energy = np.array([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])
biomass_energy = np.array([40, 42, 45, 47, 50, 52, 55, 57, 60, 62, 65])

# Stack the energy data
energy_sources = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Set up the plot
plt.figure(figsize=(12, 8))

# Define colors
colors = ['#ffcc00', '#1f77b4', '#2ca02c', '#ff7f0e']

# Create the stacked area plot
plt.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Set titles and labels with line breaks for better readability
plt.title('Renewable Energy Usage (2010-2020)\nSolar, Wind, Hydro, and Biomass Contributions', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Produced (TWh)', fontsize=12)

# Add legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Grid and formatting
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# Annotate significant change
plt.annotate('Significant Solar Growth', xy=(2018, 250), xytext=(2015, 450),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()