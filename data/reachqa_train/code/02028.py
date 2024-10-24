import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2040
years = np.arange(2010, 2041)

# Data: Energy output in Gigawatt-hours
solar_energy = [5, 10, 15, 25, 35, 50, 65, 85, 110, 140, 180, 225, 275, 330, 400, 480, 570, 670, 780, 900, 1030, 1175, 1330, 1500, 1685, 1885, 2100, 2330, 2575, 2835, 3110]
wind_energy = [15, 20, 28, 38, 55, 70, 90, 115, 145, 180, 220, 265, 315, 370, 430, 495, 565, 640, 720, 805, 895, 990, 1090, 1195, 1305, 1420, 1540, 1665, 1795, 1930, 2070]
hydropower = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250]
geothermal_energy = [2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81, 94, 108, 123, 139, 156, 174, 193, 213, 234, 256, 279, 303, 328, 354, 381, 409, 438, 468]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stackplot for energy output
ax.stackplot(years, solar_energy, wind_energy, hydropower, geothermal_energy,
             labels=['Solar', 'Wind', 'Hydropower', 'Geothermal'],
             colors=['#FDB813', '#34A853', '#4285F4', '#DB4437'], alpha=0.8)

# Title and labels
ax.set_title("Growth of Sustainable Energy Production\nin Gigawatt-hours (2010-2040)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Output (GWh)", fontsize=12)

# X-axis ticks for readability
ax.set_xticks(years[::2])
ax.tick_params(axis='x', rotation=45)

# Legend
ax.legend(loc='upper left', title="Energy Sources", fontsize=10, bbox_to_anchor=(1, 1))

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()