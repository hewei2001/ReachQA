import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2025
years = np.arange(2000, 2026)

# Data for the length of the rail network over time for each city (in kilometers)
network_length_city_a = np.array([50, 55, 63, 72, 80, 92, 105, 120, 138, 159, 181, 205, 230, 260, 292, 327, 365, 405, 448, 494, 543, 595, 650, 707, 767, 830])
network_length_city_b = np.array([30, 32, 35, 39, 43, 48, 54, 61, 69, 78, 88, 99, 111, 124, 138, 153, 169, 186, 204, 223, 243, 264, 286, 309, 333, 358])
network_length_city_c = np.array([10, 15, 20, 20, 25, 30, 40, 40, 55, 60, 60, 75, 90, 90, 105, 120, 135, 150, 150, 175, 190, 190, 210, 240, 240, 270])

# Synthetic population data for each city (in thousands)
population_city_a = np.array([800, 820, 840, 860, 880, 900, 930, 960, 1000, 1050, 1110, 1180, 1260, 1350, 1450, 1560, 1680, 1810, 1950, 2100, 2260, 2430, 2610, 2800, 3000, 3210])
population_city_b = np.array([600, 610, 620, 640, 660, 680, 700, 730, 760, 800, 850, 910, 980, 1060, 1150, 1250, 1360, 1480, 1610, 1750, 1900, 2060, 2230, 2410, 2600, 2800])
population_city_c = np.array([400, 410, 420, 430, 440, 450, 460, 470, 490, 510, 530, 550, 570, 590, 610, 630, 660, 690, 730, 770, 810, 860, 910, 970, 1040, 1120])

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each city's rail network growth
ax1.plot(years, network_length_city_a, label='City A Network', color='blue', linewidth=2.5, marker='o')
ax1.plot(years, network_length_city_b, label='City B Network', color='green', linewidth=2.5, marker='s')
ax1.plot(years, network_length_city_c, label='City C Network', color='red', linewidth=2.5, marker='^')

# Secondary y-axis for population data
ax2 = ax1.twinx()

# Plotting bar chart for population growth
ax2.bar(years - 0.2, population_city_a, width=0.2, color='lightblue', label='City A Population', alpha=0.6)
ax2.bar(years, population_city_b, width=0.2, color='lightgreen', label='City B Population', alpha=0.6)
ax2.bar(years + 0.2, population_city_c, width=0.2, color='lightcoral', label='City C Population', alpha=0.6)

# Primary axis customization
ax1.set_title('Urban Rail Network and Population Growth in Major Cities\n(2000-2025)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Network Length (km)', fontsize=14, color='black')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim([2000, 2025])
ax1.set_ylim([0, 900])
ax1.tick_params(axis='x', rotation=45)

# Secondary axis customization
ax2.set_ylabel('Population (in thousands)', fontsize=14, color='gray')
ax2.set_ylim([0, 3500])

# Legend setup
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.88), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()