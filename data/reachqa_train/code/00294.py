import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2024)
solar_energy_percentage = [
    0.5, 0.7, 1.0, 1.5, 2.3, 3.2, 4.5, 6.0, 8.0, 10.0, 
    12.5, 15.3, 18.0, 21.0, 25.0, 29.0, 34.0, 40.0, 46.0, 52.0, 
    59.0, 67.0, 74.0, 80.0
]
wind_energy_percentage = [
    1.0, 1.2, 1.6, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 
    10.0, 12.0, 14.5, 17.0, 20.0, 24.0, 29.0, 35.0, 41.0, 48.0, 
    56.0, 64.0, 72.0, 78.0
]

# Additional hypothetical data for biomass energy
biomass_energy_percentage = [
    0.5, 0.8, 1.2, 1.8, 2.1, 2.7, 3.3, 4.1, 5.0, 6.5, 
    7.8, 9.2, 11.0, 13.0, 15.5, 18.0, 21.0, 24.0, 28.0, 32.0, 
    36.0, 40.0, 45.0, 50.0
]

# Figure setup with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharex=True)

# First subplot: Line chart for Solar and Wind
axs[0].plot(years, solar_energy_percentage, label='Solar Energy', color='orange', marker='o', linestyle='-', linewidth=2)
axs[0].plot(years, wind_energy_percentage, label='Wind Energy', color='green', marker='s', linestyle='--', linewidth=2)
axs[0].set_title('The Rise of Solar and Wind Energy\nAdoption in Urban Areas (2000-2023)', fontsize=14, pad=15)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].legend(loc='upper left', fontsize=10)

# Annotations
axs[0].axvline(2010, color='grey', linestyle='--', alpha=0.5)
axs[0].text(2011, 20, 'Increased adoption post-2010', fontsize=9, color='black', rotation=90)
axs[0].axvline(2020, color='grey', linestyle='--', alpha=0.5)
axs[0].text(2021, 60, 'Rapid growth in 2020s', fontsize=9, color='black', rotation=90)

# Second subplot: Stacked bar chart for Solar, Wind, and Biomass
axs[1].bar(years, solar_energy_percentage, label='Solar', color='orange')
axs[1].bar(years, wind_energy_percentage, bottom=solar_energy_percentage, label='Wind', color='green')
combined_solar_wind = np.array(solar_energy_percentage) + np.array(wind_energy_percentage)
axs[1].bar(years, biomass_energy_percentage, bottom=combined_solar_wind, label='Biomass', color='brown')
axs[1].set_title('Cumulative Renewable Energy Adoption\nin Urban Areas (2000-2023)', fontsize=14, pad=15)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)

# Adjust layout for readability
plt.tight_layout()

# Show plot
plt.show()