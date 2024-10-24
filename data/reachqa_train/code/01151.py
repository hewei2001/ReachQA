import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

# Expanded data for squirrel sightings in Greenhaven parks over a full day (24 hours)
hours = np.array(range(0, 24))  # hourly observation times
# Constructed dataset with identifiable patterns
sightings_day = np.array([15, 18, 20, 25, 30, 35, 50, 70, 65, 60, 55, 45,
                          30, 20, 25, 30, 45, 60, 75, 80, 50, 40, 30, 20])

# Simulated data for a different species or location in the park
sightings_night = np.array([5, 4, 3, 2, 1, 5, 10, 8, 6, 15, 20, 35, 50, 
                            60, 55, 50, 45, 30, 20, 15, 10, 8, 7, 5])

# Smooth curve fitting using spline interpolation
x_smooth = np.linspace(hours.min(), hours.max(), 400)
spl_day = make_interp_spline(hours, sightings_day, k=3)
sightings_smooth_day = spl_day(x_smooth)
spl_night = make_interp_spline(hours, sightings_night, k=3)
sightings_smooth_night = spl_night(x_smooth)

# Create plot
plt.figure(figsize=(14, 8))

# Scatter and line plot for each dataset
plt.scatter(hours, sightings_day, color='blue', edgecolors='k', s=80, label='Daytime Sightings')
plt.plot(x_smooth, sightings_smooth_day, color='cyan', linewidth=2, linestyle='-', label='Day Smooth Trend')
plt.scatter(hours, sightings_night, color='red', edgecolors='k', s=80, label='Nighttime Sightings')
plt.plot(x_smooth, sightings_smooth_night, color='magenta', linewidth=2, linestyle='--', label='Night Smooth Trend')

# Titles and labels
plt.title('Squirrel Activity in Greenhaven Parks:\nDay and Night Sightings Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=12)
plt.ylabel('Number of Squirrel Sightings', fontsize=12)

# Grid and Legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')

# Time ticks
plt.xticks(np.arange(0, 24, 1), labels=[f'{h}:00' for h in range(24)], rotation=45)

# Statistical Additions - Histogram
plt.twinx()  # Create a second y-axis
plt.hist(hours, bins=12, weights=sightings_day, color='cyan', alpha=0.2, label='Day Histogram')
plt.hist(hours, bins=12, weights=sightings_night, color='magenta', alpha=0.2, label='Night Histogram')
plt.ylabel('Cumulative Sightings', fontsize=12)

# Tight layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()