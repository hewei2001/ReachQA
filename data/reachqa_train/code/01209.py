import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2010, 2021)

# Average temperature data (in °C) for each climate zone with fictional trends
polar_temps = np.array([-20.0, -19.8, -19.7, -19.5, -19.2, -19.0, -18.8, -18.6, -18.4, -18.2, -18.0])
temperate_temps = np.array([10.0, 10.2, 10.3, 10.5, 10.7, 10.9, 11.0, 11.2, 11.4, 11.5, 11.7])
tropical_temps = np.array([25.0, 25.1, 25.2, 25.4, 25.6, 25.7, 25.8, 26.0, 26.1, 26.2, 26.3])

# Error values for each climate zone, representing measurement variability
polar_errors = np.full_like(polar_temps, 0.2)
temperate_errors = np.full_like(temperate_temps, 0.3)
tropical_errors = np.full_like(tropical_temps, 0.4)

# Set up plot styles for clarity and distinction
zone_styles = [
    {'color': '#1f78b4', 'marker': 'o'},  # Polar
    {'color': '#33a02c', 'marker': 's'},  # Temperate
    {'color': '#ff7f00', 'marker': '^'}   # Tropical
]

# Create the plot
plt.figure(figsize=(14, 8))

# Plot each climate zone with error bars
plt.errorbar(years, polar_temps, yerr=polar_errors, fmt='o-', color=zone_styles[0]['color'],
             marker=zone_styles[0]['marker'], capsize=5, elinewidth=2, markersize=6, alpha=0.9,
             label='Polar Zone')
plt.errorbar(years, temperate_temps, yerr=temperate_errors, fmt='s-', color=zone_styles[1]['color'],
             marker=zone_styles[1]['marker'], capsize=5, elinewidth=2, markersize=6, alpha=0.9,
             label='Temperate Zone')
plt.errorbar(years, tropical_temps, yerr=tropical_errors, fmt='^-', color=zone_styles[2]['color'],
             marker=zone_styles[2]['marker'], capsize=5, elinewidth=2, markersize=6, alpha=0.9,
             label='Tropical Zone')

# Set axis labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.title('Annual Average Temperature Variability (2010-2020)\nAcross Different Climate Zones', fontsize=14)

# Add legend, customized to avoid overlapping with data points
plt.legend(title="Climate Zone", fontsize=10, loc='upper left')

# Customize grid and layout for clarity
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout for a better fit and avoid occlusion
plt.tight_layout()

# Show the plot
plt.show()