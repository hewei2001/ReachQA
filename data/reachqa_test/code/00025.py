import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Data: Population Density (people/km²) vs Air Quality Index (AQI)
population_density = np.array([300, 800, 1200, 2000, 3000, 4000, 6000, 8000, 10000, 15000])
aqi = np.array([50, 55, 65, 70, 90, 95, 110, 130, 150, 180])

# Additional Data: Public Transport Usage (%)
public_transport_usage = np.array([30, 40, 50, 55, 60, 65, 70, 72, 75, 78])

# Fit a polynomial curve of degree 2 for AQI
p_aqi = Polynomial.fit(population_density, aqi, 2)
x_fit = np.linspace(population_density.min(), population_density.max(), 500)
y_fit_aqi = p_aqi(x_fit)

# Set up the main plot with the first y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for Population Density vs AQI
ax1.scatter(population_density, aqi, color='royalblue', label='City Data (AQI)', s=100, alpha=0.7, edgecolor='black')
ax1.plot(x_fit, y_fit_aqi, color='tomato', linestyle='--', linewidth=2, label='Trend Line (Polynomial Fit)')

# Adding title and labels
ax1.set_title('Urban Growth Impact on Air Quality\nPopulation Density vs. Air Quality Index and Public Transport Usage', fontsize=16)
ax1.set_xlabel('Population Density (people/km²)', fontsize=14)
ax1.set_ylabel('Air Quality Index (AQI)', fontsize=14)

# Adding grid
ax1.grid(linestyle='-', alpha=0.2)

# Set up the secondary y-axis for Public Transport Usage
ax2 = ax1.twinx()
ax2.set_ylabel('Public Transport Usage (%)', fontsize=14, color='green')
ax2.plot(population_density, public_transport_usage, color='green', marker='o', linestyle='-', linewidth=2, markersize=8, label='Transport Usage (%)', alpha=0.7)

# Adding legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()