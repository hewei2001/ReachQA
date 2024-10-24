import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories for the radar chart
categories = ['Knife Skills', 'Baking', 'Plating', 'Creativity', 'Speed']

# Data for three chefs, each with a proficiency score out of 10
chef_data = {
    'Chef A': [8, 6, 7, 8, 9],
    'Chef B': [7, 8, 8, 6, 7],
    'Chef C': [6, 7, 6, 9, 8],
}

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot needs to close the radar chart, so we repeat the first angle
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each chef's data with filled areas
for chef, values in chef_data.items():
    # Repeat the first value to close the circular graph
    values += values[:1]
    ax.fill(angles, values, alpha=0.25, label=chef)
    ax.plot(angles, values, linewidth=2, linestyle='solid')

# Customize the radar chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='black', fontsize=12)

# Add labels to each angle to provide clear visibility
ax.yaxis.set_label_position("left")
ax.yaxis.set_tick_params(labelcolor='grey')
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color='grey', size=10)
plt.ylim(0, 10)

# Title and legend
plt.title('Culinary Skills Competency\nAssessment', size=16, color='darkgreen', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title='Chefs')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()