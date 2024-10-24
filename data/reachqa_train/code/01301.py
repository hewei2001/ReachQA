import matplotlib.pyplot as plt
import numpy as np

# Years from 2012 to 2022
years = np.arange(2012, 2023)

# Artificial data for renewable energy production (in terawatt-hours)
solar_production = [50, 75, 90, 110, 150, 190, 230, 290, 360, 430, 500]
wind_production = [100, 120, 145, 175, 210, 255, 300, 350, 415, 485, 550]
hydro_production = [400, 405, 410, 415, 420, 430, 440, 455, 470, 490, 505]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each energy type with different styles
ax.plot(years, solar_production, marker='o', linestyle='-', color='#FFD700', linewidth=2, label='Solar Energy')
ax.plot(years, wind_production, marker='s', linestyle='--', color='#1E90FF', linewidth=2, label='Wind Energy')
ax.plot(years, hydro_production, marker='^', linestyle='-.', color='#32CD32', linewidth=2, label='Hydro Energy')

# Title and labels
ax.set_title("Renewable Energy Production Trends (2012-2022)\nSolar, Wind, and Hydro Energy", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Adding legend
ax.legend(title="Energy Sources", loc='upper left', fontsize=10, title_fontsize='12')

# Customizing grid
ax.grid(True, linestyle='--', linewidth=0.5)

# Annotate significant points
ax.annotate('Breakthrough in Solar Tech', xy=(2016, 150), xytext=(2014, 200),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='goldenrod')

ax.annotate('Wind Energy Investments', xy=(2018, 300), xytext=(2016, 350),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='blue')

ax.annotate('Steady Growth in Hydro', xy=(2020, 470), xytext=(2018, 490),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='forestgreen')

# Adjust x-ticks to display every year
ax.set_xticks(years)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()