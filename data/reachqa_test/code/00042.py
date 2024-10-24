import matplotlib.pyplot as plt
import numpy as np

# Define coffee plantations and their quality scores
plantations = ["Blue Mountain", "Kona", "Yirgacheffe", "Sidamo", "Guatemala Antigua", "Sumatra Mandheling"]
blue_mountain_scores = [82, 86, 84, 90, 88, 91, 87, 85, 89, 92, 88, 90, 84, 86]
kona_scores = [80, 82, 85, 86, 83, 87, 85, 81, 84, 86, 88, 84, 83, 85]
yirgacheffe_scores = [88, 90, 91, 89, 92, 95, 93, 90, 89, 92, 91, 90, 91, 94]
sidamo_scores = [78, 81, 80, 83, 82, 84, 82, 80, 79, 81, 80, 82, 83, 80]
guatemala_antigua_scores = [85, 88, 87, 89, 86, 87, 88, 90, 85, 86, 87, 89, 88, 87]
sumatra_mandheling_scores = [77, 78, 79, 82, 80, 81, 80, 79, 78, 82, 83, 81, 80, 82]
scores_data = [
    blue_mountain_scores,
    kona_scores,
    yirgacheffe_scores,
    sidamo_scores,
    guatemala_antigua_scores,
    sumatra_mandheling_scores
]

# Calculate means for each plantation
means = [np.mean(data) for data in scores_data]

# Plotting
fig, ax = plt.subplots(figsize=(14, 9))
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(plantations)))

box = ax.boxplot(scores_data, vert=False, patch_artist=True, labels=plantations, notch=True, whis=1.5)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker in box['whiskers']:
    whisker.set(color='saddlebrown', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='saddlebrown', linewidth=1.5)
for median in box['medians']:
    median.set(color='darkred', linewidth=2)

# Add means to the plot
ax.scatter(means, range(1, len(plantations) + 1), color='blue', marker='D', label='Mean Score')

# Overlay scatter for data points
for i, scores in enumerate(scores_data):
    jittered_y = np.random.normal(i+1, 0.04, size=len(scores))
    ax.scatter(scores, jittered_y, alpha=0.6, color='black', s=15, edgecolor='w', linewidth=0.5)

ax.set_xlabel("Quality Score (60-100)", fontsize=12)
ax.set_title("Detailed Analysis of Coffee Bean Quality Scores\nAcross Renowned Plantations", fontsize=14)

# Grid and layout adjustments
ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='x')
plt.tight_layout()

# Legend
legend_elements = [
    plt.Line2D([0], [0], color="tan", lw=2, label='Box - IQR'),
    plt.Line2D([0], [0], color="darkred", lw=2, label='Median'),
    plt.Line2D([0], [0], color="saddlebrown", lw=1.5, linestyle='-', label='Whiskers'),
    plt.Line2D([0], [0], marker='o', color='w', label='Data Points', markerfacecolor='black', markersize=6),
    plt.Line2D([0], [0], marker='D', color='w', label='Mean Score', markerfacecolor='blue', markersize=8),
]

plt.legend(handles=legend_elements, loc='upper right', fontsize='small', title="Plot Elements")
plt.show()