import matplotlib.pyplot as plt
import numpy as np

# Data for the boxplot - diversity of artistic techniques in different art periods
art_periods = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Modern Art']
technique_diversity = [
    [15, 22, 25, 30, 18, 20, 25],  # Renaissance
    [35, 40, 38, 42, 36, 33, 45],  # Baroque
    [28, 32, 29, 31, 35, 36, 34],  # Romanticism
    [42, 45, 48, 50, 46, 44, 49],  # Impressionism
    [55, 58, 60, 62, 65, 59, 61]   # Modern Art
]

# Data for the overlay plot - average innovation scores
innovation_scores = [20, 39, 33, 46, 60]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create a horizontal boxplot
box = ax.boxplot(technique_diversity, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightblue', color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(marker='o', color='orange', markersize=6, alpha=0.7))

# Set distinct colors for each box
colors = ['#87CEFA', '#FFD700', '#FF69B4', '#ADFF2F', '#FFA07A']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Overlay line plot for innovation scores
ax.plot(innovation_scores, np.arange(1, len(art_periods) + 1), 'D-', color='darkgreen', linewidth=2,
        markersize=8, label='Average Innovation Score')

# Set titles and labels
ax.set_title('Evolution of Artistic Styles Across Eras:\nTechniques Diversity and Innovation', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Distinct Techniques or Elements', fontsize=14, labelpad=10)
ax.set_yticks(np.arange(1, len(art_periods) + 1))
ax.set_yticklabels(art_periods, fontsize=12)

# Add grid lines for x-axis
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate with additional information
annotations = [
    (30, 1, "Realism & symmetry"),
    (43, 2, "Grandeur & details"),
    (32, 3, "Emotional themes"),
    (47, 4, "Color & brushwork"),
    (63, 5, "Abstraction")
]

for (x, y, text) in annotations:
    ax.annotate(text, xy=(x, y), xytext=(x + 5, y - 0.3),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black'))

# Add legend
ax.legend(loc='lower right', fontsize=12)

# Adjust layout to ensure all text and elements are displayed properly
plt.tight_layout()

# Display the plot
plt.show()