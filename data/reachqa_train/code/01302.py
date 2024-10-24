import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Years from 2012 to 2022
years = np.arange(2012, 2023)

# Artificial data for renewable energy production (in terawatt-hours)
solar_production = np.array([50, 75, 90, 110, 150, 190, 230, 290, 360, 430, 500])
wind_production = np.array([100, 120, 145, 175, 210, 255, 300, 350, 415, 485, 550])
hydro_production = np.array([400, 405, 410, 415, 420, 430, 440, 455, 470, 490, 505])

# Calculate growth rates
solar_growth = (solar_production / solar_production[0] - 1) * 100
wind_growth = (wind_production / wind_production[0] - 1) * 100
hydro_growth = (hydro_production / hydro_production[0] - 1) * 100

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 10))

# Plot each energy type with different styles
ax1.plot(years, solar_production, marker='o', linestyle='-', color='#F9A602', linewidth=2, label='Solar Energy')
ax1.plot(years, wind_production, marker='s', linestyle='--', color='#0B84A5', linewidth=2, label='Wind Energy')
ax1.plot(years, hydro_production, marker='^', linestyle='-.', color='#60BD68', linewidth=2, label='Hydro Energy')

# Add a secondary axis for growth rates
ax2 = ax1.twinx()
ax2.plot(years, solar_growth, linestyle=':', color='#F9844A', linewidth=1.5, label='Solar Growth Rate')
ax2.plot(years, wind_growth, linestyle=':', color='#4C72B0', linewidth=1.5, label='Wind Growth Rate')
ax2.plot(years, hydro_growth, linestyle=':', color='#55A868', linewidth=1.5, label='Hydro Growth Rate')

# Title and labels
ax1.set_title("Renewable Energy Production Trends (2012-2022)\nSolar, Wind, and Hydro Energy with Growth Rates", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Production (TWh)", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)

# Adding legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10, title="Energy Sources", title_fontsize='12')

# Customizing grid
ax1.grid(True, linestyle='--', linewidth=0.5)

# Annotate significant points with enhanced styling
ax1.annotate('Breakthrough in Solar Tech', xy=(2016, 150), xytext=(2014, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='goldenrod',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='goldenrod'))
ax1.annotate('Wind Energy Investments', xy=(2018, 300), xytext=(2016, 400),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='blue',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))
ax1.annotate('Steady Growth in Hydro', xy=(2020, 470), xytext=(2018, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='forestgreen',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='forestgreen'))

# Adjust x-ticks to display every year
ax1.set_xticks(years)

# Format y-axis of the secondary axis to show percentages
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}%'.format(y)))

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()