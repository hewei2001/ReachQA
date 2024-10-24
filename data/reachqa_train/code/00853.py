import matplotlib.pyplot as plt
import numpy as np

# Celestial bodies and mission data as percentage
celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [30, 40, 25, 50, 60, 10],
    'Landers': [20, 10, 45, 10, 5, 20],
    'Flybys': [50, 50, 30, 40, 35, 70]
}

# Creating a figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# X and Y positions for bars
x_pos = np.arange(len(celestial_bodies))
y_pos = np.arange(len(missions_data))

# Bar dimensions
bar_width = 0.2
bar_depth = 0.4

# Colors for mission types
colors = ['#FF5733', '#33FFCE', '#335BFF'] 

# Plot each mission type
for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    x_offset = bar_width * idx  # Shifting each type on X-axis
    ax.bar3d(x_pos + x_offset, idx, [0] * len(percentages), bar_width, bar_depth, percentages,
             color=colors[idx], alpha=0.7, label=mission_type)

# Customize axis labels and ticks
ax.set_xlabel('Celestial Body', labelpad=15)
ax.set_ylabel('Mission Type', labelpad=15)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_title('Exploration of Our Solar System:\nA Breakdown of Space Missions', pad=30)

# Axis tick configurations
ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax.set_yticks(y_pos)
ax.set_yticklabels(missions_data.keys())
ax.set_zlim(0, 100)  # Normalize Z-axis to percentage scale

# Add a legend
ax.legend(loc='upper left', fontsize=10, title='Mission Types')

# Adjust layout to prevent overlap
plt.tight_layout()

# Viewing angle adjustments
ax.view_init(elev=25, azim=120)

# Display plot
plt.show()