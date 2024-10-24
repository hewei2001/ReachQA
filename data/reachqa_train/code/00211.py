import matplotlib.pyplot as plt
import numpy as np

# Define the adventure scores for each terrain
terrain_labels = [
    'Mountains', 'Deserts', 'Oceans', 'Forests', 
    'Urban Landscapes', 'Caves', 'Arctic Regions'
]

# Extended data for each terrain, increasing complexity
mountains_scores = [85, 88, 75, 92, 78, 85, 89, 90, 87, 88, 91, 84, 86, 80, 79, 83, 87, 89, 90, 82]
deserts_scores = [60, 65, 70, 72, 68, 75, 74, 73, 69, 65, 64, 67, 70, 71, 62, 66, 70, 68, 64, 63]
oceans_scores = [95, 98, 90, 89, 92, 97, 94, 95, 96, 93, 90, 91, 89, 88, 92, 95, 93, 92, 91, 94]
forests_scores = [76, 80, 85, 82, 79, 75, 81, 84, 77, 78, 80, 83, 82, 79, 80, 81, 78, 76, 85, 80]
urban_scores = [55, 60, 62, 58, 59, 54, 56, 61, 60, 62, 59, 57, 55, 58, 60, 63, 57, 59, 56, 55]
caves_scores = [70, 72, 68, 74, 71, 69, 75, 78, 77, 76, 73, 72, 70, 74, 75, 73, 74, 76, 77, 75]
arctic_scores = [80, 82, 81, 79, 85, 87, 90, 88, 86, 84, 83, 81, 82, 80, 85, 89, 87, 86, 84, 83]

# Compile the scores into a list of lists for each terrain
all_scores = [
    mountains_scores, deserts_scores, oceans_scores, forests_scores, 
    urban_scores, caves_scores, arctic_scores
]

# Create the box plot
fig, ax = plt.subplots(figsize=(16, 10))
box = ax.boxplot(all_scores, vert=False, patch_artist=True, labels=terrain_labels, notch=True, whis=1.5)

# Customizing the plot with colors and styles
colors = ['#FF5733', '#FFC300', '#33FF57', '#3380FF', '#FF33FB', '#8E44AD', '#16A085']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Enhance visualization: Adjust whiskers, medians, and caps
for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')

for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

# Annotate with additional statistical information
for i, line in enumerate(box['means']):
    mean_value = line.get_ydata().mean()
    ax.text(mean_value, i + 1, f'Mean: {mean_value:.1f}', 
            va='center', ha='right', fontsize=9, color='navy', alpha=0.8)

# Annotate outliers
for i, line in enumerate(box['fliers']):
    y = line.get_ydata()
    x = line.get_xdata()
    for (xi, yi) in zip(x, y):
        ax.text(xi, yi, f'{yi:.0f}', va='bottom', ha='left', fontsize=9, color=colors[i % len(colors)], alpha=0.8)

# Set titles and labels
ax.set_title('Adventure Score Distribution Across Diverse Terrains\nin Expedition Earth', fontsize=16, fontweight='bold')
ax.set_xlabel('Adventure Scores', fontsize=12)
ax.set_ylabel('Terrains', fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()