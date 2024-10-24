import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define cities, seasons, and energy sources
cities = ["SolarVille", "WindTropolis", "HydroCity"]
seasons = ["Spring", "Summer", "Autumn", "Winter"]

# Energy outputs in megawatts for each source by city over four seasons
energy_data = {
    "SolarVille": {
        "solar": [200, 250, 220, 180],
        "wind": [80, 70, 90, 110],
        "hydro": [20, 20, 25, 15]
    },
    "WindTropolis": {
        "solar": [70, 60, 65, 50],
        "wind": [250, 270, 240, 260],
        "hydro": [30, 25, 35, 40]
    },
    "HydroCity": {
        "solar": [50, 40, 45, 60],
        "wind": [90, 80, 85, 95],
        "hydro": [300, 320, 310, 330]
    }
}

# Prepare plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')
bar_width = 0.2
bar_depth = 0.2
x_pos = np.arange(len(seasons))
colors = ['#FFD700', '#87CEEB', '#32CD32']
labels = ['Solar', 'Wind', 'Hydro']

# Plot bars for each city
for i, city in enumerate(cities):
    solar_y = energy_data[city]["solar"]
    wind_y = energy_data[city]["wind"]
    hydro_y = energy_data[city]["hydro"]

    ax.bar3d(x_pos + i*bar_width, i, 0, bar_width, bar_depth, solar_y, color=colors[0], alpha=0.8)
    ax.bar3d(x_pos + i*bar_width, i, solar_y, bar_width, bar_depth, wind_y, color=colors[1], alpha=0.8)
    ax.bar3d(x_pos + i*bar_width, i, np.array(solar_y) + np.array(wind_y), bar_width, bar_depth, hydro_y, color=colors[2], alpha=0.8)

# Configure axes
ax.set_xlabel('Season')
ax.set_ylabel('City')
ax.set_zlabel('Energy Output (MW)')
ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(seasons)
ax.set_yticks(range(len(cities)))
ax.set_yticklabels(cities)

# Adjust view for optimal visibility
ax.view_init(elev=20, azim=140)

# Title and legend
ax.set_title("Energy Production Dynamics\nin Futuristic Cities (2123)", fontsize=14, fontweight='bold')
ax.legend([plt.Rectangle((0,0),1,1,color=colors[0]), 
           plt.Rectangle((0,0),1,1,color=colors[1]), 
           plt.Rectangle((0,0),1,1,color=colors[2])], 
          labels, loc='upper left', fontsize=10, title="Energy Source")

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()