import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define years and corresponding number of published titles
years = np.arange(2000, 2021)

# Simulated data: Number of digital and print publications
digital_publications = np.array([10, 20, 30, 40, 60, 90, 130, 180, 250, 350, 460, 580, 700, 850, 1000, 1200, 1450, 1700, 2000, 2300, 2600])
print_publications = np.array([3000, 3100, 3200, 3300, 3350, 3400, 3450, 3500, 3520, 3530, 3540, 3550, 3555, 3558, 3560, 3562, 3565, 3570, 3575, 3578, 3580])

# Create a smooth curve for the data
years_new = np.linspace(years.min(), years.max(), 300)

# Smooth fitting using cubic spline
spl_digital = make_interp_spline(years, digital_publications, k=3)
smooth_digital = spl_digital(years_new)
spl_print = make_interp_spline(years, print_publications, k=3)
smooth_print = spl_print(years_new)

# Plot the scatter chart with smooth fitting
plt.figure(figsize=(14, 10))
plt.scatter(years, digital_publications, color='dodgerblue', label='Digital Publications', alpha=0.7, edgecolor='k')
plt.scatter(years, print_publications, color='tomato', label='Print Publications', alpha=0.7, edgecolor='k')
plt.plot(years_new, smooth_digital, color='dodgerblue', linestyle='-', linewidth=2, label='Digital Trend')
plt.plot(years_new, smooth_print, color='tomato', linestyle='-', linewidth=2, label='Print Trend')

# Highlight the year digital surpasses print
crossover_index = np.argmax(smooth_digital > smooth_print)
crossover_year = int(years_new[crossover_index])
plt.axvline(x=crossover_year, color='gray', linestyle='--', linewidth=1)
plt.text(crossover_year + 0.5, 1500, f'Crossover in {crossover_year}', rotation=90, verticalalignment='center', fontsize=10, color='gray')

# Adding titles and labels
plt.title('The Rise of Digital Publishing\nA Comparative Analysis Over Two Decades (2000-2020)', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Published Titles', fontsize=12)

# Add a filled area between the curves
plt.fill_between(years_new, smooth_digital, smooth_print, where=(smooth_digital > smooth_print), interpolate=True, color='lightblue', alpha=0.2, label='Digital > Print')
plt.fill_between(years_new, smooth_digital, smooth_print, where=(smooth_digital <= smooth_print), interpolate=True, color='lightcoral', alpha=0.2, label='Print > Digital')

# Add legend and grid
plt.legend(loc='upper left', fontsize=10)
plt.grid(alpha=0.3)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()