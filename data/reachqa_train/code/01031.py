import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define the expanded list of competencies
competencies = [
    "Env. Awareness", "Tech. Design", "Proj. Mgmt", "Community Engagement",
    "Policy Understanding", "Innovation Capacity", "Data Analysis",
    "Communication Skills", "Regulatory Compliance", "Sustainability Ethics"
]

# Number of variables
num_vars = len(competencies)

# Define the proficiency data for each role
urban_planner = [9, 7, 8, 9, 8, 7, 8, 9, 7, 9]
environmental_scientist = [10, 5, 6, 7, 9, 6, 9, 8, 5, 10]
civil_engineer = [6, 9, 7, 6, 7, 8, 7, 6, 9, 8]
architect = [8, 8, 7, 6, 6, 9, 8, 7, 6, 9]

# Gather roles and their data
roles = ['Urban Planner', 'Environmental Scientist', 'Civil Engineer', 'Architect']
data = [urban_planner, environmental_scientist, civil_engineer, architect]

# Compute the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the radar chart loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define colors for each role
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot data for each role
for idx, (role, color) in enumerate(zip(roles, colors)):
    values = data[idx] + data[idx][:1]  # Closing the data loop
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid', label=role, marker='o')
    ax.fill(angles, values, color=color, alpha=0.25)

# Set labels for each competency and handle long text by rotating them
ax.set_xticks(angles[:-1])
ax.set_xticklabels(competencies, fontsize=9, color='dimgray', ha='right', rotation=45)

# Remove y-tick labels for clarity and aesthetics
ax.set_yticklabels([])

# Add a legend with custom patches
legend_elements = [Patch(facecolor=color, edgecolor=color, label=role, alpha=0.25) for role, color in zip(roles, colors)]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=9)

# Add title and adjust layout
plt.title('Skill Set Distribution in Sustainable Urban Development Roles', size=14, color='darkgreen', pad=20, loc='left', wrap=True)
plt.tight_layout(pad=3.0)

# Show the radar chart
plt.show()