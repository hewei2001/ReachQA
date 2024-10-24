import matplotlib.pyplot as plt
import numpy as np

# Expanded Art Movements and their corresponding influence scores
art_movements = [
    "Proto-Renaissance",
    "Early Renaissance",
    "High Renaissance",
    "Mannerism",
    "Northern Renaissance",
    "Venetian Renaissance",
    "Late Renaissance",
    "Baroque",
    "Rococo",
    "Neoclassicism",
    "Romanticism"
]

# Impact, Innovation, and Cultural Significance Scores
impact_scores = [30, 45, 80, 50, 60, 55, 35, 70, 40, 65, 75]
innovation_scores = [25, 40, 85, 45, 55, 50, 30, 65, 35, 60, 70]
cultural_significance = [35, 50, 75, 55, 65, 60, 40, 75, 45, 70, 80]

# Normalized total scores
total_scores = [i + j + k for i, j, k in zip(impact_scores, innovation_scores, cultural_significance)]

# Plotting
fig, ax = plt.subplots(figsize=(16, 10))

# Creating the stacked bar chart
bar_width = 0.6
bars1 = ax.barh(art_movements, impact_scores, color='#FF5733', edgecolor='black', height=bar_width, label='Impact Score')
bars2 = ax.barh(art_movements, innovation_scores, left=impact_scores, color='#DAF7A6', edgecolor='black', height=bar_width, label='Innovation Score')
bars3 = ax.barh(art_movements, cultural_significance, left=[i + j for i, j in zip(impact_scores, innovation_scores)], color='#3498DB', edgecolor='black', height=bar_width, label='Cultural Significance')

# Add scores as text annotations
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        width = bar.get_width()
        ax.text(bar.get_x() + width/2, bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center', ha='center', fontsize=8, color='black')

# Titles and labels
ax.set_title('Renaissance and Beyond: Evolution of Art Movements\nA Comprehensive Comparison of Impact, Innovation, and Cultural Significance', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Combined Scores', fontsize=12)
ax.set_ylabel('Art Movements', fontsize=12)
ax.set_xlim(0, max(total_scores) + 10)

# Add a legend
ax.legend(title='Score Components', loc='upper right', frameon=True, fontsize=10)

# Customize grid and layout
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()