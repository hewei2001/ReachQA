import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the skill categories and scores for each department
categories = ['Data Analysis', 'Programming', 'Communication', 'Design', 'Digital Marketing']
dept_scores = {
    'Software Development': [8, 9, 7, 5, 4],
    'Marketing': [6, 5, 8, 9, 7],
    'Human Resources': [7, 6, 5, 6, 8]
}

# Industry average scores for overlay
industry_averages = [7, 7, 7, 6, 6]

num_vars = len(categories)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Function to plot each department
def add_department_radar(dept_name, color):
    scores = dept_scores[dept_name]
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=dept_name, color=color)
    ax.fill(angles, scores, color=color, alpha=0.25)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for dept, color in zip(dept_scores.keys(), colors):
    add_department_radar(dept, color)

# Add labels for each category
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, weight='bold')

# Set the title of the plot
plt.title('Digital Skills Proficiency Radar:\nA Snapshot of Modern Workforce Capabilities',
          size=15, weight='bold', ha='center', va='top', position=(0.5, 1.1))

# Plot the industry average as a separate line on the existing polar plot
industry_averages += industry_averages[:1]
ax.plot(angles, industry_averages, linewidth=2, linestyle='dashed', color='grey', label='Industry Average')

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), title='Legend')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()