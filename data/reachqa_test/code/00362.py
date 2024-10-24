import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

solar_energy = [100, 120, 150, 180, 220, 250, 300, 350, 400, 450, 500]
wind_energy = [50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200]
hydro_energy = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
geothermal_energy = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

total_energy = [sum(energies) for energies in zip(solar_energy, wind_energy, hydro_energy, geothermal_energy)]

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Plot lines
ax1.plot(years, solar_energy, label='Solar Energy', marker='o', linestyle='-', linewidth=2, color='orange')
ax1.plot(years, wind_energy, label='Wind Energy', marker='s', linestyle='--', linewidth=2, color='green')
ax1.plot(years, hydro_energy, label='Hydro Energy', marker='D', linestyle='-.', linewidth=2, color='blue')
ax1.plot(years, geothermal_energy, label='Geothermal Energy', marker='*', linestyle=':', linewidth=2, color='red')

ax1.set_title("Renewable Energy Production: A Decade of Growth (2010-2020)\n(Gigawatt-hours)")
ax1.set_ylabel('Energy Production (GWh)')

# Plot bar chart
ax2.bar(years, total_energy, color='skyblue')
ax2.set_ylabel('Total Energy Production (GWh)')

# Set shared x-axis label
ax1.set_xlabel('Year')

# Add grid and legend
ax1.grid(True)
ax2.grid(True)
ax1.legend(loc='upper left')

# Adjust layout and show plot
plt.tight_layout()
plt.show()