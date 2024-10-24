import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define data for the analysis
years = np.arange(2010, 2020)
bicycle_lanes_km = np.array([10, 12, 15, 18, 21, 25, 30, 35, 40, 45])
traffic_congestion_index = np.array([75, 73, 70, 67, 65, 62, 58, 55, 53, 50])

# Calculating the annual growth rate of bicycle lanes and reduction rate of congestion
bicycle_growth_rate = np.diff(bicycle_lanes_km) / bicycle_lanes_km[:-1] * 100
congestion_reduction_rate = -np.diff(traffic_congestion_index) / traffic_congestion_index[:-1] * 100

# Create a 1x2 subplot
fig, ax = plt.subplots(1, 2, figsize=(16, 6), constrained_layout=True)

# First plot: Scatter chart with cubic spline interpolation
ax[0].scatter(bicycle_lanes_km, traffic_congestion_index, color='dodgerblue', label='Data Points', s=80, edgecolors='w', zorder=5)
x_smooth = np.linspace(bicycle_lanes_km.min(), bicycle_lanes_km.max(), 300)
spl = make_interp_spline(bicycle_lanes_km, traffic_congestion_index, k=3)
y_smooth = spl(x_smooth)
ax[0].plot(x_smooth, y_smooth, color='darkorange', linewidth=2, label='Trend Line')

# Adding details to the first subplot
ax[0].set_title('Impact of Bicycle Lanes on Traffic Congestion\nA Decade in Review (2010-2019)', fontsize=16, weight='bold', pad=15)
ax[0].set_xlabel('Bicycle Lanes (km)', fontsize=12)
ax[0].set_ylabel('Traffic Congestion Index', fontsize=12)
ax[0].invert_yaxis()
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(loc='upper right', fontsize=10)

# Second plot: Bar chart for growth and reduction rates
years_for_rate = years[1:]  # Years are offset by one due to diff
width = 0.35  # Width for bar plots
ax[1].bar(years_for_rate - width/2, bicycle_growth_rate, width, color='teal', label='Bicycle Growth Rate (%)')
ax[1].bar(years_for_rate + width/2, congestion_reduction_rate, width, color='salmon', label='Congestion Reduction Rate (%)')

# Adding details to the second subplot
ax[1].set_title('Growth Rate of Bicycle Lanes vs.\nReduction Rate of Traffic Congestion (2011-2019)', fontsize=16, weight='bold', pad=15)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Rate (%)', fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].set_xticks(years_for_rate)
ax[1].legend(loc='upper right', fontsize=10)

# Show the plots
plt.show()