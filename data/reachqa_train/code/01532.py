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

spaceship_classes = [scout, battleship, cargo, explorer, fuelsaver]
class_names = ['Scout Class', 'Battleship Class', 'Cargo Class', 'Explorer Class', 'FuelSaver Class']

# Function to generate the radar chart
def radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.2)
    ax.set_yticklabels([])
    ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
    ax.set_xticklabels(attributes, fontsize=10, weight='bold')
    for label, angle in zip(attributes, angles):
        ax.text(angle, 10.5, label, ha='center', va='center', size=10, weight='bold')

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = plt.cm.tab20(np.linspace(0, 1, len(spaceship_classes)))

for idx, (data, class_name) in enumerate(zip(spaceship_classes, class_names)):
    radar_chart(ax, data, colors[idx], class_name)

# Add central reference point
ax.scatter(0, 0, color='black', s=20, zorder=5)

# Enhance grid lines
ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)

# Set and adjust legend
ax.legend(class_names, loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='small')

# Title and layout
plt.title('Spaceship Class Performance Comparison\nAcross Key Attributes\nin the United Interstellar Fleet',
          size=14, color='navy', weight='bold', y=1.1)

plt.tight_layout()
plt.show()