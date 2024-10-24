import matplotlib.pyplot as plt
import numpy as np

# Define years and ocean zones
years = np.arange(2010, 2024)
oceans = ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean']

# Average surface temperatures for each ocean in degrees Celsius
temperature_pacific = np.array([23.1, 23.3, 23.4, 23.6, 23.7, 23.9, 24.0, 24.1, 24.3, 24.5, 24.6, 24.7, 24.8, 24.9])
temperature_atlantic = np.array([22.0, 22.1, 22.3, 22.5, 22.6, 22.8, 23.0, 23.1, 23.3, 23.5, 23.6, 23.8, 23.9, 24.0])
temperature_indian = np.array([24.5, 24.6, 24.7, 24.9, 25.0, 25.2, 25.3, 25.5, 25.6, 25.8, 26.0, 26.1, 26.2, 26.4])

# Errors representing variance in temperature readings
errors_pacific = np.array([0.15 for _ in range(len(years))])
errors_atlantic = np.array([0.10 for _ in range(len(years))])
errors_indian = np.array([0.12 for _ in range(len(years))])

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot line chart with error bars for each ocean
ax.errorbar(years, temperature_pacific, yerr=errors_pacific, label='Pacific Ocean', fmt='-o', capsize=4, capthick=1, color='tab:blue', alpha=0.8)
ax.errorbar(years, temperature_atlantic, yerr=errors_atlantic, label='Atlantic Ocean', fmt='-s', capsize=4, capthick=1, color='tab:green', alpha=0.8)
ax.errorbar(years, temperature_indian, yerr=errors_indian, label='Indian Ocean', fmt='-^', capsize=4, capthick=1, color='tab:red', alpha=0.8)

# Customize chart
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Surface Temperature (°C)', fontsize=12)
ax.set_title('Trends and Uncertainty in Oceanic Surface Temperatures (2010-2023)\nImplications for Marine Life Conservation', fontsize=14, fontweight='bold', loc='center', wrap=True)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Ocean Zones', loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()