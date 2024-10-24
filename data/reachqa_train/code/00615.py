import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Skill areas and their corresponding average proficiency levels
skill_areas = ['Programming', 'Electronics', 'Machine Learning', 
               'Human-Robot Interaction', 'Mechanical Design', 'System Integration']
proficiency_levels = [8.5, 7, 9, 8, 7.5, 8.5]

# Number of variables we're plotting
num_vars = len(skill_areas)

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # To close the radar chart loop

# Append the first value to close the radar chart
proficiency_levels += proficiency_levels[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axis per skill and add labels
plt.xticks(angles[:-1], skill_areas, color='darkblue', size=12)

# Draw y-labels and customize their appearance
ax.set_rscale('linear')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=11)
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Plot data and fill the area
ax.plot(angles, proficiency_levels, linewidth=2, linestyle='solid', color='navy', marker='o')
ax.fill(angles, proficiency_levels, color='lightblue', alpha=0.4)

# Add a title with a line break for better readability
plt.title('Skills Proficiency of Robotics Engineers\n(Year 2035)', size=14, color='navy', pad=30)

# Add a legend
plt.legend(['Proficiency Level'], loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=12)

# Automatically adjust layout to fit elements neatly
plt.tight_layout()

# Display the radar chart
plt.show()