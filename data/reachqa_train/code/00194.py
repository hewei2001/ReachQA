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

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the boxplots
box = ax.boxplot(all_scores, labels=district_labels, patch_artist=True, notch=True, vert=True)

# Customize the box plots with different colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize other plot elements
ax.set_title("Student Performance in Mathematics:\n8th Grade Math Scores by District", fontsize=14)
ax.set_xlabel("School District", fontsize=12)
ax.set_ylabel("Math Scores", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Further customize the box plots
for element in ['whiskers', 'caps', 'medians']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()