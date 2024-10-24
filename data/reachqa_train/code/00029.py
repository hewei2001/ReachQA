import matplotlib.pyplot as plt
import numpy as np

# Extended years of observation
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

# Energy output data in TWh for each year
solar_output = np.array([220, 245, 260, 280, 310, 340])
wind_output = np.array([180, 210, 230, 270, 290, 320])
hydro_output = np.array([260, 255, 265, 270, 275, 280])

# Additional data: Cumulative energy output
cumulative_output = solar_output + wind_output + hydro_output

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot primary data: renewable energy sources
ax1.plot(years, solar_output, label='Solar Energy', color='gold', marker='o', linewidth=2, linestyle='-')
ax1.plot(years, wind_output, label='Wind Energy', color='skyblue', marker='^', linewidth=2, linestyle='--')
ax1.plot(years, hydro_output, label='Hydro Energy', color='blue', marker='s', linewidth=2, linestyle='-.')

# Add secondary axis for cumulative output
ax2 = ax1.twinx()
ax2.plot(years, cumulative_output, label='Cumulative Energy Output', color='green', marker='D', linewidth=2, linestyle=':', alpha=0.8)
ax2.fill_between(years, cumulative_output - 20, cumulative_output + 20, color='lightgreen', alpha=0.3)

# Set axis labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Output (TWh)', fontsize=12)
ax2.set_ylabel('Cumulative Output (TWh)', fontsize=12)
ax1.set_title('Renewable Energy Output by Source (2015-2020)\nIncluding Cumulative Output with Uncertainty', fontsize=14)

# Customize grid, legend, and ticks
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Annotate key data points
for year, solar, wind, hydro in zip(years, solar_output, wind_output, hydro_output):
    ax1.annotate(f'{solar}', (year, solar), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax1.annotate(f'{wind}', (year, wind), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8)
    ax1.annotate(f'{hydro}', (year, hydro), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=8)

# Automatically adjust the subplot layout for better fit
plt.tight_layout()

# Show the plot
plt.show()