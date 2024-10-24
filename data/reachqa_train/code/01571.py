import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Categories for comparison
categories = ['Scientific Instruments', 'Mobility', 'Power Generation', 'Communication', 'Weight']
N = len(categories)

# Data for each rover
curiosity_values = [10, 7, 9, 8, 5]  # Adjusted Weight to a 1-10 scale for consistency
perseverance_values = [14, 8, 10, 9, 6]

# Complete the circle for the radar chart
curiosity_values += curiosity_values[:1]
perseverance_values += perseverance_values[:1]

# Calculate angles for each axis
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], categories, color='grey', size=10)

# Draw y-labels for values
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10, 12, 14], ["2", "4", "6", "8", "10", "12", "14"], color="grey", size=8)
plt.ylim(0, 14)

# Plot Curiosity data
ax.plot(angles, curiosity_values, linewidth=1.5, linestyle='solid', label='Curiosity')
ax.fill(angles, curiosity_values, 'b', alpha=0.2)

# Plot Perseverance data
ax.plot(angles, perseverance_values, linewidth=1.5, linestyle='solid', label='Perseverance')
ax.fill(angles, perseverance_values, 'r', alpha=0.2)

# Add title and legend
plt.title("Comparative Analysis of Mars Rover Capabilities:\nNASA's Curiosity vs. Perseverance", size=14, color='black', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()