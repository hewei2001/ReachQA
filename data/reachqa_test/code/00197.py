import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Original data: Average annual temperatures and corresponding butterfly population counts
average_temperatures = np.array([15, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25])
butterfly_counts = np.array([150, 180, 200, 210, 220, 230, 235, 240, 230, 220, 210, 190, 180, 160, 150, 140, 130, 110, 100, 90])

# Constructing data for the second plot: wing spans in relation to temperature
# Synthetic data: wing span grows with temperature initially, then decreases
wing_spans = 1.5 * (average_temperatures - 15)**2 + np.random.normal(0, 5, len(average_temperatures))

# Define a polynomial function for fitting
def polynomial(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Fit the polynomial to the population data
popt_population, _ = curve_fit(polynomial, average_temperatures, butterfly_counts)

# Create a smooth line for fitted polynomial
smooth_temperatures = np.linspace(average_temperatures.min(), average_temperatures.max(), 200)
smooth_population = polynomial(smooth_temperatures, *popt_population)

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Population vs Temperature
ax1.scatter(average_temperatures, butterfly_counts, color='darkorange', s=100, edgecolor='black', label='Observed Data')
ax1.plot(smooth_temperatures, smooth_population, color='forestgreen', linewidth=2.5, label='Polynomial Fit')
ax1.set_title("Impact of Rising Temperatures on Butterfly Populations", fontsize=16)
ax1.set_xlabel("Average Annual Temperature (°C)", fontsize=12)
ax1.set_ylabel("Butterfly Population Count", fontsize=12)
ax1.legend(loc='upper right', fontsize=10, frameon=True)
ax1.grid(True, linestyle='--', alpha=0.6)

# Second subplot: Wing Span vs Temperature (line plot)
ax2.plot(average_temperatures, wing_spans, color='royalblue', marker='o', linewidth=2, label='Wing Span')
ax2.set_title("Variation of Butterfly Wing Span with Temperature", fontsize=16)
ax2.set_xlabel("Average Annual Temperature (°C)", fontsize=12)
ax2.set_ylabel("Butterfly Wing Span (cm)", fontsize=12)
ax2.legend(loc='upper right', fontsize=10, frameon=True)
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the combined plot
plt.show()