import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Simulated Data: Duration of podcast episodes (minutes) and engagement level (% listened)
episode_durations = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
engagement_levels = np.array([75, 78, 80, 85, 88, 90, 87, 85, 82, 79, 77, 73])

# Create a smooth curve using B-spline interpolation
x_new = np.linspace(episode_durations.min(), episode_durations.max(), 300)
spline = make_interp_spline(episode_durations, engagement_levels, k=3)
engagement_smooth = spline(x_new)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot for raw data points
ax.scatter(episode_durations, engagement_levels, color='blue', label='Episode Engagement')

# Plot for smooth fitting curve
ax.plot(x_new, engagement_smooth, color='orange', linewidth=2, label='Engagement Trend')

# Title and labels
ax.set_title('The Evolution of Engagement\nin Historical Podcasts', fontsize=14, pad=20)
ax.set_xlabel('Episode Duration (minutes)', fontsize=12)
ax.set_ylabel('Engagement Level (% Listened)', fontsize=12)

# Legend and grid
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# Axis limits for better visualization
ax.set_xlim(5, 70)
ax.set_ylim(70, 95)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()