import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2021)

# Average annual salinity data (PSU) for three locations
salinity_pacific = np.array([34.7, 34.6, 34.8, 34.7, 34.9, 34.8, 35.0, 34.9, 35.1, 35.0, 35.2])
salinity_atlantic = np.array([35.1, 35.0, 35.2, 35.1, 35.3, 35.2, 35.4, 35.3, 35.5, 35.4, 35.6])
salinity_indian = np.array([34.5, 34.4, 34.6, 34.5, 34.7, 34.6, 34.8, 34.7, 34.9, 34.8, 35.0])

# Standard deviation indicating variability in measurements
std_dev_pacific = np.array([0.1, 0.2, 0.15, 0.2, 0.1, 0.15, 0.2, 0.1, 0.15, 0.2, 0.1])
std_dev_atlantic = np.array([0.12, 0.18, 0.1, 0.22, 0.15, 0.1, 0.2, 0.18, 0.14, 0.19, 0.13])
std_dev_indian = np.array([0.15, 0.12, 0.2, 0.18, 0.14, 0.1, 0.22, 0.16, 0.19, 0.21, 0.11])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting Pacific Ocean data
ax.errorbar(years, salinity_pacific, yerr=std_dev_pacific, fmt='o-', color='blue',
            ecolor='lightblue', elinewidth=2, capsize=4, alpha=0.8, label='Pacific Ocean')

# Plotting Atlantic Ocean data
ax.errorbar(years, salinity_atlantic, yerr=std_dev_atlantic, fmt='s-', color='green',
            ecolor='lightgreen', elinewidth=2, capsize=4, alpha=0.8, label='Atlantic Ocean')

# Plotting Indian Ocean data
ax.errorbar(years, salinity_indian, yerr=std_dev_indian, fmt='^-', color='red',
            ecolor='lightcoral', elinewidth=2, capsize=4, alpha=0.8, label='Indian Ocean')

# Title and labels
ax.set_title("Decadal Trends in Ocean Salinity Levels\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Average Salinity (PSU)", fontsize=14)
ax.set_xticks(years)
ax.set_ylim(34, 36)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(title='Measurement Locations', fontsize=12)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()