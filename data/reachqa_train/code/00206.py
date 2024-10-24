import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Years and transportation modes
years = np.arange(2025, 2035)
transport_modes = ["Traditional Car", "Public Bus", "Bicycle", "Electric Scooter", 
                   "Autonomous Vehicle", "Hyperloop", "Flying Taxi"]

# Percentage preferences for each mode over the years
percentage_data = np.array([
    [30, 28, 25, 22, 20, 18, 16, 15, 13, 10],  # Traditional Car
    [25, 23, 21, 20, 18, 17, 15, 14, 13, 12],  # Public Bus
    [10, 11, 12, 13, 14, 15, 15, 16, 17, 18],  # Bicycle
    [5, 6, 7, 8, 9, 10, 12, 13, 14, 15],       # Electric Scooter
    [10, 12, 14, 16, 18, 20, 22, 23, 25, 27],  # Autonomous Vehicle
    [5, 6, 7, 8, 10, 12, 13, 15, 16, 18],      # Hyperloop
    [15, 14, 14, 13, 11, 8, 7, 5, 2, 0]        # Flying Taxi
])

# Set up the plot
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Axis ticks and labels
x_ticks = np.arange(len(transport_modes))
ax.set_xticks(x_ticks)
ax.set_xticklabels(transport_modes, rotation=45, ha='right')

y_ticks = np.arange(len(years))
ax.set_yticks(y_ticks)
ax.set_yticklabels(years)

ax.set_zlim(0, 100)
ax.set_zlabel('Preference (%)')

# Plotting each mode as a set of bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'orchid', 'deepskyblue', 'sandybrown']
bar_width = 0.5

for i, mode in enumerate(transport_modes):
    x_pos = np.ones_like(years) * x_ticks[i]
    y_pos = years - years[0]
    z_pos = np.zeros_like(years)
    dz = percentage_data[i]
    
    ax.bar3d(x_pos, y_pos, z_pos, bar_width, 1, dz, color=colors[i], alpha=0.7, label=mode)

# Title and legend
plt.title("Decadal Preferences in Future Transportation Modalities\n(2025-2034)", fontsize=16)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Transportation Modes')

# Adjust layout to fit everything
plt.tight_layout()

# Show plot
plt.show()