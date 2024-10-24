import numpy as np
import matplotlib.pyplot as plt

# Define years of exoplanet discoveries
years = np.arange(1990, 2024, 5)

# Estimated atmospheric temperatures in Kelvin
temperatures = np.array([800, 780, 760, 740, 720, 690, 670])

# Uncertainties associated with temperature measurements
uncertainties = np.array([100, 90, 75, 60, 40, 25, 15])

# Fabricate data for the number of exoplanets discovered
discoveries = np.array([2, 5, 10, 25, 40, 55, 80])

# Create plot with shared x-axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot line chart with error bars for temperatures
ax1.errorbar(years, temperatures, yerr=uncertainties, fmt='-o', 
             color='navy', ecolor='skyblue', elinewidth=2, capsize=5,
             markerfacecolor='white', markeredgecolor='navy', markersize=8,
             label='Estimated Temperature (K)')

# Plot bar chart for exoplanet discoveries
ax2 = ax1.twinx()
ax2.bar(years, discoveries, color='lightcoral', alpha=0.6, width=3, label='Number of Discoveries')

# Annotate data points with temperature values
for year, temp, err in zip(years, temperatures, uncertainties):
    ax1.annotate(f'{temp}K ± {err}K', (year, temp), 
                 textcoords="offset points", xytext=(0, 10), 
                 ha='center', fontsize=9, color='darkblue')

# Annotate data points with discovery counts
for year, count in zip(years, discoveries):
    ax2.annotate(f'{count}', (year, count), 
                 textcoords="offset points", xytext=(0, 5), 
                 ha='center', fontsize=9, color='darkred')

# Add titles and labels
ax1.set_title('Exploration of Distant Exoplanets:\nAtmospheric Temperature Estimates and Discovery Trends (1990-2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year of Discovery', fontsize=13)
ax1.set_ylabel('Temperature (Kelvin)', fontsize=13, color='navy')
ax2.set_ylabel('Number of Exoplanet Discoveries', fontsize=13, color='darkred')

# Highlight a significant technological breakthrough
ax1.axvline(2010, color='green', linestyle='--', linewidth=1.5)
ax1.text(2010, 850, 'Technological Breakthrough', rotation=90, 
         verticalalignment='center', fontsize=11, color='green')

# Customize grid and ticks
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.tick_params(axis='y', labelcolor='navy')
ax2.tick_params(axis='y', labelcolor='darkred')

# Add legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=False, fontsize=11)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()