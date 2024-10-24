import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Primary Data: Crop Yields over Time
years = np.array([2000, 2003, 2006, 2009, 2012, 2015, 2018, 2021, 2024])
crop_yields = np.array([2.5, 2.7, 3.0, 3.3, 3.8, 4.1, 4.5, 5.0, 5.4])

# Secondary Data: Average Annual Precipitation (made-up data for illustration)
precipitation = np.array([800, 820, 780, 750, 850, 870, 890, 900, 920])  # mm per year

# Prepare smooth curve data for the primary plot
x_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, crop_yields, k=3)
yield_smooth = spl(x_smooth)

# Create a figure with 1 row and 2 columns for subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Subplot 1: Crop Yields
axes[0].scatter(years, crop_yields, color='darkorange', s=100, edgecolor='black', label='Observed Yields')
axes[0].plot(x_smooth, yield_smooth, color='blue', linestyle='-', linewidth=2, label='Yield Trend Line')

for year, yield_val in zip(years, crop_yields):
    axes[0].text(year, yield_val + 0.1, f"{yield_val:.1f}", fontsize=9, ha='center')

axes[0].set_title('Evolution of Drought-Resilient Crop Yields\n2000-2024', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Yield (Tons per Hectare)', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(title='Legend', fontsize=10, loc='upper left')

axes[0].annotate('Major Genetic Breakthrough', xy=(2018, 4.5), xytext=(2010, 4.0),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                 fontsize=11, color='black', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

# Subplot 2: Precipitation as a Bar Chart
axes[1].bar(years, precipitation, color='skyblue', edgecolor='black')
axes[1].set_title('Annual Precipitation Affecting Crop Yield', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Precipitation (mm)', fontsize=12)

for year, precip_val in zip(years, precipitation):
    axes[1].text(year, precip_val + 10, f"{precip_val}", fontsize=9, ha='center')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()