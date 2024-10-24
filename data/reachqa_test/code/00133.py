import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Original data
years = np.array([1995, 1997, 2000, 2003, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2025])
exoplanets_detected = np.array([3, 9, 25, 57, 127, 210, 331, 421, 504, 620, 780, 950, 1130, 1350])

# Related data for the overlay plot (number of active missions)
active_missions = np.array([1, 1, 2, 3, 5, 5, 6, 8, 9, 10, 11, 13, 14, 16])

# Smooth line for exoplanets detected
years_smooth = np.linspace(years.min(), years.max(), 300)
spline = make_interp_spline(years, exoplanets_detected, k=3)
exoplanets_smooth = spline(years_smooth)

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot and spline for exoplanets
ax1.scatter(years, exoplanets_detected, color='red', edgecolor='black', s=100, label='Detected Exoplanets')
ax1.plot(years_smooth, exoplanets_smooth, label='Trend Line (Spline Fit)', color='blue', linestyle='--', linewidth=2)

# Bar plot for active missions
ax2 = ax1.twinx()
ax2.bar(years, active_missions, color='green', alpha=0.5, width=0.7, label='Active Detection Missions')

# Titles and labels
ax1.set_title('Advancements in Exoplanet Detection (1995-2025)\nAn Astronomical Journey with Active Missions', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Exoplanets Detected', fontsize=12, color='blue')
ax2.set_ylabel('Number of Active Detection Missions', fontsize=12, color='green')

# Annotations
ax1.annotate('Kepler Launch', xy=(2009, 300), xytext=(2010, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='black')
ax1.annotate('TESS Mission', xy=(2018, 780), xytext=(2016, 1100),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
             fontsize=10, color='black')

# Legends
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Grid and layout
ax1.grid(alpha=0.3, linestyle='--', linewidth=0.5)
fig.tight_layout()

# Show plot
plt.show()