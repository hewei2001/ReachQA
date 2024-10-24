import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Consumption data in GWh for each energy source
solar = np.array([5, 10, 20, 35, 50, 70, 90, 120, 150, 185, 210])
wind = np.array([8, 15, 25, 40, 60, 80, 110, 130, 160, 190, 220])
hydro = np.array([20, 22, 23, 25, 27, 30, 35, 40, 45, 50, 55])
biomass = np.array([10, 12, 15, 18, 22, 28, 35, 42, 50, 60, 70])

# Calculate total consumption per year and percentage shares
total_consumption = solar + wind + hydro + biomass
solar_share = (solar / total_consumption) * 100
wind_share = (wind / total_consumption) * 100
hydro_share = (hydro / total_consumption) * 100
biomass_share = (biomass / total_consumption) * 100

# Create figure and two subplots side by side
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Stacked area plot for energy consumption
axs[0].stackplot(years, solar, wind, hydro, biomass, 
                 labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
                 colors=['#FFD700', '#00BFFF', '#32CD32', '#8A2BE2'], alpha=0.85)
axs[0].set_title("Evolution of Renewable Energy Consumption\nin Rivertown (2010-2020)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Energy Consumption (GWh)", fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 401, 50))
axs[0].set_xlim(2010, 2020)
axs[0].set_ylim(0, 400)
axs[0].legend(loc='upper left', title="Energy Source", fontsize=10, bbox_to_anchor=(1.05, 1))

# Line plot for percentage share of energy sources
axs[1].plot(years, solar_share, marker='o', label='Solar', color='#FFD700')
axs[1].plot(years, wind_share, marker='s', label='Wind', color='#00BFFF')
axs[1].plot(years, hydro_share, marker='^', label='Hydro', color='#32CD32')
axs[1].plot(years, biomass_share, marker='D', label='Biomass', color='#8A2BE2')
axs[1].set_title("Percentage Share of Renewable Energy Sources\nin Rivertown (2010-2020)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Percentage Share (%)", fontsize=12)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[1].set_xticks(years)
axs[1].set_yticks(np.arange(0, 101, 10))
axs[1].set_xlim(2010, 2020)
axs[1].set_ylim(0, 100)
axs[1].legend(loc='upper right', fontsize=10)

# Automatically adjust subplot params to fit the figure area
plt.tight_layout()

# Display the plots
plt.show()