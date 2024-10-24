import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import matplotlib.ticker as ticker

# Simulated Data: Duration of podcast episodes (minutes) and engagement level (% listened)
episode_durations = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
engagement_levels = np.array([75, 78, 80, 85, 88, 90, 87, 85, 82, 79, 77, 73])

# Create a smooth curve using B-spline interpolation
x_new = np.linspace(episode_durations.min(), episode_durations.max(), 300)
spline = make_interp_spline(episode_durations, engagement_levels, k=3)
engagement_smooth = spline(x_new)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot for raw data points
ax.scatter(episode_durations, engagement_levels, color='mediumblue', label='Episode Engagement', zorder=3)

# Plot for smooth fitting curve with shaded area
ax.plot(x_new, engagement_smooth, color='darkorange', linewidth=2, label='Engagement Trend', zorder=2)
ax.fill_between(x_new, engagement_smooth, color='orange', alpha=0.1)

# Annotations for significant points
peaks = [(30, 88), (35, 90)]
for x, y in peaks:
    ax.annotate(f'Peak: {y}%', xy=(x, y), xytext=(x+5, y+2),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Title and labels
ax.set_title('The Evolution of Engagement in\nHistorical Podcasts', fontsize=16, pad=20)
ax.set_xlabel('Episode Duration (minutes)', fontsize=14)
ax.set_ylabel('Engagement Level (% Listened)', fontsize=14)

# Grid with customized style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Customize ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))

# Axis limits
ax.set_xlim(5, 70)
ax.set_ylim(70, 95)

# Legend with enhanced styling
ax.legend(loc='upper right', fontsize=12, frameon=False)

# Adding a secondary y-axis to show engagement relative change
def relative_change(data):
    return (data - data[0]) / data[0] * 100

ax2 = ax.twinx()
ax2.plot(episode_durations, relative_change(engagement_levels), color='green', linestyle='--', linewidth=1.5, label='Relative Change', zorder=1)
ax2.set_ylabel('Relative Change (%)', fontsize=14)
ax2.yaxis.set_major_formatter(ticker.PercentFormatter())

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()