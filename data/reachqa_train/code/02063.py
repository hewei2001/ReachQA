import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Communication', 'Task Completion', 'Work-Life Balance', 'Creativity', 'Technology Usage']
num_vars = len(categories)

# Define the data for each role in remote work efficiency
software_engineer = [7, 9, 8, 6, 9]
project_manager = [9, 8, 7, 6, 7]
ux_designer = [8, 7, 9, 9, 7]

# Aggregate data for each role
roles_data = [software_engineer, project_manager, ux_designer]
labels = ['Software Engineer', 'Project Manager', 'UX Designer']

# Compute the angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Repeat the first value to close the radar chart
angles += angles[:1]

# Setup the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Define colors for each role
colors = ['#1F77B4', '#FF7F0E', '#2CA02C']

# Plot and fill each role's data
for i, role_data in enumerate(roles_data):
    data = role_data + role_data[:1]  # to close the radar chart
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=labels[i], color=colors[i])
    ax.fill(angles, data, alpha=0.25, color=colors[i])

# Customize the labels for each slice of the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, wrap=True) # Adjust fontsize if necessary

# Add a legend with a slight offset to avoid crowding
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=10, title='Roles')

# Title of the plot with a line break for readability
plt.title('Remote Work Efficiency Across Tech Roles\nEvaluating Key Productivity Elements', fontsize=14, fontweight='bold', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()