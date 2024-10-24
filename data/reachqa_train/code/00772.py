import matplotlib.pyplot as plt
import numpy as np

# Define regions and their respective scores for different criteria
regions = ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean']

# Scores for each criterion across the regions
scores_biodiversity = [85, 75, 70, 65]
scores_carbon_storage = [80, 72, 68, 60]
scores_clean_waters = [78, 74, 72, 67]
scores_sustainable_fishing = [82, 70, 75, 55]
scores_coastal_livelihoods = [88, 83, 77, 65]

# Combine all scores into a single list
data = [scores_biodiversity, scores_carbon_storage, scores_clean_waters, 
        scores_sustainable_fishing, scores_coastal_livelihoods]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a box plot
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, positions=range(1, len(data) + 1))

# Customize colors for each box (one color per criteria)
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot appearance
ax.set_title('Ocean Health Index Across Marine Regions', fontsize=14, weight='bold')
ax.set_xlabel('Criteria', fontsize=12)
ax.set_ylabel('OHI Score', fontsize=12)
ax.set_xticks(range(1, len(data) + 1))
ax.set_xticklabels(['Biodiversity', 'Carbon Storage', 'Clean Waters', 'Sustainable Fishing', 'Coastal Livelihoods'], rotation=30, ha='right')

# Add a grid for easier readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add a legend with color coding for criteria
criteria_legend = [
    plt.Line2D([0], [0], color=colors[0], lw=4, label='Biodiversity'),
    plt.Line2D([0], [0], color=colors[1], lw=4, label='Carbon Storage'),
    plt.Line2D([0], [0], color=colors[2], lw=4, label='Clean Waters'),
    plt.Line2D([0], [0], color=colors[3], lw=4, label='Sustainable Fishing'),
    plt.Line2D([0], [0], color=colors[4], lw=4, label='Coastal Livelihoods')
]
ax.legend(handles=criteria_legend, loc='upper right', title='Criteria')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()