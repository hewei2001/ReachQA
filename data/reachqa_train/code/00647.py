import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch

# Define categories and their contributions
categories = ['Biology', 'Chemistry', 'Physics', 'Geology', 'Social Sciences', 'Engineering']
contributions = [8, 7, 5, 6, 5, 7]
previous_contributions = [5, 6, 4, 5, 6, 6]  # Additional dataset for comparison

# Number of variables we're plotting.
num_vars = len(categories)

# Create a 360-degree angle range and add first point again to close the circle
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
contributions += contributions[:1]
previous_contributions += previous_contributions[:1]
angles += angles[:1]

# Initialize Radar Chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Offset and direction settings
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='darkslategray', size=10)

# Draw ylabels with dynamic scale adjustments
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot data
ax.plot(angles, contributions, linewidth=2, linestyle='solid', label='Current Year Contributions', color='navy', marker='o')
ax.plot(angles, previous_contributions, linewidth=2, linestyle='dashed', label='Previous Year Contributions', color='orange', marker='s')

# Fill area
ax.fill(angles, contributions, 'skyblue', alpha=0.3)
ax.fill(angles, previous_contributions, 'lightsalmon', alpha=0.3)

# Enhance gridlines and axes
ax.grid(color='lightgrey', linestyle='--', linewidth=0.75)

# Add a title
plt.title("Comparative Analysis of Interdisciplinary\nResearch Contributions in Environmental Science", 
          size=14, weight='bold', va='top', color='darkgreen')

# Add shadow for a 3D effect
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('gray')

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15), fontsize=10)

# Automatically adjust plot to ensure no element is clipped
plt.tight_layout()

# Show the plot
plt.show()