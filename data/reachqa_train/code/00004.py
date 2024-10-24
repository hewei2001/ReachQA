import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define skill categories
categories = ['Plant\nIdentification', 'Soil\nPreparation', 'Pest\nControl',
              'Watering\nEfficiency', 'Plant\nArrangement', 'Harvest\nYield']
N = len(categories)

# Scores for "Green Thumb" gardener
values = [8, 7, 6, 9, 5, 8]
values += values[:1]  # Loop closure

# Calculate angles for each category
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Loop closure for angles

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Customize grid and spokes
ax.yaxis.grid(True, color='lightgrey', linestyle='dashed')
ax.xaxis.grid(True, color='darkgreen', linestyle='solid', linewidth=0.7)
ax.spines['polar'].set_visible(False)  # Remove the outermost frame

# Draw one axe per variable with labels
plt.xticks(angles[:-1], categories, color='darkgreen', size=10, rotation=45)

# Define y-axis ticks with enhanced labels
ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot the data with enhanced styling
ax.plot(angles, values, linewidth=2.5, linestyle='-', color='darkgreen', marker='o', markersize=8, label="Green Thumb")
ax.fill(angles, values, 'forestgreen', alpha=0.25)

# Title and Legend with improved formatting
plt.title('Green Thumb\'s\nGardening Skills Radar', size=18, color='forestgreen', loc='center', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize='large', title="Gardener", title_fontsize='large')

# Adjust layout for readability
plt.tight_layout()

# Display the radar chart
plt.show()