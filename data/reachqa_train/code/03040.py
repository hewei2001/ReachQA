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
plt.figure(figsize=(12, 8))
plt.scatter(years, digital_publications, color='dodgerblue', label='Digital Publications', alpha=0.7, edgecolor='k')
plt.scatter(years, print_publications, color='tomato', label='Print Publications', alpha=0.7, edgecolor='k')
plt.plot(years_new, smooth_digital, color='dodgerblue', linestyle='--', label='Digital Trend')
plt.plot(years_new, smooth_print, color='tomato', linestyle='--', label='Print Trend')

# Adding titles and labels
plt.title('The Rise of Digital Publishing\nOver Time (2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Published Titles', fontsize=12)

# Add legend and grid
plt.legend(loc='upper left', fontsize=10)
plt.grid(alpha=0.3)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()