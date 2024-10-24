import matplotlib.pyplot as plt
import numpy as np

# Define tea varieties and continents
tea_varieties = ['Green Tea', 'Black Tea', 'Herbal Tea']
continents = ['Asia', 'Africa', 'Europe']

# Original flavor intensity scores for each tea variety from different continents
green_tea_scores = [
    [70, 82, 85, 90, 72],  # Asia
    [60, 65, 68, 62, 70],  # Africa
    [75, 78, 80, 85, 82]   # Europe
]

black_tea_scores = [
    [85, 88, 90, 92, 89],  # Asia
    [70, 72, 75, 78, 74],  # Africa
    [80, 83, 85, 88, 86]   # Europe
]

herbal_tea_scores = [
    [60, 65, 62, 68, 63],  # Asia
    [75, 78, 80, 85, 82],  # Africa
    [65, 67, 70, 72, 68]   # Europe
]

# New data: Average scores across tea varieties for each continent
average_scores = {
    'Asia': [(np.mean(green_tea_scores[0]) + np.mean(black_tea_scores[0]) + np.mean(herbal_tea_scores[0])) / 3],
    'Africa': [(np.mean(green_tea_scores[1]) + np.mean(black_tea_scores[1]) + np.mean(herbal_tea_scores[1])) / 3],
    'Europe': [(np.mean(green_tea_scores[2]) + np.mean(black_tea_scores[2]) + np.mean(herbal_tea_scores[2])) / 3]
}

# Aggregate the original data
data = [green_tea_scores, black_tea_scores, herbal_tea_scores]

# Plot configuration
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Box Plot for original data
positions = np.array(range(len(continents))) * 4
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

for i, scores in enumerate(data):
    pos = positions + i
    bp = axes[0].boxplot(scores, positions=pos, widths=0.6, patch_artist=True, notch=True)
    for patch, color in zip(bp['boxes'], [colors[i]] * len(continents)):
        patch.set_facecolor(color)
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

axes[0].set_xticks(positions + 1)
axes[0].set_xticklabels(continents, fontsize=12)
axes[0].set_title("Global Rise of Tea Varieties:\nTaste Profiles Across Continents", fontsize=16, fontweight='bold')
axes[0].set_ylabel("Flavor Intensity Score", fontsize=14)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Legend for the box plot
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
axes[0].legend(handles, tea_varieties, title='Tea Varieties', loc='upper right', fontsize=12)

# Line Plot for average scores
x_pos = np.arange(len(continents))
average_values = [average_scores[continent][0] for continent in continents]

axes[1].plot(x_pos, average_values, marker='o', linestyle='-', color='#ff7f0e', linewidth=2, markersize=8)
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(continents, fontsize=12)
axes[1].set_title("Average Flavor Intensity Across Tea Varieties", fontsize=16, fontweight='bold')
axes[1].set_ylabel("Average Flavor Intensity Score", fontsize=14)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()