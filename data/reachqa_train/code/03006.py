import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Simulated luminosity data for celestial objects (in arbitrary units)
alpha_centauri_luminosity = np.array([1.0, 1.05, 1.02, 1.03, 1.07, 1.05, 1.04, 1.06, 1.08, 1.07, 1.1])
betelgeuse_luminosity = np.array([5.0, 5.5, 5.2, 6.0, 5.8, 6.5, 6.3, 6.1, 5.9, 6.4, 6.6])
proxima_centauri_luminosity = np.array([0.2, 0.3, 0.35, 0.25, 0.4, 0.5, 0.45, 0.48, 0.42, 0.47, 0.5])

# Simulated error margins for luminosity readings
alpha_centauri_errors = np.array([0.02, 0.03, 0.02, 0.03, 0.01, 0.02, 0.02, 0.01, 0.03, 0.02, 0.01])
betelgeuse_errors = np.array([0.5, 0.4, 0.6, 0.7, 0.6, 0.5, 0.6, 0.5, 0.4, 0.7, 0.6])
proxima_centauri_errors = np.array([0.05, 0.04, 0.06, 0.05, 0.05, 0.06, 0.07, 0.06, 0.04, 0.05, 0.05])

# Plot the line chart with error bars
plt.figure(figsize=(12, 8))
plt.errorbar(years, alpha_centauri_luminosity, yerr=alpha_centauri_errors, fmt='-o', label='Alpha Centauri', color='#1f77b4', capsize=5, alpha=0.8)
plt.errorbar(years, betelgeuse_luminosity, yerr=betelgeuse_errors, fmt='-s', label='Betelgeuse', color='#ff7f0e', capsize=5, alpha=0.8)
plt.errorbar(years, proxima_centauri_luminosity, yerr=proxima_centauri_errors, fmt='-^', label='Proxima Centauri', color='#2ca02c', capsize=5, alpha=0.8)

# Title and labels
plt.title('Luminosity Trends of Celestial Objects (2010-2020)\nMeasuring Brightness Variations', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Luminosity (Arbitrary Units)', fontsize=12)

# Customize x-axis ticks
plt.xticks(years)

# Add legend
plt.legend(loc='upper right', fontsize=10, title='Celestial Objects')

# Add grid for readability
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()