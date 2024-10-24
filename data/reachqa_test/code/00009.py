import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2020)

# Define the energy production in terawatt hours (TWh) for each year
solar = np.array([5, 10, 20, 40, 60, 80, 120, 160, 210, 260])
wind = np.array([30, 35, 40, 55, 70, 90, 110, 130, 160, 200])
hydro = np.array([90, 92, 91, 93, 94, 95, 96, 97, 98, 99])
biomass = np.array([15, 18, 22, 24, 27, 30, 35, 40, 45, 50])

# Stack data for the original plot
energy_sources = np.vstack([solar, wind, hydro, biomass])

# Calculate year-over-year growth rate
def calculate_growth_rate(data):
    return np.diff(data) / data[:-1] * 100

solar_growth = calculate_growth_rate(solar)
wind_growth = calculate_growth_rate(wind)
hydro_growth = calculate_growth_rate(hydro)
biomass_growth = calculate_growth_rate(biomass)

# Create a 1x2 grid of subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Stack plot of energy production
colors = ['#FFDD44', '#6699FF', '#99BB55', '#FF8866']
axes[0].stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)
axes[0].set_title('Renewable Energy Generation\nContribution Over a Decade (2010-2019)', fontsize=14)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Generation (TWh)', fontsize=12)
axes[0].legend(loc='upper left', bbox_to_anchor=(1.05, 1), frameon=False)
axes[0].annotate('Solar surpasses Wind in 2017', xy=(2017, 290), xytext=(2012, 350),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
axes[0].grid(True, linestyle='--', linewidth=0.5)
axes[0].set_xticks(years)
axes[0].set_yticks(np.arange(0, 401, 50))

# Second subplot: Line plot of growth rates
growth_years = years[1:]  # Exclude the first year since growth is calculated between years
axes[1].plot(growth_years, solar_growth, label='Solar', color=colors[0], marker='o', linestyle='-')
axes[1].plot(growth_years, wind_growth, label='Wind', color=colors[1], marker='o', linestyle='-')
axes[1].plot(growth_years, hydro_growth, label='Hydro', color=colors[2], marker='o', linestyle='-')
axes[1].plot(growth_years, biomass_growth, label='Biomass', color=colors[3], marker='o', linestyle='-')
axes[1].set_title('Annual Growth Rate of Energy Production\n(Percentage Change)', fontsize=14)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].legend(loc='upper left', frameon=False)
axes[1].grid(True, linestyle='--', linewidth=0.5)
axes[1].set_xticks(years)
axes[1].set_yticks(np.arange(-10, 101, 10))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()