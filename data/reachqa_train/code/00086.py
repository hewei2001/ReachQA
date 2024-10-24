import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories and data for each district
categories = ['Public Transport', 'Green Spaces', 'Air Quality', 
              'Renewable Energy Use', 'Waste Management', 
              'Water Resource Management']
num_vars = len(categories)

# Scores for each district
district_scores = {
    'Downtown': [0.8, 0.6, 0.4, 0.5, 0.7, 0.6],
    'Riverdale': [0.7, 0.8, 0.6, 0.6, 0.8, 0.7],
    'Greenway': [0.6, 0.9, 0.8, 0.7, 0.9, 0.8],
    'Tech Park': [0.9, 0.7, 0.5, 0.9, 0.6, 0.7],
    'Westend': [0.5, 0.6, 0.7, 0.8, 0.5, 0.9],
}

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Create angles for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Plot each district's data
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, (district, scores) in enumerate(district_scores.items()):
    scores += scores[:1]  # Close the circle
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=district, color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

# Add labels and title
plt.xticks(angles[:-1], categories, color='grey', size=10)
ax.set_rlabel_position(30)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=8)
plt.ylim(0, 1)

# Add a legend and title
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.title('Sustainable City Development Indicators\nUrban Districts in Urbanopolis', 
          size=15, color='navy', ha='center')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()