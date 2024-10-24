import matplotlib.pyplot as plt
import numpy as np

# Extended years for the x-axis
years = np.arange(2000, 2026)

# Expanded energy production data for each renewable source (in petawatt-hours)
solar = np.array([0, 1, 2, 3, 5, 7, 10, 15, 20, 30, 45, 60, 80, 110, 150, 195, 250, 300, 350, 410, 480, 560, 650, 750, 870, 1000])
wind = np.array([5, 8, 13, 20, 30, 45, 60, 80, 100, 130, 160, 200, 250, 310, 380, 450, 530, 620, 720, 830, 950, 1080, 1220, 1370, 1530, 1700])
hydroelectric = np.array([290, 292, 295, 300, 305, 310, 320, 330, 340, 350, 365, 380, 395, 410, 425, 440, 455, 470, 485, 500, 515, 530, 545, 560, 575, 590])
biomass = np.array([40, 42, 45, 48, 50, 52, 55, 58, 62, 66, 70, 74, 79, 85, 90, 96, 102, 109, 116, 124, 132, 140, 149, 158, 168, 178])
geothermal = np.array([10, 11, 12, 13, 14, 15, 16, 18, 20, 23, 26, 29, 32, 35, 39, 43, 47, 52, 57, 63, 69, 75, 82, 89, 97, 105])
tidal = np.array([0, 0, 0, 0, 1, 1, 2, 3, 5, 7, 10, 13, 17, 22, 27, 33, 40, 47, 55, 64, 74, 85, 97, 110, 124, 139])

# Set up the figure with subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 12))

# Stacked area chart for renewable energy
ax[0].stackplot(years, solar, wind, hydroelectric, biomass, geothermal, tidal,
                labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal', 'Tidal'],
                colors=['#ffcc00', '#66b3ff', '#99ff99', '#cc99ff', '#ff6666', '#ff9999'], alpha=0.8)

ax[0].set_title("Comprehensive Evolution of Renewable Energy Sources\nFrom 2000 to 2025", fontsize=16)
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Energy Production (PWh)", fontsize=12)
ax[0].legend(loc='upper left', fontsize=10, title='Energy Sources', bbox_to_anchor=(1, 1))

# Line chart to show percentage growth relative to the year 2000
total_initial = solar[0] + wind[0] + hydroelectric[0] + biomass[0] + geothermal[0] + tidal[0]
total_energy = solar + wind + hydroelectric + biomass + geothermal + tidal
percent_growth = (total_energy - total_initial) / total_initial * 100

ax[1].plot(years, percent_growth, marker='o', linestyle='-', color='purple', label='Total Renewable Growth %')
ax[1].set_title("Percentage Growth of Total Renewable Energy Production\nRelative to Year 2000", fontsize=14)
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Percentage Growth (%)", fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)

# Automatic adjustment to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()