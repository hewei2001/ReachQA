import matplotlib.pyplot as plt
import numpy as np

# Original data
years = np.arange(2015, 2026)
solar_energy = np.array([20, 30, 45, 60, 80, 100, 130, 160, 200, 250, 300])
wind_energy = np.array([50, 60, 70, 85, 100, 120, 145, 175, 210, 250, 290])
hydropower_energy = np.array([150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200])

# Calculate total energy and percentage contributions
total_energy = solar_energy + wind_energy + hydropower_energy
solar_percent = (solar_energy / total_energy) * 100
wind_percent = (wind_energy / total_energy) * 100
hydropower_percent = (hydropower_energy / total_energy) * 100

# Prepare figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Stacked area chart
ax1.stackplot(years, solar_energy, wind_energy, hydropower_energy, 
              labels=['Solar', 'Wind', 'Hydropower'], 
              colors=['#FFD700', '#87CEEB', '#6B8E23'], alpha=0.8)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (GWh)', fontsize=12)
ax1.set_title('Renewable Energy Evolution:\nProduction from Solar, Wind, and Hydropower (2015-2025)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', title='Energy Source')
ax1.grid(True, linestyle='--', alpha=0.7)

# Annotate key events
ax1.annotate('Solar surpasses 150 GWh', xy=(2022, 160), xytext=(2019, 190),
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)

# Second subplot: Line plot for percentage contribution
ax2.plot(years, solar_percent, marker='o', linestyle='-', color='#FFD700', label='Solar %')
ax2.plot(years, wind_percent, marker='s', linestyle='-', color='#87CEEB', label='Wind %')
ax2.plot(years, hydropower_percent, marker='^', linestyle='-', color='#6B8E23', label='Hydropower %')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Contribution (%)', fontsize=12)
ax2.set_title('Contribution Breakdown:\nPercentage Share by Energy Source', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', title='Energy Source %')
ax2.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
for ax in [ax1, ax2]:
    ax.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the combined plot
plt.show()