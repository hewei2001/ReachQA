import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Extend the range of years and add more celestial objects
years = np.arange(2000, 2026)

# Constructing more detailed luminosity data and errors
alpha_centauri_luminosity = np.array(
    [1.0, 1.02, 1.01, 1.03, 1.05, 1.04, 1.03, 1.06, 1.08, 1.1, 1.12, 
     1.13, 1.14, 1.15, 1.17, 1.18, 1.2, 1.22, 1.23, 1.25, 1.3, 1.32, 1.33, 1.35, 1.37, 1.4])
betelgeuse_luminosity = np.array(
    [5.0, 5.1, 5.15, 5.2, 5.25, 5.3, 5.4, 5.5, 5.55, 5.6, 5.7, 5.8, 
     5.9, 6.0, 6.1, 6.2, 6.3, 6.35, 6.4, 6.5, 6.6, 6.7, 6.75, 6.8, 6.9, 7.0])
proxima_centauri_luminosity = np.array(
    [0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 
     0.44, 0.45, 0.47, 0.48, 0.5, 0.51, 0.52, 0.54, 0.55, 0.56, 0.57, 0.58, 0.6, 0.62])
sirius_luminosity = np.array(
    [1.8, 1.85, 1.9, 1.92, 1.95, 2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 
     2.35, 2.38, 2.4, 2.42, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9])

# Simulated error margins for luminosity readings
alpha_centauri_errors = np.full(years.shape, 0.02)
betelgeuse_errors = np.full(years.shape, 0.1)
proxima_centauri_errors = np.full(years.shape, 0.04)
sirius_errors = np.full(years.shape, 0.05)

# Create the main plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot with error bars
ax.errorbar(years, alpha_centauri_luminosity, yerr=alpha_centauri_errors, fmt='-o', label='Alpha Centauri', color='#1f77b4', capsize=4, alpha=0.8)
ax.errorbar(years, betelgeuse_luminosity, yerr=betelgeuse_errors, fmt='-s', label='Betelgeuse', color='#ff7f0e', capsize=4, alpha=0.8)
ax.errorbar(years, proxima_centauri_luminosity, yerr=proxima_centauri_errors, fmt='-^', label='Proxima Centauri', color='#2ca02c', capsize=4, alpha=0.8)
ax.errorbar(years, sirius_luminosity, yerr=sirius_errors, fmt='-d', label='Sirius', color='#d62728', capsize=4, alpha=0.8)

# Polynomial trend lines
for lum_data, color, name in zip(
        [alpha_centauri_luminosity, betelgeuse_luminosity, proxima_centauri_luminosity, sirius_luminosity],
        ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        ['Alpha Centauri Trend', 'Betelgeuse Trend', 'Proxima Centauri Trend', 'Sirius Trend']):
    p = Polynomial.fit(years, lum_data, deg=3)
    ax.plot(years, p(years), linestyle='--', color=color, alpha=0.5, label=f'{name}')

# Main plot title and labels
ax.set_title('Luminosity Trends of Various Celestial Objects (2000-2025)\nWith Polynomial Trend Lines', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Luminosity (Arbitrary Units)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(years[::2])  # Show every second year to avoid clutter

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Celestial Objects', frameon=False)
ax.grid(axis='both', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Cumulative sum subplot
cum_sum_ax = fig.add_subplot(212)
cum_sum_ax.set_title('Cumulative Luminosity Sum (2000-2025)', fontsize=14, fontweight='bold', pad=15)
cum_sum_ax.set_xlabel('Year', fontsize=12)
cum_sum_ax.set_ylabel('Cumulative Luminosity (Arbitrary Units)', fontsize=12)
cum_sum_ax.plot(years, np.cumsum(alpha_centauri_luminosity), '-o', label='Alpha Centauri', color='#1f77b4', alpha=0.8)
cum_sum_ax.plot(years, np.cumsum(betelgeuse_luminosity), '-s', label='Betelgeuse', color='#ff7f0e', alpha=0.8)
cum_sum_ax.plot(years, np.cumsum(proxima_centauri_luminosity), '-^', label='Proxima Centauri', color='#2ca02c', alpha=0.8)
cum_sum_ax.plot(years, np.cumsum(sirius_luminosity), '-d', label='Sirius', color='#d62728', alpha=0.8)

# Add grid and legend
cum_sum_ax.legend(loc='upper left', fontsize=10, frameon=False)
cum_sum_ax.grid(axis='both', linestyle='--', alpha=0.7)

# Display the plots
plt.show()