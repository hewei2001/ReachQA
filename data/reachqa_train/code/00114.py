import matplotlib.pyplot as plt
import numpy as np

# Define years and data for different energy sources (in terawatt-hours)
years = np.arange(2010, 2021)
solar_energy = np.array([15, 22, 30, 50, 80, 110, 150, 200, 260, 330, 400])
wind_energy = np.array([60, 75, 95, 120, 150, 180, 220, 270, 340, 420, 510])
hydro_energy = np.array([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])
biomass_energy = np.array([40, 42, 45, 47, 50, 52, 55, 57, 60, 62, 65])

# Additional dataset for non-renewable energy
non_renewable_energy = np.array([800, 790, 780, 770, 760, 750, 740, 730, 720, 710, 700])

# Stack the energy data
energy_sources = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Set up the plot
plt.figure(figsize=(14, 8))

# Define colors
colors = ['#ffcc00', '#1f77b4', '#2ca02c', '#ff7f0e']
line_color = '#d62728'

# Create the stacked area plot
plt.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Overlay line plot for non-renewable energy
plt.plot(years, non_renewable_energy, label='Non-Renewable', color=line_color, linewidth=2.5, linestyle='--')

# Set titles and labels with line breaks for better readability
plt.title('Renewable vs. Non-Renewable Energy Usage (2010-2020)\nComparison of Different Energy Sources', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Produced (TWh)', fontsize=12)

# Add legend and adjust its location to avoid overlap
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Grid and formatting
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# Annotate significant change
plt.annotate('Significant Solar Growth', xy=(2018, 250), xytext=(2015, 550),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred')

# Annotate non-renewable trend
plt.annotate('Steady Decline in Non-Renewables', xy=(2018, 720), xytext=(2013, 800),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkblue')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()