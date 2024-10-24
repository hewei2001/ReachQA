import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average battery life in hours for each year
battery_life = np.array([6, 6.5, 7, 7.8, 8.5, 9.3, 9.8, 10.2, 10.5, 11, 11.5])

# Variability in battery life due to usage patterns
variability = np.array([0.5, 0.6, 0.7, 0.9, 1.0, 1.2, 1.3, 1.1, 1.2, 1.3, 1.4])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot average battery life with error bars
ax.errorbar(years, battery_life, yerr=variability, fmt='-o', ecolor='gray', capsize=5,
            capthick=2, color='green', alpha=0.8, label='Battery Life Trends')

# Add a grid for easier reading
ax.grid(True, linestyle='--', alpha=0.6)

# Customizing the plot
ax.set_title("Evolution of Smartphone Battery Life (2010-2020)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Average Battery Life (hours)", fontsize=12)
ax.set_ylim(5, 13)
ax.set_xlim(2009, 2021)

# Adding the legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()