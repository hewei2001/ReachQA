import matplotlib.pyplot as plt
import numpy as np

# Define the focus areas for space missions
focus_areas = ['Research\n& Discovery', 'Life Support\nSystems', 'Spacecraft\nEngineering', 
               'Communication\nTechnologies', 'Planetary\nDefense']

# Data for "Mission Pioneering" and "Mission Frontier"
mission_pioneering = [8, 7, 9, 6, 5]
mission_frontier = [7, 8, 8, 7, 9]

# Number of focus areas
num_focus_areas = len(focus_areas)

# Function to create the radar chart
def radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_focus_areas, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    
    ax.plot(angles, data, color=color, linewidth=2, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Create the radar chart figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the data for each mission
radar_chart(ax, mission_pioneering[:], 'royalblue', 'Mission Pioneering')
radar_chart(ax, mission_frontier[:], 'darkorange', 'Mission Frontier')

# Customize the radar chart appearance
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Set the labels for each axis and align them properly
ax.set_xticks(np.linspace(0, 2 * np.pi, num_focus_areas, endpoint=False))
ax.set_xticklabels(focus_areas, ha='center')

# Set the range for each scale
ax.set_ylim(0, 10)

# Add title and legend
ax.set_title("Space Exploration Priorities in 2035:\nAn Astronaut's Perspective", fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Customize gridlines for better readability
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.5)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()