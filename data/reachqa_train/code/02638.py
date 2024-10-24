import matplotlib.pyplot as plt
import numpy as np

# Skills essential in the AI industry
skills = ['Machine Learning', 'Data Analysis', 'Deep Learning', 
          'Natural Language Processing', 'Computer Vision', 
          'AI Ethics', 'Software Development']

# Proficiency levels for each skill (scale 1 to 10)
alex_proficiency = [8, 7, 9, 6, 7, 5, 8]

# Number of variables
num_skills = len(skills)

# Compute angle for each skill in the plot (divided equally around a circle)
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

# The radar chart needs to be a closed loop, append the start to the end.
alex_proficiency += alex_proficiency[:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw the outline of the radar chart and fill area
ax.plot(angles, alex_proficiency, color='b', linewidth=2, linestyle='solid', label='Alex')
ax.fill(angles, alex_proficiency, color='b', alpha=0.25)

# Add labels for each skill
plt.xticks(angles[:-1], skills, fontsize=11)

# Add a title to the chart
ax.set_title("Tech Skills Assessment\nAI Industry", size=16, fontweight='bold', pad=30)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Customize the radial ticks
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=9)

# Gridline configuration for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()