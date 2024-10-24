import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy production data (in TWh)
solar_energy = np.array([10, 15, 20, 28, 35, 42, 55, 70, 90, 115, 140])
wind_energy = np.array([20, 22, 27, 34, 40, 50, 65, 85, 110, 130, 150])
hydro_energy = np.array([50, 55, 58, 60, 63, 65, 68, 70, 72, 75, 80])

# Cumulative renewable energy production for stacked plotting
cumulative_solar = solar_energy
cumulative_wind = solar_energy + wind_energy
cumulative_hydro = solar_energy + wind_energy + hydro_energy

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart using fill_between
ax.fill_between(years, 0, cumulative_solar, label='Solar', color='#FDB813', alpha=0.8)
ax.fill_between(years, cumulative_solar, cumulative_wind, label='Wind', color='#00A86B', alpha=0.8)
ax.fill_between(years, cumulative_wind, cumulative_hydro, label='Hydro', color='#1F78B4', alpha=0.8)

# Title and labels with multiple lines
ax.set_title("Decade of Green Power:\nRenewable Energy Production in Region X (2010-2020)", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Rotating x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid for better readability
ax.grid(linestyle='--', alpha=0.6)

# Legend to identify the energy sources
ax.legend(loc='upper left', fontsize=11, title='Energy Source', title_fontsize='13')

# Automatically adjust the layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()