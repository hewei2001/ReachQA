import numpy as np
import matplotlib.pyplot as plt

# Define the performance attributes for the radar chart
attributes = ['Speed', 'Armor', 'Fuel Efficiency', 'Cargo Capacity', 'Maneuverability']
num_vars = len(attributes)

# Performance values for each spaceship class
scout = [9, 3, 5, 4, 10]
battleship = [5, 10, 3, 6, 4]
cargo = [3, 4, 5, 10, 3]
explorer = [7, 7, 6, 7, 7]
fuelsaver = [4, 3, 10, 5, 6]

# Combine performance values into a list for iteration
spaceship_classes = [scout, battleship, cargo, explorer, fuelsaver]
class_names = ['Scout Class', 'Battleship Class', 'Cargo Class', 'Explorer Class', 'FuelSaver Class']

# Function to generate the radar chart
def radar_chart(ax, data, labels, label, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    
    ax.plot(angles, data, label=label, color=color, linewidth=2)
    ax.fill(angles, data, color=color, alpha=0.25)

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Color cycle for distinct spaceship classes
colors = plt.cm.viridis(np.linspace(0, 1, len(spaceship_classes)))

# Plot each spaceship class
for idx, (data, class_name) in enumerate(zip(spaceship_classes, class_names)):
    radar_chart(ax, data, attributes, class_name, colors[idx])

# Set the attribute labels for the axes
ax.set_yticklabels([])
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(attributes, fontsize=10, weight='bold')

# Add title and legend
plt.title('Spaceship Class Performance Comparison\nAcross Key Attributes in the United Interstellar Fleet',
          size=14, color='navy', weight='bold', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()