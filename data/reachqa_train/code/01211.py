import matplotlib.pyplot as plt
import numpy as np

# Define the years for our study
years = np.arange(2010, 2021)

# Define energy production in TWh for each energy source across the years
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])

# Calculate cumulative total energy production
cumulative_energy = solar_energy + wind_energy + hydropower_energy

# Calculate year-on-year growth as a percentage
percentage_growth = np.zeros(len(years))
percentage_growth[1:] = 100 * (cumulative_energy[1:] - cumulative_energy[:-1]) / cumulative_energy[:-1]

# Create figure with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# First subplot: Stacked bar chart
axs[0].bar(years, solar_energy, label='Solar Energy', color='gold', edgecolor='black')
axs[0].bar(years, wind_energy, bottom=solar_energy, label='Wind Energy', color='lightblue', edgecolor='black')
axs[0].bar(years, hydropower_energy, bottom=solar_energy + wind_energy, label='Hydropower', color='seagreen', edgecolor='black')

axs[0].set_title('Adoption of Renewable Energy Sources\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Energy Production (TWh)', fontsize=14)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 250, 25))
axs[0].legend(loc='upper left', fontsize=12)
axs[0].text(2010.5, 200, 'Note: Significant growth post-2015', fontsize=12, style='italic',
            bbox={'facecolor': 'lightgray', 'alpha': 0.5, 'pad': 5})
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Line plot for percentage growth
axs[1].plot(years, percentage_growth, marker='o', color='darkorange', linewidth=2, label='Percentage Growth')
axs[1].set_title('Yearly Growth Rate of Renewable Energy\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Percentage Growth (%)', fontsize=14)
axs[1].set_xticks(years)
axs[1].axhline(0, color='grey', linewidth=1)
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()