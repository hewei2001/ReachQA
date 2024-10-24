import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2022
years = np.arange(2012, 2023)

# Artificial data for renewable energy sources (in Terawatt-hours)
solar_power = np.array([10, 15, 22, 30, 38, 48, 60, 73, 88, 105, 123])
wind_power = np.array([20, 25, 30, 37, 45, 50, 58, 65, 75, 80, 88])
hydropower = np.array([50, 51, 52, 54, 55, 57, 58, 60, 61, 62, 64])

# Stack the data for the area plot
data = np.vstack([solar_power, wind_power, hydropower])

# Define colors for each energy type
colors = ['#FFD700', '#87CEEB', '#32CD32']

# Artificial data for capacity factors (percentage)
solar_cf = np.array([15, 16, 17, 19, 20, 23, 25, 28, 30, 33, 35])
wind_cf = np.array([30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
hydro_cf = np.array([40, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42])

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax1.stackplot(years, data, labels=['Solar Power', 'Wind Power', 'Hydropower'], colors=colors, alpha=0.8)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Output (TWh)", fontsize=12)
ax1.set_xlim(2012, 2022)
ax1.set_ylim(0, 250)
ax1.set_title("Renewable Energy Growth and Efficiency in Solaris\n(2012-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Energy Sources")

# Annotate significant growth in solar energy
ax1.annotate('Significant Growth\n in Solar Energy', xy=(2019, 130), xytext=(2015, 180),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold')

# Adding a line plot for capacity factors on a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, solar_cf, 'o--', color='orange', label='Solar Capacity Factor')
ax2.plot(years, wind_cf, 'o--', color='blue', label='Wind Capacity Factor')
ax2.plot(years, hydro_cf, 'o--', color='green', label='Hydropower Capacity Factor')
ax2.set_ylabel("Capacity Factor (%)", fontsize=12)
ax2.set_ylim(0, 100)

# Legend for capacity factors
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(0.95, 0.85), title="Capacity Factors")

# Use tight layout to prevent clipping of labels and adjust overlaps
plt.tight_layout()

# Display the plot
plt.show()