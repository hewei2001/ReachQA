import matplotlib.pyplot as plt
import numpy as np

# Monthly data from 2012 to 2021
months = np.arange(2012, 2022, 1/12)

# Detailed hypothetical energy production data
solar = np.linspace(100, 600, len(months)) + np.sin(months * 2 * np.pi) * 30
wind = np.linspace(200, 810, len(months)) + np.cos(months * 2 * np.pi) * 50
hydro = np.linspace(1000, 1100, len(months))
geothermal = np.linspace(50, 97, len(months)) + np.sin(months * 1.5 * np.pi) * 10
biomass = np.linspace(75, 172, len(months)) + np.cos(months * np.pi) * 15

# Additional energy sources
nuclear = np.linspace(800, 850, len(months)) + np.sin(months * 1.2 * np.pi) * 20
natural_gas = np.linspace(500, 600, len(months)) + np.cos(months * 0.9 * np.pi) * 30

# Stacking the energy data
energy_sources = np.vstack([solar, wind, hydro, geothermal, biomass, nuclear, natural_gas])

# Colors and patterns for each energy source
colors = ['#FFD700', '#00BFFF', '#1E90FF', '#FF6347', '#32CD32', '#8A2BE2', '#FF8C00']

# Plotting
fig, ax = plt.subplots(figsize=(16, 10))

# Create a stacked area chart
ax.stackplot(months, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Nuclear', 'Natural Gas'], 
             colors=colors, alpha=0.8)

# Adding title and labels
ax.set_title('Monthly Trends in Global Renewable Energy Production and Fossil Fuels\n(2012-2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Adding legend
ax.legend(loc='upper left', title='Energy Source', fontsize=12)

# Customizing the x-ticks for better readability
ax.set_xticks(np.arange(2012, 2022, 1))
ax.set_xticklabels([str(year) for year in range(2012, 2022)], fontsize=12)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add an annotation for total energy production
total_energy = energy_sources.sum(axis=0)
max_year = months[np.argmax(total_energy)]
max_value = np.max(total_energy)
ax.annotate(f'Max Production: {int(max_value)} TWh', xy=(max_year, max_value), xytext=(max_year-2, max_value+500),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, backgroundcolor='white')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()