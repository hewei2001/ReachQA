import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data for stars in the Zeltron galaxy
surface_temperatures = np.array([3, 4, 5, 6, 7, 8, 9, 10])
luminosity = np.array([0.5, 1.5, 1.7, 2.1, 3.5, 6.1, 9.5, 12.3])

# Additional data for the average age of stars (in billions of years)
# Hypothetical relationship for added complexity
average_star_age = np.array([10, 8.5, 7, 6.5, 6, 5, 4.5, 4])

# Generate smooth curve fit for the original data
x_smooth = np.linspace(surface_temperatures.min(), surface_temperatures.max(), 300)
spl = make_interp_spline(surface_temperatures, luminosity, k=3)
y_smooth = spl(x_smooth)

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(12, 7))

# Scatter plot for luminosity vs. surface temperature
scatter = ax1.scatter(surface_temperatures, luminosity, color='blue', s=100, label='Stars in Zeltron', edgecolor='k', zorder=5)
ax1.plot(x_smooth, y_smooth, color='red', linewidth=2, label='Luminosity-Temperature Trend', zorder=4)

# Second y-axis for average star age
ax2 = ax1.twinx()
ax2.plot(surface_temperatures, average_star_age, color='green', linewidth=2, linestyle='--', marker='o', label='Average Star Age', zorder=3)

# Add titles and labels
plt.title('Luminosity vs. Surface Temperature of Stars\nin the Zeltron Galaxy with Star Age Overlay', fontsize=16, fontweight='bold')
ax1.set_xlabel('Surface Temperature (in thousands of Kelvin)', fontsize=13)
ax1.set_ylabel('Luminosity (Relative to the Sun)', fontsize=13, color='blue')
ax2.set_ylabel('Average Age of Stars (in billions of years)', fontsize=13, color='green')

# Add grid, legends, and customize plot
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2.5, 10.5)
ax1.set_ylim(0, 14)
ax2.set_ylim(3.5, 10.5)
ax1.set_xticks(np.arange(3, 11, 1))
ax1.set_yticks(np.arange(0, 15, 2))
ax2.set_yticks(np.arange(4, 11, 1))

# Add legends
ax1.legend(loc='upper left', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Add annotations
for i, txt in enumerate(luminosity):
    ax1.annotate(f'{txt}', (surface_temperatures[i], luminosity[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plot
plt.show()