import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2040
years = np.arange(2010, 2041)

# Data: Energy output in Gigawatt-hours
solar_energy = np.array([5, 10, 15, 25, 35, 50, 65, 85, 110, 140, 180, 225, 275, 330, 400, 480, 570, 670, 780, 900, 1030, 1175, 1330, 1500, 1685, 1885, 2100, 2330, 2575, 2835, 3110])
wind_energy = np.array([15, 20, 28, 38, 55, 70, 90, 115, 145, 180, 220, 265, 315, 370, 430, 495, 565, 640, 720, 805, 895, 990, 1090, 1195, 1305, 1420, 1540, 1665, 1795, 1930, 2070])
hydropower = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250])
geothermal_energy = np.array([2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256, 279, 303, 328, 354, 381, 409, 438, 468])

# Total energy output for percentage calculation
total_energy = solar_energy + wind_energy + hydropower + geothermal_energy

# Creating the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Stacked Area Chart for Energy Output
ax1.stackplot(years, solar_energy, wind_energy, hydropower, geothermal_energy,
              labels=['Solar', 'Wind', 'Hydropower', 'Geothermal'],
              colors=['#FDB813', '#34A853', '#4285F4', '#DB4437'], alpha=0.8)
ax1.set_title("Growth of Sustainable Energy Production\nin Gigawatt-hours (2010-2040)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Output (GWh)", fontsize=12)
ax1.set_xticks(years[::2])
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left', title="Energy Sources", fontsize=10, bbox_to_anchor=(1, 1))
ax1.grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Percentage Share of Each Energy Source
solar_percent = (solar_energy / total_energy) * 100
wind_percent = (wind_energy / total_energy) * 100
hydropower_percent = (hydropower / total_energy) * 100
geothermal_percent = (geothermal_energy / total_energy) * 100

ax2.stackplot(years, solar_percent, wind_percent, hydropower_percent, geothermal_percent,
              labels=['Solar %', 'Wind %', 'Hydropower %', 'Geothermal %'],
              colors=['#FDB813', '#34A853', '#4285F4', '#DB4437'], alpha=0.8)
ax2.set_title("Percentage Share of Energy Sources\nin Total Sustainable Energy Production (2010-2040)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Percentage Share (%)", fontsize=12)
ax2.set_xticks(years[::2])
ax2.tick_params(axis='x', rotation=45)
ax2.legend(loc='upper left', title="Energy Sources", fontsize=10, bbox_to_anchor=(1, 1))
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for readability and display the plots
plt.tight_layout()
plt.show()