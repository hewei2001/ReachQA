import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the labels for the radar chart
attributes = ['Military Strength', 'Economic Stability', 'Cultural Influence', 
              'Technological Innovation', 'Diplomatic Prowess']

# Define the data for each kingdom
eldoria_stats = [60, 65, 85, 70, 80]
dracoria_stats = [85, 80, 60, 65, 70]
lunaria_stats = [70, 60, 75, 85, 85]

# Combine data for ease of iteration
data = [eldoria_stats, dracoria_stats, lunaria_stats]
kingdoms = ['Kingdom of Eldoria', 'Realm of Dracoria', 'Empire of Lunaria']
colors = ['blue', 'green', 'purple']

# Number of variables we're plotting
num_vars = len(attributes)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Make plot circular

def create_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label, marker='o')
    ax.fill(angles, data, color=color, alpha=0.25)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Add each kingdom's data to the radar chart
for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

# Enhance visual elements
ax.set_yticks([20, 40, 60, 80, 100])  # Set y-ticks to provide scale indicators
ax.set_yticklabels([str(i) for i in range(20, 120, 20)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='darkslategray', weight='bold')

# Add radial grid
ax.yaxis.grid(True, color='lightgray', linestyle='--')
ax.xaxis.grid(True, color='lightgray', linestyle='--')

# Title and annotations
plt.title('Attributes of Medieval Kingdoms\nA Comparative Analysis', size=14, weight='bold', pad=20)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=10, frameon=True)

# Additional decorations
for label, angle in zip(ax.get_xticklabels(), angles):
    label.set_horizontalalignment('center')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()