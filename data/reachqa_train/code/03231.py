import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define skills and industries
skills = ['Technical', 'Communication', 'Analytical', 'Creativity', 'Emotional Intelligence']
industries = {
    'Technology': [9, 7, 8, 6, 5],
    'Healthcare': [6, 9, 7, 5, 8],
    'Finance': [7, 8, 9, 4, 6],
    'Education': [5, 8, 6, 7, 9],
    'Arts': [4, 6, 5, 9, 10],
}

# Number of variables
num_skills = len(skills)

# Compute angle for each skill in the radar chart
angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#eaeaf2')

# Plot each industry's data
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for idx, (industry, values) in enumerate(industries.items()):
    values += values[:1]
    ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='solid', label=industry)
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

# Add labels for each skill
plt.xticks(angles[:-1], skills, color='black', size=12, weight='bold')
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color='black', size=10)
ax.set_ylim(0, 10)

# Enhance gridlines and add a title
ax.yaxis.grid(True, linestyle='--', color='grey', linewidth=0.75)
ax.xaxis.grid(True, linestyle='--', color='grey', linewidth=0.75)
plt.title("Key Skills Valued Across Various Industries\nin the Modern Job Market", size=14, fontweight='bold', pad=40)

# Legend configuration
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.05), title="Industries", fontsize='medium', title_fontsize='13')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()