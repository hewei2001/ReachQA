import matplotlib.pyplot as plt
import numpy as np

# Define the skill categories
categories = ['Machine Learning', 'Data Visualization', 'Communication', 'Programming', 'Domain Knowledge', 'Statistical Analysis']

# Define the proficiency data for each industry
proficiency_healthcare = [7, 6, 8, 5, 9, 7]
proficiency_finance = [8, 7, 7, 8, 6, 9]
proficiency_technology = [9, 8, 6, 9, 7, 8]

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the circle by appending the start value to the end
proficiency_healthcare += proficiency_healthcare[:1]
proficiency_finance += proficiency_finance[:1]
proficiency_technology += proficiency_technology[:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot for healthcare
ax.plot(angles, proficiency_healthcare, linewidth=2, linestyle='solid', label='Healthcare', color='#1f77b4')
ax.fill(angles, proficiency_healthcare, alpha=0.25, color='#1f77b4')

# Plot for finance
ax.plot(angles, proficiency_finance, linewidth=2, linestyle='solid', label='Finance', color='#ff7f0e')
ax.fill(angles, proficiency_finance, alpha=0.25, color='#ff7f0e')

# Plot for technology
ax.plot(angles, proficiency_technology, linewidth=2, linestyle='solid', label='Technology', color='#2ca02c')
ax.fill(angles, proficiency_technology, alpha=0.25, color='#2ca02c')

# Add labels for each skill category
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='navy')

# Add title and legend
plt.title('Skills Proficiency Radar Chart\nfor Data Scientists in 2025', fontsize=16, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Industry')

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()