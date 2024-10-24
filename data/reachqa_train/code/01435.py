import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define synthetic popularity data for each cuisine in four regions
popularity_scores = {
    'North America': {
        'Italian': [70, 75, 80, 82, 76, 78, 74, 77, 79, 75],
        'Mexican': [80, 85, 88, 90, 86, 82, 84, 83, 85, 87],
        'Chinese': [60, 62, 64, 59, 61, 63, 65, 67, 66, 64],
        'Indian': [55, 58, 56, 60, 57, 59, 61, 60, 58, 57],
        'Mediterranean': [68, 70, 72, 71, 73, 69, 67, 68, 70, 72]
    },
    'Europe': {
        'Italian': [85, 88, 90, 87, 89, 92, 91, 86, 85, 90],
        'Mexican': [55, 57, 54, 56, 58, 59, 60, 58, 55, 57],
        'Chinese': [60, 62, 63, 61, 64, 66, 65, 67, 62, 64],
        'Indian': [70, 72, 75, 71, 74, 76, 73, 72, 74, 73],
        'Mediterranean': [78, 80, 82, 81, 79, 78, 81, 82, 80, 79]
    },
    'Asia': {
        'Italian': [65, 67, 64, 66, 68, 70, 69, 65, 67, 66],
        'Mexican': [50, 52, 55, 54, 53, 51, 50, 52, 53, 54],
        'Chinese': [90, 92, 94, 93, 91, 95, 93, 94, 92, 91],
        'Indian': [82, 84, 85, 83, 86, 87, 88, 84, 85, 83],
        'Mediterranean': [68, 67, 70, 69, 71, 68, 69, 72, 73, 70]
    },
    'South America': {
        'Italian': [72, 74, 76, 73, 75, 74, 76, 75, 72, 74],
        'Mexican': [77, 80, 82, 83, 81, 79, 78, 82, 81, 80],
        'Chinese': [55, 56, 54, 58, 60, 57, 56, 59, 58, 57],
        'Indian': [50, 52, 51, 53, 55, 54, 52, 50, 51, 53],
        'Mediterranean': [63, 65, 64, 67, 66, 68, 65, 66, 64, 63]
    }
}

# Set up figure and axis
fig, ax = plt.subplots(figsize=(16, 10))

# Define positions for the box plots
positions = np.arange(len(popularity_scores['North America'])) * 10

# Plot box plots for each region and cuisine
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
patterns = ['/', '\\', '|', '-']
for i, (region, scores) in enumerate(popularity_scores.items()):
    data = [scores[cuisine] for cuisine in scores]
    bplot = ax.boxplot(
        data, 
        vert=False, 
        positions=positions - i * 2.5, 
        widths=1.8, 
        patch_artist=True, 
        boxprops=dict(color=colors[i], hatch=patterns[i]),
        whiskerprops=dict(color=colors[i]),
        capprops=dict(color=colors[i]),
        medianprops=dict(color='black'),
        flierprops=dict(marker='o', color=colors[i], markersize=5, alpha=0.6)
    )
    # Fill the boxes with colors
    for patch, color in zip(bplot['boxes'], [colors[i]] * len(data)):
        patch.set_facecolor(color)

# Define cuisine labels
cuisine_labels = list(next(iter(popularity_scores.values())).keys())

# Set labels and title
ax.set_yticks(positions - 3.5)
ax.set_yticklabels(cuisine_labels)
ax.set_xlabel('Popularity Score')
ax.set_title('Culinary Preferences Evolution (2013-2023)\nPopularity of Cuisines by Region', fontsize=16)

# Add a legend
handles = [mpatches.Patch(facecolor=color, edgecolor='k', label=region, hatch=pattern) 
           for color, pattern, region in zip(colors, patterns, popularity_scores.keys())]
ax.legend(handles=handles, title='Regions', loc='upper right')

# Annotate mean values
for i, (region, scores) in enumerate(popularity_scores.items()):
    means = [np.mean(scores[cuisine]) for cuisine in scores]
    for mean, position in zip(means, positions - i * 2.5):
        ax.text(mean, position, f'{mean:.1f}', va='center', ha='left', fontsize=9, color=colors[i])

# Ensure layout fits well
plt.tight_layout()

# Show the plot
plt.show()