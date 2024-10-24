import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2030 with half-year intervals for granularity
years = np.arange(2010, 2031.5, 0.5)

# Extended Energy production data (in TWh) for each energy source
solar_energy = [10, 15, 20, 30, 40, 55, 75, 95, 120, 150, 180, 215, 255, 300, 350, 410, 475, 550, 630, 720, 820, 935, 1060, 1195, 1350, 1525, 1710, 1910, 2130, 2370, 2630, 2915, 3230, 3570, 3940, 4340, 4770, 5240, 5740, 6280, 6860, 7480, 8150]
wind_energy = [20, 30, 45, 60, 80, 110, 150, 200, 260, 320, 390, 475, 570, 680, 800, 935, 1080, 1235, 1410, 1600, 1805, 2025, 2260, 2510, 2785, 3080, 3395, 3730, 4090, 4475, 4885, 5320, 5780, 6270, 6790, 7340, 7920, 8535, 9180, 9860, 10575, 11330, 12125]
hydro_energy = [50, 52, 55, 58, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174]
biomass_energy = [5, 7, 9, 12, 16, 22, 29, 37, 46, 55, 65, 77, 90, 104, 120, 137, 156, 176, 198, 222, 248, 276, 307, 340, 376, 414, 455, 499, 546, 596, 649, 705, 764, 826, 892, 961, 1034, 1110, 1190, 1273, 1360, 1451, 1546]
geothermal_energy = [3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 36, 42, 49, 57, 66, 76, 87, 99, 112, 127, 143, 160, 178, 198, 219, 241, 265, 290, 317, 345, 375, 406, 439, 474, 511, 550, 591, 634, 679, 726, 775, 826]
nuclear_energy = [100, 103, 105, 108, 111, 114, 117, 120, 123, 126, 130, 134, 138, 142, 146, 150, 155, 160, 165, 170, 176, 182, 188, 194, 201, 208, 215, 222, 230, 238, 246, 254, 263, 272, 281, 290, 300, 310, 320, 330, 341, 352, 364]

# Stack data for plotting
energy_data = np.array([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy, nuclear_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 9))

# Enhanced color palette
colors = ["#FFD700", "#00BFFF", "#32CD32", "#8B4513", "#FF4500", "#8A2BE2"]

ax.stackplot(years, energy_data, labels=["Solar", "Wind", "Hydroelectric", "Biomass", "Geothermal", "Nuclear"],
             colors=colors, alpha=0.8)

# Title and labels
ax.set_title("Renewable and Nuclear Energy Production (2010-2030)\nA Comprehensive Decade-Plus Study", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Adding a legend with more space and styling
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