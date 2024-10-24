import matplotlib.pyplot as plt
import numpy as np

# Define the technologies and criteria
technologies = [
    "Advanced Propulsion",
    "Sustainable Life Support",
    "Autonomous Spacecraft",
    "Energy Harvesting",
    "Interstellar Communication"
]

criteria = ['Feasibility', 'Energy Efficiency', 'Scalability', 'Cost', 'Innovation']

# Scores for each technology (out of 10 for each criterion)
technology_scores = {
    "Advanced Propulsion": [7, 8, 6, 5, 9],
    "Sustainable Life Support": [8, 9, 7, 6, 8],
    "Autonomous Spacecraft": [9, 7, 8, 6, 7],
    "Energy Harvesting": [6, 8, 5, 7, 8],
    "Interstellar Communication": [8, 6, 9, 7, 9]
}

# Prepare data for radar chart
labels = np.array(criteria)
num_vars = len(labels)

# Create a function to draw radar charts
def radar_chart(ax, data, color='blue', title=None):
    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # The plot is made in a circular (not polygon) space, so we need to "complete the loop"
    data += data[:1]
    angles += angles[:1]

    # Draw the outline of the radar chart
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

    # Labels and title
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    if title:
        ax.set_title(title, color=color, size=12, position=(0.5, 1.1))

# Initialize the plot with radar subplots for each technology
fig, axs = plt.subplots(1, len(technologies), figsize=(18, 8), subplot_kw=dict(polar=True))
fig.suptitle("The Spectrum of Stellar Technologies:\nA Futuristic Radar", fontsize=16, fontweight='bold')

# Colors for each radar chart
colors = ['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#FFD700']

# Plot each technology radar chart
for i, (tech, scores) in enumerate(technology_scores.items()):
    radar_chart(axs[i], scores, color=colors[i], title=tech)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()