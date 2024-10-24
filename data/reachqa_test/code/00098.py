import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the five key areas
categories = ['Time\nManagement', 'Study\nTechniques', 'Physical\nWell-being', 
              'Social\nInteraction', 'Mental\nHealth']

# Average scores based on survey results
scores = [6.8, 7.2, 5.5, 7.0, 6.3]
scores += scores[:1]

# Comparison data set
comparison_scores = [7.5, 6.5, 6.0, 6.8, 7.2]
comparison_scores += comparison_scores[:1]

num_vars = len(categories)

# Calculate angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plotting the original scores
ax.fill(angles, scores, color='skyblue', alpha=0.5, linewidth=2, linestyle='solid')
ax.plot(angles, scores, color='blue', linewidth=2, linestyle='solid', label='Student Averages')

# Plotting the comparison scores
ax.fill(angles, comparison_scores, color='salmon', alpha=0.5, linewidth=2, linestyle='dotted')
ax.plot(angles, comparison_scores, color='red', linewidth=2, linestyle='dotted', label='Target Scores')

# Add labels for each spoke
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='navy')

# Add data labels
for i in range(num_vars):
    ax.text(angles[i], scores[i] + 0.5, f"{scores[i]:.1f}", horizontalalignment='center', size=10, color='blue')
    ax.text(angles[i], comparison_scores[i] + 0.5, f"{comparison_scores[i]:.1f}", horizontalalignment='center', size=10, color='red')

# Customize the grid
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.yaxis.grid(True, color='gray', linestyle=':', linewidth=0.5)
ax.set_rgrids([2, 4, 6, 8, 10], angle=0)

# Hide the radial labels
ax.set_yticklabels([])

# Set radial limits
ax.set_ylim(0, 10)

# Set title with multiline for clarity
ax.set_title("Student Life Balance:\nComparison of Average and Target Scores\nAcross Five Key Areas", fontsize=14, fontweight='bold', pad=20, color='darkblue')

# Add legend
legend_elements = [Patch(facecolor='skyblue', edgecolor='blue', label='Student Averages', alpha=0.5),
                   Patch(facecolor='salmon', edgecolor='red', label='Target Scores', alpha=0.5)]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()