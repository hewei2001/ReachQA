import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.arange(2000, 2021)

# Artificial data for different energy sources (in gigawatts)
solar_energy = np.array([2, 3, 5, 7, 10, 15, 20, 30, 45, 60, 80, 105, 130, 160, 195, 230, 270, 315, 360, 400, 450])
wind_energy = solar_energy + np.array([1, 2, 3, 5, 8, 12, 18, 25, 35, 50, 70, 90, 120, 150, 180, 220, 260, 305, 350, 390, 440])
hydro_energy = wind_energy + np.array([15, 18, 20, 25, 30, 38, 45, 55, 70, 85, 100, 115, 130, 145, 165, 185, 205, 230, 250, 275, 300])
geothermal_energy = hydro_energy + np.array([5, 7, 10, 12, 15, 20, 28, 37, 48, 60, 75, 90, 110, 135, 160, 190, 220, 255, 290, 330, 375])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, solar_energy, label='Solar Energy', color='gold', alpha=0.8)
ax.fill_between(years, solar_energy, wind_energy, label='Wind Energy', color='skyblue', alpha=0.8)
ax.fill_between(years, wind_energy, hydro_energy, label='Hydro Energy', color='lightgreen', alpha=0.8)
ax.fill_between(years, hydro_energy, geothermal_energy, label='Geothermal Energy', color='coral', alpha=0.8)

# Title and labels
ax.set_title('Global Renewable Energy Production (2000-2020):\nTransition to Clean Energy', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (Gigawatts)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(years[::2])  # Show every second year
ax.set_xticklabels([str(year) for year in years[::2]], rotation=45, ha='right')

# Grid for readability
ax.grid(linestyle='--', alpha=0.5)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Cumulative Total Line Plot
ax.plot(years, geothermal_energy, label='Total Renewable Energy', color='black', linestyle='--', linewidth=2)

# Annotate the chart with a significant trend
ax.annotate('Significant increase\nin Solar Energy', xy=(2010, 150), xytext=(2012, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()