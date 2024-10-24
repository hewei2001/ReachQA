import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy production data (in TWh) for each energy source
# The data is structured to reflect different growth patterns over a decade
solar_energy = [10, 15, 20, 30, 40, 55, 75, 95, 120, 150, 180]
wind_energy = [20, 30, 45, 60, 80, 110, 150, 200, 260, 320, 390]
hydro_energy = [50, 52, 55, 58, 60, 63, 66, 69, 72, 75, 78]
biomass_energy = [5, 7, 9, 12, 16, 22, 29, 37, 46, 55, 65]
geothermal_energy = [3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30]

# Stack data for plotting
energy_data = np.array([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, energy_data, labels=["Solar", "Wind", "Hydroelectric", "Biomass", "Geothermal"],
             colors=["#FFD700", "#00BFFF", "#32CD32", "#8B4513", "#FF4500"], alpha=0.8)

# Title and labels
ax.set_title("The Renewable Energy Transition:\nA Decade of Diverse Growth (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Energy Sources', fontsize=10, title_fontsize='12', frameon=True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid settings
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()