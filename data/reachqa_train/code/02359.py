import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Define focus areas and data for missions
focus_areas = ['Research\n& Discovery', 'Life Support\nSystems', 'Spacecraft\nEngineering', 
               'Communication\nTechnologies', 'Planetary\nDefense']
mission_pioneering = [8, 7, 9, 6, 5]
mission_frontier = [7, 8, 8, 7, 9]

# Append the first value to the end to close the radar chart loop
mission_pioneering += mission_pioneering[:1]
mission_frontier += mission_frontier[:1]

# Number of focus areas
num_focus_areas = len(focus_areas)

# Set angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_focus_areas, endpoint=False).tolist()
angles += angles[:1]

# Create custom colormap for gradient fill
cmap_pioneering = LinearSegmentedColormap.from_list("pioneering_grad", ["royalblue", "lightsteelblue"])
cmap_frontier = LinearSegmentedColormap.from_list("frontier_grad", ["darkorange", "moccasin"])

# Create radar chart figure
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Function to add data to radar chart
def radar_chart(ax, data, color, label, cmap):
    ax.plot(angles, data, color=color, linewidth=2, label=label, marker='o')
    ax.fill(angles, data, color=color, alpha=0.25)
    # Add gradient fill
    ax.fill_between(angles, 0, data, color=color, alpha=0.1)
    for i in range(len(data) - 1):
        ax.fill_between(angles[i:i+2], 0, data[i:i+2], color=cmap(i / num_focus_areas), alpha=0.2)

# Plot each mission
radar_chart(ax, mission_pioneering, 'royalblue', 'Mission Pioneering', cmap_pioneering)
radar_chart(ax, mission_frontier, 'darkorange', 'Mission Frontier', cmap_frontier)

# Customizing radar chart appearance
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(focus_areas, ha='center', fontsize=11)

# Set dynamic y-ticks
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=10, color='gray')

# Add grid customization
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', color='lightgray', alpha=0.5)

# Add title and legend
ax.set_title("Space Exploration Priorities in 2035:\nAn Astronaut's Perspective", fontsize=16, fontweight='bold', pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)

# Annotate important points
ax.annotate('Max\nResearch', xy=(angles[0], mission_pioneering[0]), xytext=(angles[0]+0.1, mission_pioneering[0]+1),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='royalblue')
ax.annotate('Max\nDefense', xy=(angles[4], mission_frontier[4]), xytext=(angles[4]-0.2, mission_frontier[4]+1),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='darkorange')

# Improve layout
plt.tight_layout()

# Show plot
plt.show()