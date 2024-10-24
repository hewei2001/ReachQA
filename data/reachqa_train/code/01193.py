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
def create_radar_chart(ax, data, color, label):
    # Calculate angles for each variable
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]  # Close the plot by repeating the first value
    angles += angles[:1]

    # Plot data and fill area
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Colors for each hero
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a radar chart for each hero
for i, hero in enumerate(heroes):
    create_radar_chart(ax, superpowers[hero], colors[i], hero)

# Add labels and adjust tick positions
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(labels, fontsize=11, color='black')

# Remove radial labels to declutter the chart
ax.set_yticklabels([])

# Add a chart title
plt.title('Comparison of Superpowers\nAcross Iconic Comic Book Heroes', size=16, color='darkred', pad=30)

# Add legend to differentiate heroes
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10, title="Heroes", title_fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()