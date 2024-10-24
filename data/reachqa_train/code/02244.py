import matplotlib.pyplot as plt
import numpy as np

# Starship attributes and data
starships = {
    'SS Voyager': [8, 6, 7, 5, 9],
    'SS Defiant': [7, 9, 9, 4, 6],
    'SS Enterprise': [9, 7, 8, 6, 7],
    'SS Discovery': [7, 8, 7, 8, 8],
    'SS Atlantis': [6, 6, 8, 9, 5]
}

# Core attributes
attributes = ['Speed', 'Firepower', 'Defense', 'Crew Capacity', 'Range']
num_vars = len(attributes)

def create_radar_chart(ax, data, label, color):
    # Compute angle for each axis and close the loop
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    # Plot and fill the radar chart
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=label, color=color)
    ax.fill(angles, data, color=color, alpha=0.25)

    # Set labels for each axis
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, size=9, fontweight='bold')

# Colors for each starship
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each starship's attributes
for (ship_name, ship_attributes), color in zip(starships.items(), colors):
    create_radar_chart(ax, ship_attributes[:], ship_name, color)

# Add legend and title
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title('Galactic Exploration:\nStarfleet Attributes Radar', size=16, fontweight='bold', pad=20)

# Adjust layout and display
plt.tight_layout()
plt.show()