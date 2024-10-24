import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years of observation
years = np.arange(2010, 2021)

# Average trunk diameter data (in cm) for different tree species over the years
oak_diameter = np.array([5, 5.5, 6.2, 6.8, 7.5, 8.1, 9.0, 9.8, 10.5, 11.3, 12])
maple_diameter = np.array([4, 4.4, 5, 5.5, 6, 6.6, 7.3, 8, 8.7, 9.5, 10.3])
pine_diameter = np.array([3, 3.5, 4, 4.6, 5.2, 5.9, 6.5, 7.2, 7.9, 8.6, 9.3])

# Calculate the growth rate (first derivative)
oak_growth_rate = np.gradient(oak_diameter)
maple_growth_rate = np.gradient(maple_diameter)
pine_growth_rate = np.gradient(pine_diameter)

# Create a smooth curve fitting
years_new = np.linspace(years.min(), years.max(), 300)
oak_spline = make_interp_spline(years, oak_diameter, k=3)
maple_spline = make_interp_spline(years, maple_diameter, k=3)
pine_spline = make_interp_spline(years, pine_diameter, k=3)
oak_smooth = oak_spline(years_new)
maple_smooth = maple_spline(years_new)
pine_smooth = pine_spline(years_new)

# Plot setup
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 12))

# Plot: Average Trunk Diameter
ax1.scatter(years, oak_diameter, color='forestgreen', label='Oak Tree', zorder=5)
ax1.scatter(years, maple_diameter, color='saddlebrown', label='Maple Tree', zorder=5)
ax1.scatter(years, pine_diameter, color='darkslategray', label='Pine Tree', zorder=5)
ax1.plot(years_new, oak_smooth, color='forestgreen', linestyle='-', linewidth=2, alpha=0.7)
ax1.plot(years_new, maple_smooth, color='saddlebrown', linestyle='--', linewidth=2, alpha=0.7)
ax1.plot(years_new, pine_smooth, color='darkslategray', linestyle=':', linewidth=2, alpha=0.7)

# Annotation for notable points
ax1.annotate('Highest Growth', xy=(2018, 11.3), xytext=(2017, 12),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

ax1.set_title('Tree Growth Patterns in Urban GreenVille:\nAverage Trunk Diameter (2010-2020)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Trunk Diameter (cm)', fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(3, 13, 1))
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(title='Tree Species', fontsize=10, loc='upper left', title_fontsize=12)

# Plot: Growth Rate
ax2.bar(years - 0.2, oak_growth_rate, width=0.2, color='forestgreen', align='center', label='Oak Growth Rate')
ax2.bar(years, maple_growth_rate, width=0.2, color='saddlebrown', align='center', label='Maple Growth Rate')
ax2.bar(years + 0.2, pine_growth_rate, width=0.2, color='darkslategray', align='center', label='Pine Growth Rate')

ax2.set_title('Annual Growth Rate of Tree Species', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (cm/year)', fontsize=12)
ax2.set_xticks(years)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.legend(title='Growth Rate', fontsize=10, loc='upper left', title_fontsize=12)

# Improve layout and show plot
plt.tight_layout()
plt.show()