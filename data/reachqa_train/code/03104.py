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

# Number of variables we're plotting.
num_vars = len(attributes)

# Compute angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Make the plot circular by repeating the first angle
angles += angles[:1]

# Function to create a radar plot
def create_radar_chart(ax, data, color, label):
    data += data[:1]  # Ensure the plot is closed
    ax.plot(angles, data, color=color, linewidth=2, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Add each kingdom's data to the radar chart
for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

# Customize labels and title
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])  # Set the positions of the attribute labels
ax.set_xticklabels(attributes, fontsize=10, color='gray')
plt.title('Attributes of Medieval Kingdoms\nComparative Analysis', size=14, weight='bold', pad=20)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()