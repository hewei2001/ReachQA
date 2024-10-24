import matplotlib.pyplot as plt
import numpy as np

# Define the categories for sustainability assessment
categories = ['Renewable Energy', 'Waste Management', 'Public Transport',
              'Green Spaces', 'Air Quality', 'Water Conservation']
num_vars = len(categories)

# Performance scores for each city
scores = {
    'Amsterdam': [9, 8, 7, 8, 7, 9],
    'San Francisco': [7, 9, 8, 7, 8, 6],
    'Singapore': [8, 7, 9, 6, 9, 8],
    'Stockholm': [9, 9, 7, 9, 9, 8],
    'Sydney': [8, 6, 8, 7, 8, 7]
}

# Add the first score to the end to close the circle for the radar chart
for city in scores:
    scores[city] += scores[city][:1]

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True})

# Radar chart for detailed comparison
ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='grey', size=12)
ax.set_rlabel_position(0)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
ax.set_ylim(0, 10)

colors = ['deepskyblue', 'forestgreen', 'darkorange', 'mediumorchid', 'crimson']

for i, (city, score) in enumerate(scores.items()):
    ax.plot(angles, score, linewidth=2, linestyle='solid', label=city, color=colors[i])
    ax.fill(angles, score, color=colors[i], alpha=0.1)

ax.set_title("Urban Sustainability Performance 2023\nComparative Analysis of Major Cities", size=14, weight='bold')

# Bar chart for average scores
ax2 = axs[1]
average_scores = {city: np.mean(scores[city][:-1]) for city in scores}
ax2.bar(average_scores.keys(), average_scores.values(), color=colors)
ax2.set_ylim(0, 10)
ax2.set_title("Average Sustainability Score per City", size=14, weight='bold')
ax2.set_ylabel('Average Score', size=12)
ax2.set_xticklabels(average_scores.keys(), rotation=45, ha='right', fontsize=12)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1.1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()