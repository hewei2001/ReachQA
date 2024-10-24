import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Skills and role data
skills = ['Programming', 'Data Analysis', 'Machine Learning', 'Communication', 'Design', 'Problem-Solving']
data_scientist = [9, 10, 8, 7, 5, 7]
software_engineer = [8, 6, 7, 8, 4, 9]
ux_designer = [5, 4, 3, 9, 10, 8]

# Number of skills
num_skills = len(skills)

# Compute the angle for each skill
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

# Complete the loop by appending the first value to the end
data_scientist += data_scientist[:1]
software_engineer += software_engineer[:1]
ux_designer += ux_designer[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Add circles to enhance the visual complexity
ax.add_patch(Circle((0, 0), 10, transform=ax.transData._b, color='grey', alpha=0.05))

# Plot data with styles and gradient fills
ax.plot(angles, data_scientist, color='navy', linewidth=2, linestyle='solid', marker='o', markersize=6, label='Data Scientist')
ax.fill(angles, data_scientist, color='blue', alpha=0.2)

ax.plot(angles, software_engineer, color='forestgreen', linewidth=2, linestyle='dashed', marker='s', markersize=6, label='Software Engineer')
ax.fill(angles, software_engineer, color='green', alpha=0.2)

ax.plot(angles, ux_designer, color='darkred', linewidth=2, linestyle='dashdot', marker='^', markersize=6, label='UX Designer')
ax.fill(angles, ux_designer, color='red', alpha=0.2)

# Calculate average skill levels and add them to the chart
avg_skills = [(a + b + c) / 3 for a, b, c in zip(data_scientist[:-1], software_engineer[:-1], ux_designer[:-1])]
avg_skills += avg_skills[:1]
ax.plot(angles, avg_skills, color='black', linewidth=1, linestyle='dotted', marker='x', markersize=6, label='Average Skill Level')

# Add skill labels with adjustable font size
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=10)

# Configure y-axis properties
ax.set_yticks(range(1, 11))
ax.set_yticklabels(map(str, range(1, 11)), color='gray', fontsize=9)

# Add a title
plt.title('Tech Industry Skills Analysis\nComparing Key Skills Across Roles', size=16, color='navy', pad=20)

# Add legend in a position that doesn’t obscure other elements
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()