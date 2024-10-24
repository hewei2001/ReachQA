import matplotlib.pyplot as plt
import numpy as np

# Define time span and create more data points for better curve representation
years = np.arange(1000, 3100, 100)

# Update the original data with more realistic trends and slight adjustments
solar_luminosity = np.array([99.5, 100, 100.8, 101.2, 102])
solar_luminosity = np.interp(years, np.arange(1000, 3100, 500), solar_luminosity)

earth_temperature = np.array([14.5, 15, 15.2, 15.5, 16])
earth_temperature = np.interp(years, np.arange(1000, 3100, 500), earth_temperature)

# Add more variation to CO2 levels
co2_levels = np.array([280, 285, 300, 325, 360])
co2_levels = np.interp(years, np.arange(1000, 3100, 500), co2_levels)

# Create the main plot with an additional subplot
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [3, 1]})

# Plot solar luminosity data on the main plot
color = 'tab:orange'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Solar Luminosity (% of current)', color=color, fontsize=12)
ax1.plot(years, solar_luminosity, color=color, marker='o', linestyle='-', linewidth=2, label='Solar Luminosity')
ax1.tick_params(axis='y', labelcolor=color)

# Annotate the solar luminosity data points with less frequent labels to reduce clutter
for i in range(0, len(years), 4):
    ax1.annotate(f'{solar_luminosity[i]:.1f}%', (years[i], solar_luminosity[i]), 
                 textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color=color)

# Create a second y-axis for Earth temperature
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Average Earth Temperature (°C)', color=color, fontsize=12)
ax2.plot(years, earth_temperature, color=color, marker='o', linestyle='--', linewidth=2, label='Earth Temperature')
ax2.tick_params(axis='y', labelcolor=color)

# Annotate the temperature data points with adjusted positions to prevent overlap
for i in range(0, len(years), 4):
    xytext = (-15, -20) if i % 8 == 0 else (10, 10)  # Alternating text placement for clarity
    ax2.annotate(f'{earth_temperature[i]:.1f}°C', (years[i], earth_temperature[i]), 
                 textcoords="offset points", xytext=xytext, ha='center', fontsize=9, color=color)

# Set the title with multiple lines
ax1.set_title('Evolution of Solar Luminosity and\nTemperature Over Millennia', fontsize=16, fontweight='bold')

# Add legends to the main plot
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1), frameon=False)
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1), frameon=False)

# Enhance layout with a grid on the main plot
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot CO2 levels in the additional subplot
ax3.set_title('CO2 Levels Over Millennia', fontsize=14, fontweight='bold')
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('CO2 Levels (ppm)', fontsize=12)
ax3.plot(years, co2_levels, color='tab:green', marker='s', linestyle='-', linewidth=2, label='CO2 Levels')
ax3.fill_between(years, co2_levels, color='tab:green', alpha=0.2)

# Adjust the y-axis limits and ticks for better clarity
ax3.set_ylim(270, 370)  # Expanded range for clarity
ax3.set_yticks(np.arange(280, 371, 20))  # More readable tick intervals
ax3.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the CO2 plot
ax3.legend(loc='upper left', frameon=False)

# Automatically adjust the layout with increased spacing
plt.tight_layout(pad=3)

# Show the plot
plt.show()