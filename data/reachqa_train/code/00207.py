import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data setup
years = np.arange(2025, 2035)
transport_modes = ["Traditional Car", "Public Bus", "Bicycle", "Electric Scooter", 
                   "Autonomous Vehicle", "Hyperloop", "Flying Taxi"]

percentage_data = np.array([
    [30, 28, 25, 22, 20, 18, 16, 15, 13, 10],
    [25, 23, 21, 20, 18, 17, 15, 14, 13, 12],
    [10, 11, 12, 13, 14, 15, 15, 16, 17, 18],
    [5, 6, 7, 8, 9, 10, 12, 13, 14, 15],
    [10, 12, 14, 16, 18, 20, 22, 23, 25, 27],
    [5, 6, 7, 8, 10, 12, 13, 15, 16, 18],
    [15, 14, 14, 13, 11, 8, 7, 5, 2, 0]
])

# Set up the plot
fig = plt.figure(figsize=(18, 12))
ax = fig.add_subplot(111, projection='3d')

x_ticks = np.arange(len(transport_modes))
ax.set_xticks(x_ticks)
ax.set_xticklabels(transport_modes, rotation=30, ha='right', fontsize=10)

y_ticks = np.arange(len(years))
ax.set_yticks(y_ticks)
ax.set_yticklabels(years)

ax.set_zlim(0, 100)
ax.set_zlabel('Preference (%)', fontsize=12)

# Plot each mode
colors = ['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', '#B276B2', '#DECF3F']
bar_width = 0.5

for i, mode in enumerate(transport_modes):
    x_pos = np.ones_like(years) * x_ticks[i]
    y_pos = years - years[0]
    z_pos = np.zeros_like(years)
    dz = percentage_data[i]
    
    ax.bar3d(x_pos, y_pos, z_pos, bar_width, 1, dz, color=colors[i], alpha=0.9, label=mode)
    
    # Add annotations for the max preference in each mode
    max_year_index = np.argmax(dz)
    ax.text(x_pos[max_year_index], y_pos[max_year_index], dz[max_year_index] + 2, 
            f'{dz[max_year_index]}%', color='black', ha='center', va='bottom', fontsize=9)

# Grid and background
ax.xaxis._axinfo['grid'].update(color='gray', linestyle='-', alpha=0.5)
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='-', alpha=0.5)
ax.zaxis._axinfo['grid'].update(color='gray', linestyle='-', alpha=0.5)

# Title and legend
plt.title("Decadal Preferences in Future Transportation Modalities\n2025-2034", fontsize=18, ha='center')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Modes', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()