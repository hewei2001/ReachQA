import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2025
years = np.arange(2010, 2026)

# Data for renewable energy production in MWh
solar_energy = [120, 150, 190, 240, 290, 350, 420, 500, 590, 690, 800, 920, 1050, 1190, 1350, 1520]
wind_energy = [90, 110, 130, 160, 190, 230, 270, 320, 370, 430, 500, 580, 670, 770, 880, 1000]
hydro_energy = [200, 210, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480]

# Calculate total energy and percentage contributions
total_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy)
solar_percentage = (np.array(solar_energy) / total_energy) * 100
wind_percentage = (np.array(wind_energy) / total_energy) * 100
hydro_percentage = (np.array(hydro_energy) / total_energy) * 100

# Create the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), sharex=True)

# Subplot 1: Energy Production Trends
ax1.plot(years, solar_energy, label='Solar Energy', marker='o', linestyle='-', linewidth=2.5, color='orange')
ax1.plot(years, wind_energy, label='Wind Energy', marker='s', linestyle='-', linewidth=2.5, color='blue')
ax1.plot(years, hydro_energy, label='Hydro Energy', marker='^', linestyle='-', linewidth=2.5, color='green')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Production (MWh)', fontsize=12)
ax1.set_title('Renewable Energy Production Trends\nin Green City (2010-2025)', fontsize=16, fontweight='bold')
ax1.set_xticks(years[::2])
ax1.set_yticks(np.arange(0, 1800, 200))
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.legend(loc='upper left', fontsize=11)

# Subplot 2: Percentage Contribution
ax2.stackplot(years, solar_percentage, wind_percentage, hydro_percentage, labels=['Solar', 'Wind', 'Hydro'], 
              colors=['orange', 'blue', 'green'], alpha=0.8)

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Contribution (%)', fontsize=12)
ax2.set_title('Percentage Contribution of Each Energy Source\nin Total Renewable Production', fontsize=16, fontweight='bold')
ax2.set_xticks(years[::2])
ax2.set_yticks(np.arange(0, 101, 10))
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.legend(loc='upper right', fontsize=11)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()