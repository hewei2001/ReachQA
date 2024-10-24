import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the metrics and space missions
metrics = ['Scientific Contribution', 'Technology Development', 'Mission Duration', 'Budget Efficiency', 'Public Engagement']
missions = ['Lunar Quest', 'Mars Odyssey', 'Jupiter Gateway']

# Data for each mission (0-10 scale)
mission_data = {
    'Lunar Quest': [8, 6, 7, 9, 5],
    'Mars Odyssey': [9, 8, 6, 5, 7],
    'Jupiter Gateway': [7, 7, 8, 6, 9]
}

# Setup radar chart framework
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.title('Cosmic Exploration Metrics:\nComparative Analysis of Space Missions', size=14, weight='bold', pad=20)

# Compute angle for each metric
num_vars = len(metrics)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle for closing the loop

# Function to plot each mission's metrics
def create_radar_chart(mission_name, color):
    mission_values = mission_data[mission_name]
    mission_values += mission_values[:1]  # Close the loop for radar chart
    ax.plot(angles, mission_values, color=color, linewidth=2, label=f"{mission_name}")
    ax.fill(angles, mission_values, color=color, alpha=0.25)

# Plot each mission with specified colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, mission in enumerate(missions):
    create_radar_chart(mission, colors[i])

# Customize chart appearance
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics, color='grey', size=10, ha='center')
ax.yaxis.grid(True, linestyle='--')

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize='small', ncol=1)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()