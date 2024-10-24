import matplotlib.pyplot as plt
import numpy as np

# Data: Well-being scores for different cities
cities = ['New York', 'Tokyo', 'London', 'Paris', 'Vancouver']

# Well-being scores across different aspects for each city
well_being_scores = {
    'New York': [65, 70, 62, 68, 75, 64, 80, 70, 72],
    'Tokyo': [58, 60, 55, 62, 67, 61, 59, 68, 64],
    'London': [72, 78, 74, 76, 80, 70, 68, 75, 77],
    'Paris': [63, 67, 64, 66, 72, 65, 71, 69, 68],
    'Vancouver': [80, 85, 82, 87, 89, 84, 86, 83, 88]
}

# Convert the data into a list of arrays for plotting
data = [np.array(well_being_scores[city]) for city in cities]

# Calculate average scores for each city for the bar plot
average_scores = [np.mean(scores) for scores in data]

# Create a 1x2 grid for plots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: horizontal box plot
bplot = axs[0].boxplot(data, vert=False, patch_artist=True, labels=cities, notch=True, whis=1.5)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

for whisker in bplot['whiskers']:
    whisker.set(color='#7570b3', linewidth=1.5, linestyle='--')

for cap in bplot['caps']:
    cap.set(color='#7570b3', linewidth=1.5)

for median in bplot['medians']:
    median.set(color='black', linewidth=2)

for flier in bplot['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

axs[0].grid(True, linestyle='--', which='both', alpha=0.7)
axs[0].set_title('Well-being Impact of Urban Green Spaces\nAcross Major Cities in 2023', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Well-being Score (0-100)', fontsize=12)
axs[0].set_ylabel('Cities', fontsize=12)

# Second subplot: bar plot for average scores
axs[1].barh(cities, average_scores, color=colors, alpha=0.7)
axs[1].set_title('Average Well-being Scores\nAcross Cities', fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel('Average Score', fontsize=12)
axs[1].set_ylabel('Cities', fontsize=12)

# Display the values on the bars
for i, v in enumerate(average_scores):
    axs[1].text(v + 0.5, i, f"{v:.1f}", va='center', fontsize=10, color='black')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()