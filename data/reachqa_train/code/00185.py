import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years for which data is available
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])

# Adoption rates for different technology sectors
internet_usage = np.array([2, 10, 30, 45, 65, 85, 90])
mobile_devices = np.array([5, 20, 50, 60, 70, 88, 95])
cloud_computing = np.array([0, 1, 5, 15, 35, 55, 80])
artificial_intelligence = np.array([1, 2, 5, 8, 15, 30, 70])

# Calculate change rate as the difference between consecutive elements
def calculate_change_rate(data):
    return np.diff(data)

# Get smooth curves using spline interpolation
def get_smooth_curve(years, data):
    spline = make_interp_spline(years, data, k=3)
    smooth_years = np.linspace(years.min(), years.max(), 300)
    smooth_data = spline(smooth_years)
    return smooth_years, smooth_data

# Generate smooth curves for each sector
smooth_years_internet, smooth_internet_usage = get_smooth_curve(years, internet_usage)
smooth_years_mobile, smooth_mobile_devices = get_smooth_curve(years, mobile_devices)
smooth_years_cloud, smooth_cloud_computing = get_smooth_curve(years, cloud_computing)
smooth_years_ai, smooth_ai = get_smooth_curve(years, artificial_intelligence)

# Calculate change rates
years_midpoints = (years[:-1] + years[1:]) / 2
change_rate_internet = calculate_change_rate(internet_usage)
change_rate_mobile = calculate_change_rate(mobile_devices)
change_rate_cloud = calculate_change_rate(cloud_computing)
change_rate_ai = calculate_change_rate(artificial_intelligence)

# Create the figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First subplot for adoption trends
ax1 = axes[0]
ax1.set_title("Technology Adoption Trends (1990-2020)\nGrowth in Major Technology Sectors", fontsize=14, weight='bold')
ax1.scatter(years, internet_usage, color='darkblue', s=100, label='Internet Usage', alpha=0.6, edgecolor='black')
ax1.plot(smooth_years_internet, smooth_internet_usage, color='steelblue', linewidth=2)
ax1.scatter(years, mobile_devices, color='darkorange', s=100, label='Mobile Devices', alpha=0.6, edgecolor='black')
ax1.plot(smooth_years_mobile, smooth_mobile_devices, color='orange', linewidth=2)
ax1.scatter(years, cloud_computing, color='darkgreen', s=100, label='Cloud Computing', alpha=0.6, edgecolor='black')
ax1.plot(smooth_years_cloud, smooth_cloud_computing, color='green', linewidth=2)
ax1.scatter(years, artificial_intelligence, color='darkred', s=100, label='Artificial Intelligence', alpha=0.6, edgecolor='black')
ax1.plot(smooth_years_ai, smooth_ai, color='red', linewidth=2)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Adoption Rate (%)", fontsize=12)
ax1.set_xlim(1985, 2025)
ax1.set_ylim(0, 100)
ax1.set_xticks(np.arange(1990, 2025, 5))
ax1.set_yticks(np.arange(0, 101, 10))
ax1.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
ax1.grid(True, linestyle='--', alpha=0.6)

# Second subplot for change rates
ax2 = axes[1]
ax2.set_title("Rate of Adoption Change\nTechnology Sectors 1990-2020", fontsize=14, weight='bold')
width = 2
ax2.bar(years_midpoints, change_rate_internet, width, label='Internet Usage', color='steelblue', alpha=0.7)
ax2.bar(years_midpoints + width, change_rate_mobile, width, label='Mobile Devices', color='orange', alpha=0.7)
ax2.bar(years_midpoints + 2 * width, change_rate_cloud, width, label='Cloud Computing', color='green', alpha=0.7)
ax2.bar(years_midpoints + 3 * width, change_rate_ai, width, label='Artificial Intelligence', color='red', alpha=0.7)
ax2.set_xlabel("Year Midpoint", fontsize=12)
ax2.set_ylabel("Change Rate", fontsize=12)
ax2.set_xticks(years_midpoints + width)
ax2.set_xticklabels(["{}-{}".format(years[i], years[i+1]) for i in range(len(years)-1)])
ax2.legend(loc='upper right', fontsize=10, frameon=True, shadow=True)
ax2.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()