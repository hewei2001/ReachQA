import matplotlib.pyplot as plt
import numpy as np

# Define the years for the extended study
years = np.arange(2000, 2031)

# Generate synthetic data for multiple energy sources
# These functions are designed to simulate realistic, yet challenging, energy adoption trends
solar_energy = 10 + 5 * np.log1p(years - 1999) + 2 * np.sin((years - 2000) / 5)
wind_energy = 15 + 10 * np.sqrt(years - 1999) - 0.5 * (years - 2000)
hydro_energy = np.full(years.shape, 20)
geothermal_energy = 5 + 0.5 * (years - 2000) + 1 * np.sin((years - 2000) / 2)
biomass_energy = 5 + 2 * np.log1p(years - 1999)
tidal_energy = 2 + 0.3 * (years - 2000)

# Stack data for the area plot
energy_sources = np.row_stack((solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy, tidal_energy))

# Create the area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF6347', '#8B4513', '#1E90FF']

# Plot the stacked area chart
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Tidal'], colors=colors, alpha=0.8)

# Add a title and labels
ax.set_title('Trends in Renewable Energy Adoption (2000-2030)\nChallenging Growth Patterns and Projections', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage Contribution of Energy Sources (%)', fontsize=12)

# Customize ticks and grid
ax.set_xticks(np.arange(2000, 2031, 2))
ax.set_yticks(np.arange(0, 151, 10))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend outside the plot
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Highlight significant global events related to energy
highlight_years = {2015: "Paris Agreement", 2020: "Renewables Push", 2030: "Sustainability Goal"}
for year, event in highlight_years.items():
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=0.8)
    ax.text(year, 5, event, rotation=90, verticalalignment='bottom', horizontalalignment='right', color='grey', fontsize=9)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Adjust layout to accommodate legends and labels
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()