import numpy as np
import matplotlib.pyplot as plt

# Data for global average temperature changes
decades = np.array(['1950-59', '1960-69', '1970-79', '1980-89', '1990-99', '2000-09', '2010-19'])
average_temperatures = np.array([13.8, 13.9, 14.1, 14.4, 14.6, 14.9, 15.2])
temperature_variability = np.array([0.1, 0.12, 0.13, 0.15, 0.17, 0.18, 0.19])

# Related data for hypothetical CO2 concentrations over the same periods
co2_concentrations = np.array([300, 315, 330, 350, 370, 390, 415])

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharex=True)

# First subplot: Line chart with error bars for temperature
ax1.errorbar(
    decades, 
    average_temperatures, 
    yerr=temperature_variability, 
    fmt='-o', 
    color='red', 
    ecolor='gray', 
    elinewidth=2, 
    capsize=4, 
    capthick=2, 
    label='Avg Temp ± Variability'
)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Global Avg Temp (°C)', fontsize=12)
ax1.set_title('Global Average Temperature\nChanges (1950-2020)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)

# Second subplot: Bar chart for CO2 concentrations
ax2.bar(decades, co2_concentrations, color='skyblue', label='CO2 Concentrations (ppm)')
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('CO2 Concentration (ppm)', fontsize=12)
ax2.set_title('Atmospheric CO2 Concentrations\n(1950-2020)', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.7)

# Rotate x-axis labels to avoid overlapping
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()