import matplotlib.pyplot as plt
import numpy as np

# Define the years and cities
years = np.arange(2040, 2051)
cities = ['Techville', 'Ecotown', 'Sustainopolis']

# Renewable energy data for each city over the years
techville_solar = [2, 5, 9, 15, 22, 30, 39, 49, 60, 72, 85]
techville_wind = [1, 3, 7, 12, 18, 25, 33, 42, 52, 63, 75]
techville_hydro = [0.5, 1.5, 4, 8, 13, 19, 26, 34, 43, 53, 64]

ecotown_solar = [3, 7, 13, 20, 28, 37, 47, 58, 70, 83, 97]
ecotown_wind = [1.5, 4, 9, 15, 22, 30, 39, 49, 60, 72, 85]
ecotown_hydro = [0.8, 2.2, 5, 9, 14, 20, 27, 35, 44, 54, 65]

sustainopolis_solar = [4, 9, 16, 24, 33, 43, 54, 66, 79, 93, 108]
sustainopolis_wind = [2, 5, 11, 18, 26, 35, 45, 56, 68, 81, 95]
sustainopolis_hydro = [1, 2.5, 6, 11, 17, 24, 32, 41, 51, 62, 74]

# Stack the data for each city
techville_data = np.vstack([techville_solar, techville_wind, techville_hydro])
ecotown_data = np.vstack([ecotown_solar, ecotown_wind, ecotown_hydro])
sustainopolis_data = np.vstack([sustainopolis_solar, sustainopolis_wind, sustainopolis_hydro])

# Create the figure and axes
fig, axs = plt.subplots(3, 1, figsize=(12, 15), sharex=True, sharey=True)

# Define colors for energy sources
colors = ['#FFD700', '#87CEEB', '#228B22']

# Plot each city's data
for ax, city_data, city_name in zip(axs, [techville_data, ecotown_data, sustainopolis_data], cities):
    ax.stackplot(years, city_data, labels=['Solar', 'Wind', 'Hydro'], colors=colors, alpha=0.8)
    ax.set_title(f'Energy Adoption in {city_name} (2040-2050)', fontsize=14)
    ax.set_ylabel('Energy Output (TWh)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc='upper left', fontsize=10)

# Set common x-label
axs[-1].set_xlabel('Year', fontsize=12)

# Enhance layout
plt.suptitle('Evolution of Renewable Energy Adoption\nin Futuristic Cities', fontsize=16, fontweight='bold', y=0.95)
plt.xticks(years, rotation=45)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show plot
plt.show()