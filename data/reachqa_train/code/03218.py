import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Define the categories for the radar chart
categories = [
    'Biodiversity', 'Vegetation Density', 'Water Availability', 
    'Air Quality', 'Noise Levels', 'Human Interference'
]

# Number of variables
num_vars = len(categories)

# Values for each urban habitat
city_parks = [8, 8, 6, 6, 3, 5]
rooftop_gardens = [5, 6, 4, 9, 9, 2]
community_gardens = [9, 9, 7, 8, 4, 5]

# Create a 2D array with the data and repeat the first value to close the radar chart
data = np.array([city_parks, rooftop_gardens, community_gardens])
data = np.concatenate((data, data[:, [0]]), axis=1)

# The angles for the categories
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define color scheme and gradients for fill
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
hatch_patterns = ['/', '\\', '|']

# Plot each habitat's data with filled area and markers
for i, (habitat, pattern) in enumerate(zip(['City Parks', 'Rooftop Gardens', 'Community Gardens'], hatch_patterns)):
    ax.fill(angles, data[i], color=colors[i], alpha=0.25, label=habitat, hatch=pattern)
    ax.plot(angles, data[i], color=colors[i], linewidth=2, linestyle='solid')
    ax.scatter(angles, data[i], color=colors[i], s=50, edgecolor='black', zorder=5)

# Add the category labels with enhanced font
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, weight='bold')

# Draw circular grid lines
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.set_ylim(0, 10)

# Remove radial labels for a cleaner look
ax.set_yticklabels([])

# Add dynamic title with line break
ax.set_title(
    'Ecosystem Resilience Indicators:\nComparing Urban Wildlife Habitats',
    size=16, color='darkslategray', weight='bold', position=(0.5, 1.1)
)

# Add a legend with enhanced styling
legend_elements = [
    Patch(facecolor=colors[0], edgecolor='black', alpha=0.25, label='City Parks', hatch=hatch_patterns[0]),
    Patch(facecolor=colors[1], edgecolor='black', alpha=0.25, label='Rooftop Gardens', hatch=hatch_patterns[1]),
    Patch(facecolor=colors[2], edgecolor='black', alpha=0.25, label='Community Gardens', hatch=hatch_patterns[2])
]

plt.legend(
    handles=legend_elements,
    loc='upper right', bbox_to_anchor=(1.3, 1.2), fontsize=10,
    title='Habitats', title_fontsize='13', frameon=True
)

# Enhance the plot with a tight layout
plt.tight_layout()

# Display the radar chart
plt.show()