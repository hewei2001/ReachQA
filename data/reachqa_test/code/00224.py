import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Categories and company names
categories = ['AI Integration', 'Cloud Services', 'Cybersecurity', 
              'UX Design', 'Mobile Development', 'Data Analytics']
companies = ['Tech Pioneer', 'InnovateX', 'FutureVision', 'CodeNext']

# Scores for each company on each category (0-10 scale)
scores = np.array([
    [9, 8, 7, 6, 8, 9],  # Tech Pioneer
    [8, 9, 6, 7, 8, 7],  # InnovateX
    [7, 6, 9, 8, 7, 8],  # FutureVision
    [6, 7, 8, 9, 7, 6]   # CodeNext
])

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the radar
scores = np.concatenate((scores, scores[:, [0]]), axis=1)
angles += angles[:1]

# Create plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Set color palette
colors = ['#6a0dad', '#ffa07a', '#20b2aa', '#f08080']

# Plot each company with enhanced styles
for i, company in enumerate(companies):
    ax.fill(angles, scores[i], color=colors[i], alpha=0.3, linewidth=2, linestyle='solid')
    ax.plot(angles, scores[i], label=company, color=colors[i], linewidth=2, linestyle='solid')
    max_score = max(scores[i])
    max_index = np.where(scores[i] == max_score)[0][0]
    ax.annotate(f'{max_score}', xy=(angles[max_index], max_score), textcoords="offset points", 
                xytext=(5, 5), ha='center', color=colors[i], fontsize=10, fontweight='bold')

# Add labels for each axis with enhanced typography
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold', va='bottom')

# Add title with improved readability
ax.set_title("Digital Innovation Spectrum:\nRadar Chart Analysis of Tech Company Competencies",
             size=15, color='darkslategray', pad=40)

# Add a legend with improved placement
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.15), fontsize=10, frameon=False)

# Show radial lines and labels with subtle enhancements
ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='lightgrey')
ax.set_yticklabels([])  # Hide radial labels for cleaner look

# Add a radial annotation
for angle in angles[:-1]:
    ax.annotate("", xy=(angle, 10), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color='lightgrey', lw=0.5))

# Adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()