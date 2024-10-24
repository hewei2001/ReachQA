import matplotlib.pyplot as plt
import numpy as np

# Extended range of years from 2000 to 2025
years = np.arange(2000, 2026)

# Monthly granularity for more data points
months = np.array(range(1, 13))

# Energy production data (in TWh) expanded for additional sources
solar_energy = np.array([
    2, 3, 5, 7, 10, 15, 20, 28, 35, 42, 50, 60, 70, 85, 100, 120, 140, 165, 190, 220, 250, 280, 315, 355, 400, 450
])
wind_energy = np.array([
    5, 7, 10, 13, 18, 23, 30, 38, 48, 60, 75, 90, 110, 130, 155, 180, 210, 245, 280, 320, 365, 410, 460, 515, 575, 640
])
hydro_energy = np.array([
    30, 32, 35, 38, 42, 47, 50, 54, 58, 63, 68, 72, 78, 84, 90, 96, 102, 108, 115, 122, 129, 136, 144, 152, 160, 168
])
geothermal_energy = np.array([
    3, 4, 5, 6, 8, 10, 13, 16, 19, 23, 27, 31, 36, 41, 47, 53, 60, 67, 75, 84, 94, 105, 117, 130, 144, 159
])

# Cumulative renewable energy production for stacked plotting
cumulative_solar = solar_energy
cumulative_wind = cumulative_solar + wind_energy
cumulative_hydro = cumulative_wind + hydro_energy
cumulative_geothermal = cumulative_hydro + geothermal_energy

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the stacked area chart using fill_between
ax.fill_between(years, 0, cumulative_solar, label='Solar', color='#FDB813', alpha=0.8)
ax.fill_between(years, cumulative_solar, cumulative_wind, label='Wind', color='#00A86B', alpha=0.8)
ax.fill_between(years, cumulative_wind, cumulative_hydro, label='Hydro', color='#1F78B4', alpha=0.8)
ax.fill_between(years, cumulative_hydro, cumulative_geothermal, label='Geothermal', color='#E31A1C', alpha=0.8)

# Add advanced styling
ax.set_title("Expanding Horizons in Renewable Energy:\nA Journey from 2000 to 2025", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)
ax.set_xticks(years[::2])  # Only display every other year for better readability
ax.set_xticklabels(years[::2], rotation=45)

# Adding grid and legend
ax.grid(linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=11, title='Energy Source', title_fontsize='13')

# Automatically adjust the layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()