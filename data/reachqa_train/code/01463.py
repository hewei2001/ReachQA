import numpy as np
import matplotlib.pyplot as plt

# Define the data
years = np.arange(2010, 2021)
germany_energy = [4500, 4700, 4800, 5000, 5100, 5200, 5300, 5500, 5700, 5900, 6100]
france_energy = [3200, 3400, 3500, 3550, 3650, 3700, 3800, 3850, 3900, 4000, 4150]
spain_energy = [2800, 2900, 3000, 3100, 3150, 3200, 3250, 3350, 3450, 3500, 3600]

germany_errors = [200, 180, 160, 150, 145, 140, 135, 130, 125, 120, 110]
france_errors = [150, 140, 130, 125, 120, 115, 110, 105, 100, 95, 90]
spain_errors = [180, 170, 160, 155, 150, 145, 140, 135, 130, 125, 120]

# Additional data for the stacked bar chart
germany_wind = [2000, 2100, 2200, 2350, 2400, 2500, 2600, 2700, 2800, 2900, 3000]
germany_solar = [500, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
germany_hydro = [1500, 1600, 1700, 1750, 1800, 1850, 1900, 2000, 2100, 2200, 2300]

france_wind = [1200, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1800]
france_solar = [600, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
france_hydro = [1400, 1500, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000]

spain_wind = [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]
spain_solar = [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
spain_hydro = [1200, 1300, 1350, 1400, 1450, 1500, 1550, 1650, 1750, 1800, 2000]

# Create the figure and axes
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot the first subplot (original plot with error bars)
ax1 = axs[0]
ax1.errorbar(years, germany_energy, yerr=germany_errors, fmt='-o', capsize=5, label='Germany',
             color='green', linestyle='-', linewidth=2, marker='o')
ax1.errorbar(years, france_energy, yerr=france_errors, fmt='-s', capsize=5, label='France',
             color='blue', linestyle='--', linewidth=2, marker='s')
ax1.errorbar(years, spain_energy, yerr=spain_errors, fmt='-^', capsize=5, label='Spain',
             color='orange', linestyle='-.', linewidth=2, marker='^')

ax1.set_title('Renewable Energy Utilization with Uncertainty (2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Energy Utilization (GWh)')
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10)

# Plot the second subplot (stacked bar chart)
ax2 = axs[1]
ax2.bar(years - 0.2, germany_wind, width=0.2, label='Germany Wind', color='lightgreen', edgecolor='black')
ax2.bar(years - 0.2, germany_solar, width=0.2, bottom=germany_wind, label='Germany Solar', color='yellow', edgecolor='black')
ax2.bar(years - 0.2, germany_hydro, width=0.2, bottom=np.array(germany_wind) + np.array(germany_solar), label='Germany Hydro', color='lightblue', edgecolor='black')

ax2.bar(years, france_wind, width=0.2, label='France Wind', color='mediumseagreen', edgecolor='black')
ax2.bar(years, france_solar, width=0.2, bottom=france_wind, label='France Solar', color='gold', edgecolor='black')
ax2.bar(years, france_hydro, width=0.2, bottom=np.array(france_wind) + np.array(france_solar), label='France Hydro', color='deepskyblue', edgecolor='black')

ax2.bar(years + 0.2, spain_wind, width=0.2, label='Spain Wind', color='darkseagreen', edgecolor='black')
ax2.bar(years + 0.2, spain_solar, width=0.2, bottom=spain_wind, label='Spain Solar', color='khaki', edgecolor='black')
ax2.bar(years + 0.2, spain_hydro, width=0.2, bottom=np.array(spain_wind) + np.array(spain_solar), label='Spain Hydro', color='cornflowerblue', edgecolor='black')

ax2.set_title('Breakdown of Renewable Energy Sources (2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Energy Utilization (GWh)')
ax2.set_xticks(years)
ax2.legend(loc='upper left', fontsize=9, bbox_to_anchor=(1, 1), ncol=1)
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()