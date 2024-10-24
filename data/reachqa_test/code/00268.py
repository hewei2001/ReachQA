import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2014, 2024)

# Energy production data (in terawatt-hours)
solar_energy = np.array([50, 55, 60, 68, 72, 78, 85, 90, 95, 100])
wind_energy = np.array([60, 65, 70, 80, 85, 92, 100, 108, 115, 122])
hydro_energy = np.array([120, 118, 125, 130, 128, 135, 140, 142, 148, 150])

# Cumulative energy production
cumulative_energy = solar_energy + wind_energy + hydro_energy

# Standard deviations (for error bars)
solar_std = np.array([3, 3.5, 2.8, 3, 2.5, 2.8, 3, 2.5, 2, 2.1])
wind_std = np.array([2.5, 3, 2, 3.5, 3, 3.2, 2.8, 3, 3.1, 2.5])
hydro_std = np.array([4, 4.2, 3.8, 4, 4.1, 3.5, 3.7, 4.2, 3.9, 3.6])

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot original energy production with error bars
ax1.errorbar(years, solar_energy, yerr=solar_std, label='Solar Energy', fmt='-o', 
             color='gold', capsize=5, alpha=0.7)
ax1.errorbar(years, wind_energy, yerr=wind_std, label='Wind Energy', fmt='-s', 
             color='deepskyblue', capsize=5, alpha=0.7)
ax1.errorbar(years, hydro_energy, yerr=hydro_std, label='Hydro Energy', fmt='-^', 
             color='green', capsize=5, alpha=0.7)

# Set labels, title, and legend for the primary y-axis
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (TWh)', fontsize=12)
ax1.set_title('Renewable Energy Production in Greenscape\n2014-2023', fontsize=16, fontweight='bold', pad=20)
ax1.legend(title='Energy Source', title_fontsize='13', fontsize='11', loc='upper left')
ax1.set_xlim(2013.5, 2023.5)
ax1.set_ylim(45, 160)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot cumulative energy production on the secondary y-axis
ax2.plot(years, cumulative_energy, label='Cumulative Energy', color='purple', linestyle='-', marker='x', alpha=0.8)
ax2.set_ylabel('Cumulative Energy (TWh)', fontsize=12, color='purple')
ax2.set_ylim(230, 370)
ax2.tick_params(axis='y', labelcolor='purple')

# Add legend for the secondary y-axis
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

# Show plot
plt.show()