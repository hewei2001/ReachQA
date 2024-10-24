import numpy as np
import matplotlib.pyplot as plt

# Define the parameters and their respective scores for each planetary system
categories = ['Atmosphere\nComposition', 'Water\nAvailability', 'Temperature\nStability', 'Gravity', 'Energy\nSources']
num_vars = len(categories)

# Data scores for the systems
planetary_system_data = {
    'Kepler-186': [7, 8, 6, 5, 9],
    'TRAPPIST-1': [8, 9, 8, 4, 7],
    'Proxima Centauri': [6, 7, 5, 8, 6],
    'Gliese 581': [5, 6, 7, 7, 5],
    'Tau Ceti': [9, 5, 9, 6, 8]
}

# Create a figure for the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Calculate the angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the last angle

# Draw the radar chart with filled areas
for system, scores in planetary_system_data.items():
    scores += scores[:1]  # Repeat the first value to close the radar chart loop
    ax.fill(angles, scores, alpha=0.25, label=system)
    ax.plot(angles, scores, linewidth=2)

# Customize the chart's appearance
plt.xticks(angles[:-1], categories, color='navy', size=10)
ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="navy", size=7)

# Title and legend settings
plt.title('Performance Radar of the\nPlanetary Systems Exploration 2025', size=16, color='darkgreen', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, title='Planetary Systems')

# Ensure everything is adjusted neatly
plt.tight_layout()

# Display the radar chart
plt.show()