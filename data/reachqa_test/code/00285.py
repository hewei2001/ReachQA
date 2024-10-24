import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data for eco-design trends
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
green_roofs_adoption = np.array([2, 8, 15, 25, 40, 60, 85])
solar_panels_adoption = np.array([1, 10, 25, 50, 70, 90, 120])
vertical_gardens_adoption = np.array([0, 5, 20, 30, 50, 75, 100])

# Smooth curve interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
green_roofs_smooth = make_interp_spline(years, green_roofs_adoption)(years_smooth)
solar_panels_smooth = make_interp_spline(years, solar_panels_adoption)(years_smooth)
vertical_gardens_smooth = make_interp_spline(years, vertical_gardens_adoption)(years_smooth)

# Additional data for cumulative adoption trends
cumulative_adoption = green_roofs_adoption + solar_panels_adoption + vertical_gardens_adoption

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# First subplot: Original line plot with trends
axes[0].scatter(years, green_roofs_adoption, color='green', label='Green Roofs', s=100, edgecolor='black', zorder=5)
axes[0].scatter(years, solar_panels_adoption, color='orange', label='Solar Panels', s=100, edgecolor='black', zorder=5)
axes[0].scatter(years, vertical_gardens_adoption, color='purple', label='Vertical Gardens', s=100, edgecolor='black', zorder=5)

axes[0].plot(years_smooth, green_roofs_smooth, color='green', linestyle='-', linewidth=2.5, label='Green Roofs Trend')
axes[0].plot(years_smooth, solar_panels_smooth, color='orange', linestyle='-', linewidth=2.5, label='Solar Panels Trend')
axes[0].plot(years_smooth, vertical_gardens_smooth, color='purple', linestyle='-', linewidth=2.5, label='Vertical Gardens Trend')

axes[0].set_title('Eco-Design Trends in Urban Architecture\n(1990-2020)', fontsize=16, fontweight='bold', pad=20)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Number of Urban Projects', fontsize=12)
axes[0].set_xticks(years)
axes[0].set_yticks(np.arange(0, 130, 10))
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(loc='upper left', fontsize=10, frameon=False)

# Second subplot: Stacked area plot for cumulative adoption
axes[1].stackplot(years, green_roofs_adoption, solar_panels_adoption, vertical_gardens_adoption,
                  labels=['Green Roofs', 'Solar Panels', 'Vertical Gardens'], colors=['green', 'orange', 'purple'], alpha=0.6)

axes[1].set_title('Cumulative Adoption of Eco-Designs', fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Cumulative Adoption', fontsize=12)
axes[1].set_xticks(years)
axes[1].set_yticks(np.arange(0, 250, 25))
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()