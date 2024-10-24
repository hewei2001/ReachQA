import matplotlib.pyplot as plt
import numpy as np

# Define the years and average global salinity levels (in PSU - Practical Salinity Units)
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
average_salinity = np.array([34.5, 34.7, 34.6, 34.8, 34.9, 35.0, 34.8, 34.7, 35.1, 35.2, 35.0])
variability = np.array([0.2, 0.15, 0.25, 0.2, 0.18, 0.1, 0.2, 0.22, 0.15, 0.13, 0.2])

# Define sea surface temperature anomalies (in degrees Celsius) for the same years
temperature_anomalies = np.array([0.5, 0.52, 0.48, 0.54, 0.55, 0.57, 0.58, 0.56, 0.60, 0.62, 0.61])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the salinity trends with error bars
ax1.errorbar(years, average_salinity, yerr=variability, fmt='-o', color='navy', ecolor='lightblue',
             elinewidth=2, capsize=5, alpha=0.8, label='Average Salinity Level (PSU)')

# Customize the first y-axis
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Salinity (PSU)', fontsize=14, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_title('Trends and Variability in Global Ocean Salinity and Temperature (2010-2020)', 
              fontsize=16, fontweight='bold', pad=20)

# Add grid lines
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Create a second y-axis for the temperature anomalies
ax2 = ax1.twinx()
ax2.bar(years, temperature_anomalies, color='orange', alpha=0.6, width=0.4, label='Temperature Anomalies (°C)', align='center')
ax2.set_ylabel('Temperature Anomalies (°C)', fontsize=14, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add annotations to highlight significant years
for year, sal, temp in zip(years, average_salinity, temperature_anomalies):
    if temp > 0.6 or sal > 35.1:
        ax1.annotate(f'Year: {year}', xy=(year, sal), xytext=(-20, 10),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='grey'), fontsize=10)

# Add legends for both datasets
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Adjust layout to prevent overlap
fig.tight_layout()

# Show the plot
plt.show()