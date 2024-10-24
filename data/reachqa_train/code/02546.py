import numpy as np
import matplotlib.pyplot as plt

# Define an increased set of categories for space colonization qualities
categories = [
    'Atmosphere', 'Water Availability', 'Terraforming Feasibility',
    'Natural Resources', 'Biodiversity', 'Safety', 'Climate Stability',
    'Energy Potential', 'Geological Activity', 'Proximity to Earth'
]
n_categories = len(categories)

# Data for fictional planets, expanding number of planets and categories
planets_data = {
    'Planet Azura': [8, 6, 7, 5, 7, 8, 6, 8, 5, 7],
    'Nebula Prime': [6, 8, 5, 9, 6, 7, 7, 5, 6, 8],
    'Terra Nova': [9, 5, 8, 6, 9, 7, 9, 6, 4, 7],
    'Chronos': [7, 4, 6, 8, 5, 9, 6, 5, 7, 6],
    'Vulcan': [5, 9, 4, 7, 4, 8, 6, 9, 5, 8],
    'Zelos': [6, 7, 5, 6, 6, 7, 8, 6, 6, 9]
}

# Weights for each category
weights = [1.2, 1.5, 1.3, 1.0, 1.1, 1.4, 1.6, 1.3, 1.2, 1.1]

# Calculate composite scores
composite_scores = {}
for planet, scores in planets_data.items():
    weighted_score = np.dot(scores, weights)
    composite_scores[planet] = weighted_score / sum(weights)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Create radar chart angles
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]

# Plot each planet's data
colors = plt.cm.viridis(np.linspace(0, 1, len(planets_data)))
for (planet, scores), color in zip(planets_data.items(), colors):
    scores += scores[:1]  # Loop the data to close the radar chart
    ax.plot(angles, scores, linewidth=1.5, linestyle='solid', label=planet, color=color)
    ax.fill(angles, scores, alpha=0.25, color=color)

# Customize the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=8)
ax.set_ylim(0, 10)
ax.set_title("Exploring the Qualities of Fictional Planets for Space Colonization", size=14, fontweight='bold', pad=20)

# Display composite scores in the legend
legend_labels = [f"{planet} (Score: {composite_scores[planet]:.2f})" for planet in planets_data]
ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1.1, 1.05), fontsize='small')

# Improve layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Show the plot
plt.show()