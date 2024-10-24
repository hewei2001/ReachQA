import numpy as np
import matplotlib.pyplot as plt

# Decades for the timeline
decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Average temperature anomalies (°C) for each decade
temperature_anomalies = np.array([-0.1, -0.05, 0.03, 0.2, 0.4, 0.6, 0.8, 1.0])

# Error margins indicating variability or uncertainty in the temperature data
error_margins = np.array([0.05, 0.04, 0.03, 0.06, 0.08, 0.05, 0.07, 0.06])

# CO2 emissions (in billion metric tons) for each decade - hypothetical data
co2_emissions = np.array([5, 8, 12, 15, 20, 25, 30, 35])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot the temperature anomaly line chart with error bars
ax1.errorbar(
    decades, temperature_anomalies, yerr=error_margins, label='Avg Temperature Anomaly (°C)',
    color='red', marker='o', linestyle='-', linewidth=2, capsize=5, ecolor='black', alpha=0.8
)
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Temperature Anomaly (°C)', fontsize=12, color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.set_ylim(-0.2, 1.2)
ax1.set_yticks(np.arange(-0.2, 1.4, 0.2))
ax1.grid(True, linestyle='--', alpha=0.5)

# Add a second y-axis for CO2 emissions
ax2 = ax1.twinx()
ax2.fill_between(decades, co2_emissions, color='lightblue', alpha=0.4, label='CO2 Emissions (Billion Tons)')
ax2.set_ylabel('CO2 Emissions (Billion Tons)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax2.set_ylim(0, 40)

# Add titles and legends
plt.title('Climate Change Indicators: Temperature Anomalies and CO2 Emissions\nAcross Decades', fontsize=16, fontweight='bold', pad=20)
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

# Adjust layout for better visualization
plt.tight_layout()

# Show the combined chart
plt.show()