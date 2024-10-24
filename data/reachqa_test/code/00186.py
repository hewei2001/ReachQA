import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.cm as cm

# Data for the release years and corresponding processing power of tech gadgets
release_years = np.array([1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023])
processing_power = np.array([10, 15, 22, 30, 40, 55, 80, 110, 150, 200])

# Calculate a color map to represent processing power
colors = cm.viridis((processing_power - min(processing_power)) / (max(processing_power) - min(processing_power)))

# Create a scatter plot of the data
fig, ax = plt.subplots(figsize=(12, 7))
sc = ax.scatter(release_years, processing_power, c=colors, s=100, cmap='viridis', label='Gadget Data Points', alpha=0.8, edgecolors='w', linewidth=0.5)

# Add color bar for processing power
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Processing Power Intensity', fontsize=11)

# Fit a polynomial curve to the data (degree 3 for smooth fitting)
polynomial_coeff = Polynomial.fit(release_years, processing_power, deg=3)
poly_curve = polynomial_coeff.linspace(n=200, domain=[1980, 2023])

# Plot the polynomial fitting curve
ax.plot(poly_curve[0], poly_curve[1], color='red', linestyle='-.', linewidth=2, label='Fitting Curve')

# Titles and labels
ax.set_title('Advancements in Tech Gadget\nProcessing Power From 1980 to 2023', fontsize=16, weight='bold', loc='center')
ax.set_xlabel('Release Year', fontsize=12)
ax.set_ylabel('Processing Power (Arbitrary Units)', fontsize=12)

# Customize grid, legend, and axis
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=10, frameon=True)
ax.set_xlim(1978, 2025)
ax.set_ylim(0, 220)
ax.set_xticks(release_years)
plt.xticks(rotation=45)

# Annotate some key data points for emphasis
annotations = {1980: 'Early Computers', 2000: 'PC Era', 2020: 'Smartphones'}
for year, label in annotations.items():
    power = processing_power[np.where(release_years == year)][0]
    ax.annotate(label, xy=(year, power), xytext=(-40, 15), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.3'), fontsize=9, bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='lightyellow', alpha=0.8))

# Adjust layout to ensure everything fits
plt.tight_layout()

# Show the plot
plt.show()