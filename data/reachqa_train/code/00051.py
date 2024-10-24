import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)

# EcoMetropolis
solar_eco = [5, 7, 10, 14, 18, 23, 27, 32, 37, 42, 48]
wind_eco = [3, 6, 10, 13, 17, 22, 26, 30, 33, 37, 40]
hydro_eco = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]

# SolarVille
solar_solarville = [10, 15, 20, 28, 35, 42, 49, 56, 63, 70, 78]
wind_solarville = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
hydro_solarville = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# WindyCity
solar_windycity = [2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 16]
wind_windycity = [8, 12, 18, 23, 29, 35, 41, 46, 51, 57, 63]
hydro_windycity = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]

# Plotting the Area Chart
fig, ax = plt.subplots(3, 1, figsize=(12, 18), sharex=True, constrained_layout=True)

# Plot for EcoMetropolis
ax[0].stackplot(years, solar_eco, wind_eco, hydro_eco, labels=['Solar', 'Wind', 'Hydro'], colors=['#FFD700', '#87CEEB', '#00FA9A'], alpha=0.8)
ax[0].set_title('EcoMetropolis Energy Mix\n2010-2020', fontsize=14, weight='bold')
ax[0].set_ylabel('Energy Production (GW)', fontsize=12)
ax[0].legend(loc='upper left', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.5)

# Plot for SolarVille
ax[1].stackplot(years, solar_solarville, wind_solarville, hydro_solarville, labels=['Solar', 'Wind', 'Hydro'], colors=['#FFD700', '#87CEEB', '#00FA9A'], alpha=0.8)
ax[1].set_title('SolarVille Energy Mix\n2010-2020', fontsize=14, weight='bold')
ax[1].set_ylabel('Energy Production (GW)', fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.5)

# Plot for WindyCity
ax[2].stackplot(years, solar_windycity, wind_windycity, hydro_windycity, labels=['Solar', 'Wind', 'Hydro'], colors=['#FFD700', '#87CEEB', '#00FA9A'], alpha=0.8)
ax[2].set_title('WindyCity Energy Mix\n2010-2020', fontsize=14, weight='bold')
ax[2].set_xlabel('Year', fontsize=12)
ax[2].set_ylabel('Energy Production (GW)', fontsize=12)
ax[2].legend(loc='upper left', fontsize=10)
ax[2].grid(True, linestyle='--', alpha=0.5)

# Adjusting tick parameters
for axis in ax:
    axis.tick_params(axis='x', labelrotation=45)
    axis.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.suptitle('Renewable Energy Adoption in Futurist Cities: A Decade in Review', fontsize=16, weight='bold', y=1.02)
plt.show()