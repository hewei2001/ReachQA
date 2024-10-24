import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Sleep Duration (hours) vs. Productivity Index
sleep_duration = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9])
productivity_index = np.array([55, 60, 65, 70, 80, 85, 90, 85, 75])

# New data: Energy Levels
energy_levels = np.array([50, 52, 60, 68, 78, 82, 88, 83, 72])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Scatter plot for Productivity Index
scatter = ax1.scatter(sleep_duration, productivity_index, color='royalblue', edgecolors='black', s=100, label='Observed Productivity', zorder=2)

# Smooth fitting curve using B-Spline interpolation
x_smooth = np.linspace(sleep_duration.min(), sleep_duration.max(), 300)
spl = make_interp_spline(sleep_duration, productivity_index, k=3)
y_smooth = spl(x_smooth)
line = ax1.plot(x_smooth, y_smooth, color='darkorange', linewidth=2.5, linestyle='--', label='Trend Line', zorder=1)

# Bar plot for Energy Levels
ax2 = ax1.twinx()  # Create a secondary y-axis
bars = ax2.bar(sleep_duration, energy_levels, width=0.3, color='limegreen', alpha=0.6, label='Energy Levels', zorder=0)

# Titles and labels
plt.title("Impact of Sleep Duration on Creative Productivity and Energy Levels:\nInsights from the SomniTech Study", fontsize=14, fontweight='bold')
ax1.set_xlabel("Average Sleep Duration (hours)", fontsize=12)
ax1.set_ylabel("Productivity Index", fontsize=12, color='royalblue')
ax2.set_ylabel("Energy Levels", fontsize=12, color='limegreen')

# Grid
ax1.grid(visible=True, linestyle='--', alpha=0.6)

# Legends
scatter_legend = ax1.legend(loc='upper left', fontsize=10)
bars_legend = ax2.legend(loc='upper right', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()