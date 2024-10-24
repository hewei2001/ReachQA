import matplotlib.pyplot as plt
import numpy as np

# Skill categories
skill_categories = ['Programming', 'Data Analysis', 'System Design', 'User Experience', 'Communication']

# Skill emphasis by role (values between 1 and 10)
roles_skills = {
    'Data Scientist': [8, 9, 5, 4, 6],
    'Software Developer': [9, 6, 8, 5, 4],
    'Product Manager': [5, 4, 7, 8, 9],
    'System Administrator': [6, 4, 9, 3, 5],
    'UX Designer': [4, 5, 6, 10, 7],
}

# Number of variables we're plotting
num_vars = len(skill_categories)

# Compute angle for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Append the start point to the end to complete the loop
skill_categories += skill_categories[:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each role
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each role's skills
for idx, (role, skills) in enumerate(roles_skills.items()):
    skills += skills[:1]  # Complete the loop
    ax.fill(angles, skills, color=colors[idx], alpha=0.25, label=role)
    ax.plot(angles, skills, color=colors[idx], linewidth=2, linestyle='solid')

# Add labels for each category
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skill_categories[:-1], fontsize=12)

# Title and legend
ax.set_title('Skill Emphasis in\nTechnology Industry Roles', size=15, weight='bold', position=(0.5, 1.1))
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title='Roles', fontsize=10)

# Enhance grid visibility
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Automatically adjust layout to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()