import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for Planet Xylon
xylon_sectors = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
xylon_concentration = np.array([8.1, 7.9, 8.5, 9.0, 8.7, 9.2, 9.5, 9.7, 10.1, 9.8])

# Data for Planet Zynith
zynith_sectors = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
zynith_concentration = np.array([7.2, 7.5, 7.9, 8.3, 8.0, 8.6, 8.9, 9.1, 9.4, 9.0])

# Additional Data: Zygonite extraction cost per sector
extraction_cost = np.array([10, 12, 15, 14, 13, 11, 16, 14, 13, 12])

# Create smooth lines using make_interp_spline
sectors_smooth = np.linspace(1, 10, 300)
xylon_spline = make_interp_spline(xylon_sectors, xylon_concentration, k=3)
xylon_smooth = xylon_spline(sectors_smooth)
zynith_spline = make_interp_spline(zynith_sectors, zynith_concentration, k=3)
zynith_smooth = zynith_spline(sectors_smooth)

# Plotting with subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 7))

# Subplot 1: Concentration Line and Scatter Plot
axs[0].scatter(xylon_sectors, xylon_concentration, color='royalblue', label='Planet Xylon', edgecolor='black', s=100)
axs[0].plot(sectors_smooth, xylon_smooth, color='royalblue', alpha=0.7, linewidth=2)
axs[0].scatter(zynith_sectors, zynith_concentration, color='mediumseagreen', label='Planet Zynith', edgecolor='black', s=100)
axs[0].plot(sectors_smooth, zynith_smooth, color='mediumseagreen', alpha=0.7, linewidth=2)

axs[0].set_title("Zygonite Concentration\nXylon vs. Zynith", fontsize=16, weight='bold')
axs[0].set_xlabel("Sector Number", fontsize=12)
axs[0].set_ylabel("Zygonite Concentration (g/m³)", fontsize=12)
axs[0].legend(title="Planets", title_fontsize='13', fontsize='12')
axs[0].grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Bar Chart for Extraction Cost
axs[1].bar(xylon_sectors, extraction_cost, color='coral', edgecolor='black')
axs[1].set_title("Zygonite Extraction Cost by Sector", fontsize=16, weight='bold')
axs[1].set_xlabel("Sector Number", fontsize=12)
axs[1].set_ylabel("Extraction Cost ($)", fontsize=12)
axs[1].set_xticks(range(1, 11))
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Show plot
plt.show()