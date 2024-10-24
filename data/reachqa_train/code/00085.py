import matplotlib.pyplot as plt
import numpy as np

# Define time range for daily data over a year
days = np.arange(1, 366)

# Energy consumption data in terawatt-hours (TWh) for each source
# Base pattern over the year (artificially generated for complexity)
solar_energy = 20 + 10 * np.sin(2 * np.pi * days / 365)  # Cyclical pattern
wind_energy = 15 + 7 * np.cos(4 * np.pi * days / 365)  # More frequent cycles
fusion_energy = 10 + 5 * np.sin(2 * np.pi * (days / 365 - 0.25))  # Offset sinusoid
hydropower_energy = 12 + 4 * np.cos(2 * np.pi * days / 365)  # Another pattern
geothermal_energy = 8 + np.sin(8 * np.pi * days / 365)  # Rapid fluctuations

# Create the figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Subplot 1: Stacked area plot
ax1.fill_between(days, solar_energy, color='gold', alpha=0.6, label='Solar Energy')
ax1.fill_between(days, solar_energy + wind_energy, solar_energy, color='skyblue', alpha=0.6, label='Wind Energy')
ax1.fill_between(days, solar_energy + wind_energy + fusion_energy, solar_energy + wind_energy, color='lightgreen', alpha=0.6, label='Fusion Energy')
ax1.fill_between(days, solar_energy + wind_energy + fusion_energy + hydropower_energy, solar_energy + wind_energy + fusion_energy, color='navy', alpha=0.6, label='Hydropower Energy')
ax1.fill_between(days, solar_energy + wind_energy + fusion_energy + hydropower_energy + geothermal_energy, solar_energy + wind_energy + fusion_energy + hydropower_energy, color='purple', alpha=0.6, label='Geothermal Energy')

ax1.set_title('Energy Dynamics in Lumina\nA Comprehensive Yearly Overview', fontsize=16, fontweight='bold')
ax1.set_ylabel('Energy Consumption (TWh)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, ncol=2)
ax1.grid(True, linestyle='--', alpha=0.5)

# Subplot 2: Derived metrics plot
total_energy = solar_energy + wind_energy + fusion_energy + hydropower_energy + geothermal_energy
rolling_avg_energy = np.convolve(total_energy, np.ones(30)/30, mode='same')

ax2.plot(days, total_energy, color='coral', label='Total Energy Consumption', linewidth=2)
ax2.plot(days, rolling_avg_energy, color='blue', linestyle='--', label='30-Day Rolling Average', linewidth=2)

ax2.set_title('Derived Metrics for Energy Consumption Analysis', fontsize=14, fontweight='bold')
ax2.set_xlabel('Day of Year', fontsize=12)
ax2.set_ylabel('Total Energy (TWh)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)

# Set day names for the x-ticks
ax2.set_xticks(np.linspace(1, 365, 12))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the plot
plt.show()