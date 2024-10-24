import matplotlib.pyplot as plt
import numpy as np

# Define the data for the original line chart with error bars
years = np.arange(2010, 2020)
avg_temperatures = np.array([15.2, 15.3, 15.4, 15.7, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8])
temperature_errors = np.array([0.2, 0.3, 0.25, 0.3, 0.2, 0.3, 0.15, 0.2, 0.25, 0.2])

# Define data for the new subplot
# Here, we are using CO2 emissions for the same period as a related but distinct dataset
co2_emissions = np.array([370, 375, 380, 385, 390, 395, 400, 405, 410, 415])  # Example data

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the line chart with error bars on the first subplot
ax1.errorbar(
    years, avg_temperatures, yerr=temperature_errors,
    fmt='-o', color='mediumseagreen', ecolor='lightcoral',
    elinewidth=2, capsize=5, capthick=2, alpha=0.8, label='Avg Temp ± Error'
)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
ax1.set_title('Annual Temperature Trends\nCoastal City (2010-2019)', fontsize=13, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2009, 2020)
ax1.set_ylim(14.5, 17.5)
ax1.legend(loc='upper left', fontsize=10)

# Plot a bar chart for CO2 emissions on the second subplot
ax2.bar(years, co2_emissions, color='steelblue', alpha=0.8, label='CO2 Emissions')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('CO2 Emissions (ppm)', fontsize=12, fontweight='bold')
ax2.set_title('Annual CO2 Emissions\n(2010-2019)', fontsize=13, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.7, axis='y')
ax2.set_xlim(2009, 2020)
ax2.set_ylim(365, 420)
ax2.legend(loc='upper left', fontsize=10)

# Adjust layout for clarity and readability
plt.tight_layout()

# Display the plot
plt.show()