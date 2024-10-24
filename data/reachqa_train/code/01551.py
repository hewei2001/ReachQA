import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding data
years = np.arange(2020, 2031, 0.5)  # Half-year increments
efficiency = 60 + 10 * np.log(years - 2019)  # Nonlinear growth pattern
latency = 150 / (years - 2019)  # Decrease over time
error_rate = 5 + np.sin(years - 2020) * 3  # Oscillating pattern

# Generate smooth curves using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 500)
efficiency_spline = make_interp_spline(years, efficiency, k=3)(years_smooth)
latency_spline = make_interp_spline(years, latency, k=3)(years_smooth)
error_rate_spline = make_interp_spline(years, error_rate, k=3)(years_smooth)

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot efficiency
ax1.scatter(years, efficiency, color='orange', s=70, edgecolors='k', label='Efficiency Data')
ax1.plot(years_smooth, efficiency_spline, 'b-', linewidth=2, label='Efficiency Trend')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Communication Efficiency (%)', fontsize=12, color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Adding a secondary y-axis for latency
ax2 = ax1.twinx()
ax2.plot(years_smooth, latency_spline, 'g--', linewidth=2, label='Latency Trend')
ax2.set_ylabel('Latency (ms)', fontsize=12, color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Plot error rate on the same axis but different style
ax1.plot(years_smooth, error_rate_spline, 'r:', linewidth=2, label='Error Rate Trend')

# Customize the chart
ax1.set_title('Interplanetary Communication Metrics Over Time\nMars-to-Earth Signals', 
              fontsize=16, fontweight='bold', pad=15)
ax1.set_xticks(np.arange(2020, 2031, 1))

# Annotate significant events
ax1.annotate('Efficiency Breakthrough', xy=(2026, efficiency_spline[160]), xytext=(2027, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Latency Stabilization', xy=(2027, latency_spline[200]), xytext=(2025, 50),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='g')

# Add legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# Grid and layout
ax1.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()

# Display the plot
plt.show()