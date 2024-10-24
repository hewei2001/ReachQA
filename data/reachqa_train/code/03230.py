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

# Scores for each technology
technology_scores = {
    "Advanced Propulsion": [7, 8, 6, 5, 9],
    "Sustainable Life Support": [8, 9, 7, 6, 8],
    "Autonomous Spacecraft": [9, 7, 8, 6, 7],
    "Energy Harvesting": [6, 8, 5, 7, 8],
    "Interstellar Communication": [8, 6, 9, 7, 9]
}

# Industry standard scores for overlay
industry_standards = [7, 7, 7, 7, 7]

# Prepare data for radar chart
labels = np.array(criteria)
num_vars = len(labels)

# Function to draw radar charts with overlay
def radar_chart_with_overlay(ax, data, overlay, colors, title=None):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    data += data[:1]
    overlay += overlay[:1]
    angles += angles[:1]

    ax.plot(angles, data, color=colors['data'], linewidth=2, linestyle='solid', label='Technology Score')
    ax.fill(angles, data, color=colors['data'], alpha=0.25)

    ax.plot(angles, overlay, color=colors['overlay'], linewidth=2, linestyle='dashdot', label='Industry Standard')
    
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    if title:
        ax.set_title(title, color=colors['data'], size=12, position=(0.5, 1.1))

    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Initialize the plot
fig, axs = plt.subplots(1, len(technologies), figsize=(18, 8), subplot_kw=dict(polar=True))
fig.suptitle("The Spectrum of Stellar Technologies:\nRadar Comparison Against Industry Standards", fontsize=16, fontweight='bold')

# Colors for radar charts and overlay
colors_list = [
    {'data': '#FF6347', 'overlay': '#A9A9A9'},
    {'data': '#4682B4', 'overlay': '#A9A9A9'},
    {'data': '#32CD32', 'overlay': '#A9A9A9'},
    {'data': '#8A2BE2', 'overlay': '#A9A9A9'},
    {'data': '#FFD700', 'overlay': '#A9A9A9'}
]

# Plot each technology radar chart with overlay
for i, (tech, scores) in enumerate(technology_scores.items()):
    radar_chart_with_overlay(axs[i], scores.copy(), industry_standards.copy(), colors_list[i], title=tech)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()