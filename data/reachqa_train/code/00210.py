import matplotlib.pyplot as plt
import numpy as np

# Define the adventure scores for each terrain
terrain_labels = ['Mountains', 'Deserts', 'Oceans', 'Forests', 'Urban Landscapes']
mountains_scores = [85, 88, 75, 92, 78, 85, 89, 90, 87, 88, 91, 84, 86, 80, 79]
deserts_scores = [60, 65, 70, 72, 68, 75, 74, 73, 69, 65, 64, 67, 70, 71, 62]
oceans_scores = [95, 98, 90, 89, 92, 97, 94, 95, 96, 93, 90, 91, 89, 88, 92]
forests_scores = [76, 80, 85, 82, 79, 75, 81, 84, 77, 78, 80, 83, 82, 79, 80]
urban_scores = [55, 60, 62, 58, 59, 54, 56, 61, 60, 62, 59, 57, 55, 58, 60]

# Compile the scores into a list of lists for each terrain
all_scores = [mountains_scores, deserts_scores, oceans_scores, forests_scores, urban_scores]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(all_scores, vert=False, patch_artist=True, labels=terrain_labels, notch=True, whis=1.5)

# Customizing the plot with colors and styles
colors = ['#FF5733', '#FFC300', '#33FF57', '#3380FF', '#FF33FB']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Enhance visualization: Adjusting the whiskers and medians
for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')

for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

# Setting titles and labels
ax.set_title('Adventure Score Distribution Across Diverse Terrains\nin Expedition Earth', fontsize=16, fontweight='bold')
ax.set_xlabel('Adventure Scores', fontsize=12)
ax.set_ylabel('Terrains', fontsize=12)

# Annotate with additional information, like outliers
for i, line in enumerate(box['fliers']):
    # Draw the line locations at specific (x, y) points, these represent outliers
    y = line.get_ydata()
    x = line.get_xdata()
    for (xi, yi) in zip(x, y):
        ax.text(xi, yi, f'{yi:.0f}', va='bottom', ha='left', fontsize=9, color=colors[i % len(colors)], alpha=0.8)

# Ensure layout is tight and clear
plt.tight_layout()

# Show the plot
plt.show()