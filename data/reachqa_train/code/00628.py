import matplotlib.pyplot as plt
import numpy as np

# Years for the plot
years = np.array([1990, 2000, 2010, 2020])

# Energy generated from different sources in GWh
solar_energy = np.array([5, 20, 50, 90])
wind_energy = np.array([10, 30, 70, 100])
hydropower_energy = np.array([15, 40, 60, 80])

# Calculate total energy for the overlay
total_energy = solar_energy + wind_energy + hydropower_energy

# Create the figure and a subplot with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(12, 8))
ax2 = ax1.twinx()

# Stackplot for energy data
stack = ax1.stackplot(years, solar_energy, wind_energy, hydropower_energy, labels=['Solar', 'Wind', 'Hydropower'], 
                      colors=['#FFD700', '#87CEEB', '#32CD32'], alpha=0.85, edgecolor='w')

# Line plot for total energy trend
ax2.plot(years, total_energy, color='darkred', linewidth=2.5, linestyle='--', marker='o', label='Total Energy')

# Adding annotations
for i, year in enumerate(years):
    ax1.text(year, solar_energy[i] / 2, f'{solar_energy[i]}', fontsize=8, ha='center', color='black', weight='bold')
    ax1.text(year, solar_energy[i] + wind_energy[i] / 2, f'{wind_energy[i]}', fontsize=8, ha='center', color='black', weight='bold')
    ax1.text(year, solar_energy[i] + wind_energy[i] + hydropower_energy[i] / 2, f'{hydropower_energy[i]}', fontsize=8, ha='center', color='black', weight='bold')

# Title and labels
ax1.set_title('GreenVille Renewable Energy Generation Over Time\nTransition to Sustainability', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Generated (GWh)', fontsize=14)
ax2.set_ylabel('Total Energy (GWh)', fontsize=14, color='darkred')

# Customize grid and legends
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Enhancing visual appearance
ax1.set_facecolor('#F7F7F9')
fig.patch.set_facecolor('#EDEDED')

# Use a tight layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()