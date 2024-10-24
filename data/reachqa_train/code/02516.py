import matplotlib.pyplot as plt
import numpy as np

# Define the skill categories
categories = [
    'Machine Learning', 
    'Data Visualization', 
    'Communication', 
    'Programming', 
    'Domain Knowledge', 
    'Statistical Analysis'
]

# Define proficiency data for each industry
proficiency_healthcare = [7, 6, 8, 5, 9, 7]
proficiency_finance = [8, 7, 7, 8, 6, 9]
proficiency_technology = [9, 8, 6, 9, 7, 8]

# Additional projected data for 2030
proficiency_projection_2030 = {
    'Healthcare': [8, 7, 9, 6, 9, 8],
    'Finance': [9, 8, 8, 9, 7, 9],
    'Technology': [9, 9, 7, 9, 8, 9]
}

# Number of variables
num_vars = len(categories)

# Compute angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proficiency_healthcare += proficiency_healthcare[:1]
proficiency_finance += proficiency_finance[:1]
proficiency_technology += proficiency_technology[:1]
angles += angles[:1]

# Initialize the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=True))
fig.subplots_adjust(wspace=0.5)

# Radar chart
ax = axs[0]
ax.set_title('Skills Proficiency Radar Chart\nfor Data Scientists in 2025', fontsize=14, fontweight='bold', pad=20)
ax.plot(angles, proficiency_healthcare, linewidth=2, linestyle='solid', label='Healthcare', color='#1f77b4')
ax.fill(angles, proficiency_healthcare, alpha=0.25, color='#1f77b4')
ax.plot(angles, proficiency_finance, linewidth=2, linestyle='solid', label='Finance', color='#ff7f0e')
ax.fill(angles, proficiency_finance, alpha=0.25, color='#ff7f0e')
ax.plot(angles, proficiency_technology, linewidth=2, linestyle='solid', label='Technology', color='#2ca02c')
ax.fill(angles, proficiency_technology, alpha=0.25, color='#2ca02c')
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='navy')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, title='Industry')

# Bar chart for projected 2030 data
ax2 = axs[1]
width = 0.2  # Bar width
labels = categories
x = np.arange(len(labels))

# Bar positions and heights
bar_healthcare = ax2.bar(x - width, proficiency_projection_2030['Healthcare'], width, label='Healthcare', color='#1f77b4')
bar_finance = ax2.bar(x, proficiency_projection_2030['Finance'], width, label='Finance', color='#ff7f0e')
bar_technology = ax2.bar(x + width, proficiency_projection_2030['Technology'], width, label='Technology', color='#2ca02c')

# Chart details
ax2.set_title('Projected Proficiency in 2030', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, rotation=45, ha='right')
ax2.set_ylabel('Proficiency Level')
ax2.legend(title='Industry')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()