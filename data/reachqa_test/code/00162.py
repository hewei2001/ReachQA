import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original Data: Number of trees planted (in thousands) and corresponding AQI
trees_planted = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
aqi_values = np.array([75, 70, 68, 63, 60, 57, 55, 53, 52, 50])

# New Data: Carbon Sequestration Rate (tons per 1,000 trees)
carbon_sequestration = np.array([12, 15, 18, 20, 22, 24, 25, 27, 29, 30])

# Fit a smooth curve for AQI using spline interpolation
spline_fit_aqi = make_interp_spline(trees_planted, aqi_values, k=3)
x_smooth = np.linspace(trees_planted.min(), trees_planted.max(), 500)
y_smooth_aqi = spline_fit_aqi(x_smooth)

# Create a dual-axis plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot and smooth curve for AQI
ax1.scatter(trees_planted, aqi_values, color='#2A9D8F', s=100, edgecolor='black', label='Observed AQI')
ax1.plot(x_smooth, y_smooth_aqi, color='#E76F51', linewidth=2, linestyle='-', label='Trend Line')
ax1.set_xlabel('Number of Trees Planted (in thousands)', fontsize=12)
ax1.set_ylabel('Air Quality Index (Lower is Better)', fontsize=12, color='#E76F51')
ax1.tick_params(axis='y', labelcolor='#E76F51')

# Add annotations to AQI data points
for x, y in zip(trees_planted, aqi_values):
    ax1.annotate(f"AQI {y}", (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='black')

# Secondary Y-axis for Carbon Sequestration
ax2 = ax1.twinx()
ax2.bar(trees_planted, carbon_sequestration, width=3, color='#264653', alpha=0.7, label='Carbon Sequestration')
ax2.set_ylabel('Carbon Sequestration (tons)', fontsize=12, color='#264653')
ax2.tick_params(axis='y', labelcolor='#264653')

# Title and Layout adjustments
plt.title('Impact of Tree Planting on Air Quality and Carbon Sequestration\nCity GreenFuture Analysis (2023)', 
          fontsize=16, fontweight='bold')
fig.tight_layout()

# Customize gridlines and add legends
ax1.grid(True, linestyle='--', alpha=0.5)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=10)

# Display the plot
plt.show()