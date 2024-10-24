import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define expanded categories with new art forms
categories = ['Painting', 'Sculpture', 'Architecture', 'Literature', 'Music', 'Photography', 'Cinema', 'Dance', 'Digital Art']

# Skill levels for two groups: Renaissance Artists and Modern Artists
renaissance_skills = [8, 7, 9, 5, 6, 4, 3, 7, 5]
modern_skills = [7, 6, 8, 6, 8, 9, 7, 8, 9]

# Number of variables
num_vars = len(categories)

# Create angles for radar chart
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Extend skill levels to close the radar chart area
renaissance_skills += renaissance_skills[:1]
modern_skills += modern_skills[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Add labels for each category
plt.xticks(angles[:-1], categories, color='darkblue', size=10)

# Draw y-labels with a logarithmic effect
ax.set_rlabel_position(30)
plt.yticks([1, 2, 4, 8, 10], ["1", "2", "4", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot data for Renaissance Artists
ax.plot(angles, renaissance_skills, linewidth=2, linestyle='solid', label='Renaissance Artists', color='royalblue')
ax.fill(angles, renaissance_skills, color='royalblue', alpha=0.25)

# Plot data for Modern Artists
ax.plot(angles, modern_skills, linewidth=2, linestyle='dashed', label='Modern Artists', color='firebrick')
ax.fill(angles, modern_skills, color='firebrick', alpha=0.25)

# Title with line breaks
plt.title('Artistic Mastery Across Historical Periods:\nRenaissance vs Modern', size=16, color='darkblue', y=1.1)

# Customizing the legend
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.3, 0.1))

# Adding statistical insights with annotations
max_skill = max(max(renaissance_skills), max(modern_skills))
max_category = categories[renaissance_skills.index(max_skill) % num_vars]

# Annotate highest skill level
ax.annotate(f'Max Skill: {max_skill} in {max_category}', xy=(angles[renaissance_skills.index(max_skill)], max_skill), 
            xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'), fontsize=9, color='black')

# Adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()