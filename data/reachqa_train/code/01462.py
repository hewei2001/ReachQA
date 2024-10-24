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

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot lines with error bars
ax.errorbar(years, germany_energy, yerr=germany_errors, fmt='-o', capsize=5, label='Germany',
            color='green', linestyle='-', linewidth=2, marker='o')
ax.errorbar(years, france_energy, yerr=france_errors, fmt='-s', capsize=5, label='France',
            color='blue', linestyle='--', linewidth=2, marker='s')
ax.errorbar(years, spain_energy, yerr=spain_errors, fmt='-^', capsize=5, label='Spain',
            color='orange', linestyle='-.', linewidth=2, marker='^')

# Title and labels
ax.set_title('Renewable Energy Utilization in European Countries (2010-2020)\nWith Error Margins Showing Uncertainty', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Utilization (GWh)', fontsize=12)
ax.set_xticks(years)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()