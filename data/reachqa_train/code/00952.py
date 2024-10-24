import matplotlib.pyplot as plt
import numpy as np

# Years for the study
years = np.arange(2015, 2026)

# Estimated deer population over the years
population_estimates = np.array([150, 160, 172, 180, 190, 205, 215, 220, 230, 240, 250])

# Error margins for each year
population_errors = np.array([5, 7, 6, 8, 5, 7, 6, 7, 8, 6, 7])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the line chart with error bars
ax.errorbar(years, population_estimates, yerr=population_errors, fmt='-o', color='forestgreen', ecolor='lightgray',
            elinewidth=3, capsize=5, capthick=2, marker='s', markersize=8, markerfacecolor='orange', 
            label='Estimated Population with Uncertainty')

# Set chart title and labels
ax.set_title("Wildlife Conservation Efforts:\nMonitoring Deer Population Growth with Uncertainty (2015-2025)",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Estimated Deer Population", fontsize=14)

# Set grid, legend, and axis limits
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=12)
ax.set_xlim(2014, 2026)
ax.set_ylim(140, 260)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()