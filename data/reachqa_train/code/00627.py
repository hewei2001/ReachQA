import matplotlib.pyplot as plt
import numpy as np

# Years for the plot
years = np.array([1990, 2000, 2010, 2020])

# Energy generated from different sources in GWh
solar_energy = np.array([5, 20, 50, 90])
wind_energy = np.array([10, 30, 70, 100])
hydropower_energy = np.array([15, 40, 60, 80])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the energy data
ax.stackplot(years, solar_energy, wind_energy, hydropower_energy, labels=['Solar', 'Wind', 'Hydropower'], colors=['#FFD700', '#87CEEB', '#32CD32'], alpha=0.7)

# Adding annotations
for i, year in enumerate(years):
    ax.text(year, solar_energy[i], f'{solar_energy[i]}', fontsize=9, ha='center', va='bottom', color='black', weight='bold')
    ax.text(year, wind_energy[i] + solar_energy[i], f'{wind_energy[i]}', fontsize=9, ha='center', va='bottom', color='black', weight='bold')
    ax.text(year, wind_energy[i] + solar_energy[i] + hydropower_energy[i], f'{hydropower_energy[i]}', fontsize=9, ha='center', va='bottom', color='black', weight='bold')

# Title and labels
ax.set_title('GreenVille Renewable Energy Generation Over Time\nTransition to Sustainability', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Generated (GWh)', fontsize=14)

# Legend
ax.legend(loc='upper left', fontsize=12)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-axis labels to improve readability
plt.xticks(years)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()