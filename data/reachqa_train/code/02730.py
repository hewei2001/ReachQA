import matplotlib.pyplot as plt
import numpy as np

# Define the criteria for culinary skills
criteria = ['Creativity', 'Presentation', 'Taste', 'Technique', 'Consistency']
num_criteria = len(criteria)

# Scores for each chef
chef_scores = {
    'Chef Aria': [8, 9, 9, 7, 8],
    'Chef Bastian': [7, 8, 10, 6, 9],
    'Chef Carmen': [9, 7, 8, 8, 7],
    'Chef Dante': [6, 8, 7, 9, 9],
    'Chef Elara': [8, 9, 7, 8, 10]
}

# Number of chefs
num_chefs = len(chef_scores)

# Setup the radar chart framework
angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Define a dynamic color palette using a colormap
colors = plt.cm.viridis(np.linspace(0, 1, num_chefs))

# Plot each chef's data with enhancements
for idx, (chef_name, scores) in enumerate(chef_scores.items()):
    scores += scores[:1]  # Repeat the first score to close the loop
    ax.plot(angles, scores, color=colors[idx], linewidth=2, linestyle='-', label=chef_name)
    ax.fill(angles, scores, color=colors[idx], alpha=0.25)

    # Annotate highest score for each chef
    max_score_idx = np.argmax(scores[:-1])
    ax.text(angles[max_score_idx], scores[max_score_idx] + 0.5, f'{scores[max_score_idx]}', 
            horizontalalignment='center', color=colors[idx], fontsize=10)

# Add criteria labels to the chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, fontweight='bold')

# Set the range of each axis
ax.set_ylim(0, 10)

# Style the gridlines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Customization of y-tick labels
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=9, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=0.3'))

# Add a title with multiple lines for better layout
plt.title("The Artistry of Cuisine:\nComparing Culinary Skills\nAcross Five Renowned Chefs", size=16, color='darkblue', y=1.15)

# Adjust legend location and aesthetics
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10, frameon=True, fancybox=True)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the radar chart
plt.show()