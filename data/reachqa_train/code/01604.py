import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define original coffee consumption and productivity data
coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
productivity = np.array([3, 5, 8, 10, 11, 12, 11, 9, 6])

# Create additional data for stress levels and breaks taken
# Assuming stress levels rise significantly after 4 cups
stress_levels = np.array([1, 2, 3, 4, 6, 8, 10, 12, 15])
# Assuming breaks taken decrease with more coffee up to a point then increase
breaks_taken = np.array([5, 4, 3, 3, 2, 2, 3, 4, 5])

# Interpolate productivity for a smooth line
coffee_spline = make_interp_spline(coffee_consumption, productivity)
coffee_new = np.linspace(0, 8, 300)
productivity_smooth = coffee_spline(coffee_new)

# Set up the plot with a secondary y-axis for stress levels
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for coffee consumption vs productivity
ax1.scatter(coffee_consumption, productivity, color='brown', label='Observed Productivity', s=100, edgecolor='black')
ax1.plot(coffee_new, productivity_smooth, color='green', linewidth=2, alpha=0.7, label='Productivity Trend')

# Bar plot for breaks taken
ax2 = ax1.twinx()
ax2.bar(coffee_consumption, breaks_taken, color='lightblue', alpha=0.6, label='Breaks Taken', width=0.5, align='center')

# Plot for stress levels
ax1.plot(coffee_consumption, stress_levels, color='red', linestyle='--', linewidth=2, label='Stress Levels')

# Title and axis labels
ax1.set_title('Impact of Coffee Consumption on Productivity\nand Stress Levels in a Tech Startup', fontsize=16, fontweight='bold')
ax1.set_xlabel('Coffee Consumption (Cups per Day)', fontsize=12)
ax1.set_ylabel('Productivity & Stress Levels', fontsize=12, color='black')
ax2.set_ylabel('Breaks Taken', fontsize=12, color='lightblue')

# Customize ticks and grid
ax1.set_xticks(np.arange(0, 9, step=1))
ax1.set_yticks(np.arange(0, 16, step=2))
ax2.set_yticks(np.arange(0, 6, step=1))
ax1.grid(alpha=0.3, linestyle='--')

# Legends
ax1.legend(loc='upper left', fontsize=10, edgecolor='gray')
ax2.legend(loc='upper right', fontsize=10, edgecolor='gray')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()