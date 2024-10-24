import matplotlib.pyplot as plt
import numpy as np

# Musical abilities
abilities = np.array(['Melody', 'Rhythm', 'Harmony', 'Dynamics', 'Timbre'])

# Tribes and their skill levels
tribes = ['Druids of Harmony', 'Rhythmic Nomads', 'Melodic Whisperers', 'Dynamic Artisans', 'Timbre Guardians']
musical_skills = {
    'Druids of Harmony': [6, 7, 9, 5, 6],
    'Rhythmic Nomads': [5, 10, 4, 6, 7],
    'Melodic Whisperers': [9, 6, 7, 5, 5],
    'Dynamic Artisans': [6, 4, 5, 10, 7],
    'Timbre Guardians': [5, 6, 6, 7, 10]
}

# Number of abilities
num_vars = len(abilities)

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
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Colors for each tribe
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create a radar chart for each tribe
for i, tribe in enumerate(tribes):
    create_radar_chart(ax, musical_skills[tribe], colors[i], tribe)

# Add labels and adjust tick positions
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(abilities, fontsize=11, color='black')

# Remove radial labels to declutter the chart
ax.set_yticklabels([])

# Add a chart title
plt.title('Symphony of the Ancients: Musical Skill Balance\nAcross Verdantian Tribes', size=15, color='darkgreen', pad=30)

# Add legend to differentiate tribes
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title="Tribes", title_fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()