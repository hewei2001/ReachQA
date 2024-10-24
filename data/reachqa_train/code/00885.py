import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # Importing Axes3D

# Celestial bodies and mission data
celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [30, 40, 25, 50, 60, 10],
    'Landers': [20, 10, 45, 10, 5, 20],
    'Flybys': [50, 50, 30, 40, 35, 70]
}

# New data for the pie chart: total mission types
total_missions = {key: sum(values) for key, values in missions_data.items()}

# Create subplots
fig = plt.figure(figsize=(16, 8))
ax1 = fig.add_subplot(121, projection='3d')  # 3D subplot
ax2 = fig.add_subplot(122)  # 2D subplot for pie chart

# 3D Bar Chart
x_pos = np.arange(len(celestial_bodies))
bar_width = 0.2
colors = ['#FF5733', '#33FFCE', '#335BFF']

for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    x_offset = bar_width * idx
    ax1.bar3d(x_pos + x_offset, [idx] * len(percentages), [0] * len(percentages), 
              bar_width, 0.4, percentages,
              color=colors[idx], alpha=0.8, label=mission_type)

ax1.set_xlabel('Celestial Body')
ax1.set_ylabel('Mission Type')
ax1.set_zlabel('Percentage (%)')
ax1.set_title('Exploration of Our Solar System:\nSpace Missions Breakdown', pad=30)
ax1.set_xticks(x_pos + bar_width)
ax1.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(missions_data)))
ax1.set_yticklabels(missions_data.keys())
ax1.set_zlim(0, 100)
ax1.legend(loc='upper left', fontsize=10, title='Mission Types')
ax1.view_init(elev=25, azim=120)

# Pie Chart
ax2.pie(total_missions.values(), labels=total_missions.keys(), autopct='%1.1f%%', startangle=140, colors=colors)
ax2.set_title('Overall Mission Type Distribution')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()