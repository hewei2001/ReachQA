import matplotlib.pyplot as plt
import numpy as np

# Data for math scores from different districts
northville_scores = [65, 67, 70, 72, 69, 71, 73, 68, 66, 74, 75, 70, 72, 65, 68]
southtown_scores = [80, 82, 85, 79, 81, 83, 78, 85, 84, 79, 77, 86, 88, 85, 82]
eastside_scores = [55, 57, 60, 52, 58, 61, 63, 54, 59, 62, 56, 51, 50, 65, 53]
westburg_scores = [72, 74, 78, 71, 73, 77, 75, 76, 72, 79, 80, 81, 77, 82, 70]
centerville_scores = [90, 92, 89, 95, 91, 94, 93, 87, 88, 96, 97, 90, 92, 85, 94]

# Group all scores into a list for plotting
all_scores = [
    northville_scores,
    southtown_scores,
    eastside_scores,
    westburg_scores,
    centerville_scores
]

# District labels for the box plot
district_labels = ["Northville", "Southtown", "Eastside", "Westburg", "Centerville"]

# Calculate means for each district for the line plot
means = [np.mean(scores) for scores in all_scores]

# Create the figure and axis for two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# 1. Box Plot on the first subplot
box = axes[0].boxplot(all_scores, labels=district_labels, patch_artist=True, notch=True, vert=True)

# Customize the box plots with different colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize other plot elements
axes[0].set_title("8th Grade Math Scores by District", fontsize=12)
axes[0].set_xlabel("School District", fontsize=10)
axes[0].set_ylabel("Math Scores", fontsize=10)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Further customize the box plots
for element in ['whiskers', 'caps', 'medians']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

# 2. Bar Plot for Average Scores on the second subplot
axes[1].bar(district_labels, means, color=colors, alpha=0.7)
axes[1].set_title("Average Math Scores by District", fontsize=12)
axes[1].set_xlabel("School District", fontsize=10)
axes[1].set_ylabel("Average Score", fontsize=10)

# Add value annotations on the bars
for i, mean in enumerate(means):
    axes[1].text(i, mean + 0.5, f'{mean:.1f}', ha='center', va='bottom', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()