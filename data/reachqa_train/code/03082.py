import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy consumption data for each source
years = np.arange(1990, 2021, 10)
solar_energy = [20, 150, 400, 1000]  # Solar energy consumption in TWh
wind_energy = [50, 250, 600, 1200]   # Wind energy consumption in TWh
hydro_energy = [500, 550, 600, 650]  # Hydro energy consumption in TWh

# Data for growth rates
solar_growth = np.diff(solar_energy) / solar_energy[:-1] * 100
wind_growth = np.diff(wind_energy) / wind_energy[:-1] * 100
hydro_growth = np.diff(hydro_energy) / hydro_energy[:-1] * 100

# Setup the subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plot the area chart
axs[0].fill_between(years, solar_energy, color='#FFD700', alpha=0.7, label='Solar Energy')
axs[0].fill_between(years, np.add(solar_energy, wind_energy), solar_energy, color='#87CEFA', alpha=0.7, label='Wind Energy')
axs[0].fill_between(years, np.add(np.add(solar_energy, wind_energy), hydro_energy), np.add(solar_energy, wind_energy), 
                    color='#2E8B57', alpha=0.7, label='Hydro Energy')

axs[0].set_title('Evolution of Renewable Energy Sources\nUsage Over Decades (1990-2020)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Energy Consumption (TWh)', fontsize=12)
axs[0].set_xticks(np.arange(1990, 2021, 5))
axs[0].legend(loc='upper left', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].annotate('Rise in Solar Energy Technology', xy=(2000, 200), xytext=(2005, 800),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkorange')
axs[0].annotate('Policy Boost for Wind Energy', xy=(2010, 800), xytext=(2015, 1600),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='royalblue')
axs[0].tick_params(axis='x', rotation=45)

# Plot the line chart for growth rates
growth_years = np.arange(2000, 2021, 10)
axs[1].plot(growth_years, solar_growth, marker='o', linestyle='-', color='#FFD700', label='Solar Energy Growth Rate')
axs[1].plot(growth_years, wind_growth, marker='o', linestyle='-', color='#87CEFA', label='Wind Energy Growth Rate')
axs[1].plot(growth_years, hydro_growth, marker='o', linestyle='-', color='#2E8B57', label='Hydro Energy Growth Rate')

axs[1].set_title('Decadal Growth Rates of Renewable Energy Sources', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Rate (%)', fontsize=12)
axs[1].set_xticks(growth_years)
axs[1].legend(loc='upper right', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].tick_params(axis='x', rotation=45)

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plots
plt.show()