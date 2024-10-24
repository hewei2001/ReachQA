import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

criteria_names = ['Biodiversity', 'Carbon Storage', 'Clean Waters', 'Sustainable Fishing', 'Coastal Livelihoods']

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create violin plot
sns.violinplot(data=data, ax=ax, inner=None, color=".8")

# Overlay box plot
box = ax.boxplot(data, patch_artist=True, notch=True, positions=range(len(data)), widths=0.2, zorder=2)

# Overlay jittered scatter plot for individual data points
for i, score in enumerate(data):
    y = score
    x = np.random.normal(i, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.6, color='k', zorder=3)

# Customize box colors
colors = sns.color_palette("Set2", len(data))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add mean value markers
means = [np.mean(scores) for scores in data]
ax.scatter(range(len(data)), means, color='r', s=100, zorder=4, marker='D', label='Mean')

# Customize the plot
ax.set_title('Ocean Health Index Across Marine Regions\nComparing Multiple Criteria', fontsize=16, weight='bold')
ax.set_xlabel('Criteria', fontsize=14)
ax.set_ylabel('OHI Score', fontsize=14)
ax.set_xticks(range(len(data)))
ax.set_xticklabels(criteria_names, rotation=30, ha='right')

# Add a grid for easier readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add legend
handles = [
    plt.Line2D([0], [0], color=color, lw=4, label=name) 
    for color, name in zip(colors, criteria_names)
] + [plt.Line2D([0], [0], marker='D', color='w', label='Mean', markerfacecolor='r', markersize=10)]
ax.legend(handles=handles, loc='upper left', title='Criteria')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()