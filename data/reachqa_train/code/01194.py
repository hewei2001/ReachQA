import matplotlib.pyplot as plt
import numpy as np

# Define superpowers and their levels for each hero
labels = np.array(['Super Strength', 'Flight', 'Invisibility', 'Intelligence', 'Elemental Control'])
heroes = ['Titan Man', 'Night Shadow', 'Wind Whisperer']
superpowers = {
    'Titan Man': [9, 8, 3, 7, 6],
    'Night Shadow': [4, 1, 9, 10, 2],
    'Wind Whisperer': [6, 9, 4, 5, 10]
}

# Number of superpowers
num_vars = len(labels)

# Function to create a radar chart
def create_radar_chart(ax, data, color, marker, linestyle, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]  
    angles += angles[:1]

    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, label=label, marker=marker, markersize=6)
    ax.fill(angles, data, color=color, alpha=0.15)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Colors for each hero and marker styles
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
markers = ['o', 's', '^']
linestyles = ['solid', 'dashed', 'dotted']

# Create a radar chart for each hero
for i, hero in enumerate(heroes):
    create_radar_chart(ax, superpowers[hero], colors[i], markers[i], linestyles[i], hero)

# Add labels and adjust tick positions
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(labels, fontsize=12, color='black', rotation=45, ha='right')

# Add concentric circles with labels
ax.set_yticks(range(1, 11, 2))
ax.set_yticklabels(range(1, 11, 2), fontsize=10, color='gray')
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Add a chart title
plt.title('Comparison of Superpowers\nAcross Iconic Comic Book Heroes', size=16, color='darkred', pad=40, loc='center')

# Add legend outside the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title="Heroes", title_fontsize=12, shadow=True)

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()