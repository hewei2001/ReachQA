import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data
installations = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
efficiency = np.array([12, 14, 16, 19, 21, 24, 27, 29, 31, 35])

# New overlay data: Investment in solar energy (in millions)
investment = np.array([30, 45, 60, 80, 95, 110, 130, 155, 180, 200])

# Create a smooth line for the scatter plot
x_smooth = np.linspace(installations.min(), installations.max(), 300)
spl = make_interp_spline(installations, efficiency, k=3)
y_smooth = spl(x_smooth)

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Primary axis: Scatter and smooth line plot for efficiency
ax1.scatter(installations, efficiency, color='#1f77b4', s=100, edgecolor='k', label='Efficiency Data Points')
ax1.plot(x_smooth, y_smooth, color='orange', linewidth=2, linestyle='--', label='Smooth Efficiency Trend')
ax1.set_xlabel('Number of Solar Installations (in thousands)', fontsize=12, labelpad=10)
ax1.set_ylabel('Solar Panel Efficiency (%)', fontsize=12, labelpad=10, color='#1f77b4')
ax1.tick_params(axis='y', labelcolor='#1f77b4')

# Annotations for data points
for i, (x, y) in enumerate(zip(installations, efficiency)):
    ax1.text(x, y + 0.7, f'{y}%', fontsize=9, ha='center', color='darkblue')

# Secondary axis: Bar plot for investment
ax2 = ax1.twinx()
ax2.bar(installations, investment, width=3, alpha=0.3, color='green', label='Investment in Solar (millions)')
ax2.set_ylabel('Investment in Solar Energy (in millions)', fontsize=12, labelpad=10, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and layout adjustments
plt.title('Evolution of Solar Energy Adoption\nwith Efficiency and Investment in Smart Cities', fontsize=14, fontweight='bold', pad=20)
fig.tight_layout()

# Legend management
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), bbox_transform=ax1.transAxes, fontsize=10)

# Display the plot
plt.show()