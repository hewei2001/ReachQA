import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define blade lengths and expanded elevation range
blade_lengths = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
elevations = np.arange(0, 1100, 100)

# Simulated efficiency data matrix (10 blade lengths x 11 elevation points)
efficiency_data = np.array([
    [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85],  # Blade length 30m
    [78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89],  # Blade length 35m
    [80, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92],  # Blade length 40m
    [83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95],  # Blade length 45m
    [85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97],  # Blade length 50m
    [86, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98],  # Blade length 55m
    [88, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100], # Blade length 60m
    [89, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101],# Blade length 65m
    [90, 92, 94, 95, 96, 97, 98, 99, 100, 101, 102],# Blade length 70m
    [91, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103]# Blade length 75m
])

# Prepare figure
fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(blade_lengths)))

# Plotting 3D scatter and 2D overlay with line plots
for idx, blade_length in enumerate(blade_lengths):
    # Scatter plot
    ax.scatter(elevations, efficiency_data[idx], color=colors[idx], label=f'Blade Length: {blade_length}m', s=75, alpha=0.8)
    # Connect with lines
    ax.plot(elevations, efficiency_data[idx], color=colors[idx], linewidth=1, alpha=0.6)

# Customize the plot
ax.set_title("Wind Turbine Efficiency Analysis\nby Blade Length and Elevation", fontsize=16, weight='bold', pad=15)
ax.set_xlabel("Elevation (m)", fontsize=12)
ax.set_ylabel("Efficiency (%)", fontsize=12)
ax.set_xlim(-50, 1050)
ax.set_ylim(70, 110)
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(title="Blade Lengths", title_fontsize='13', fontsize='10', loc='lower right')

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Show plot
plt.show()