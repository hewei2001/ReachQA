import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Culinary techniques and their popularity scores
culinary_techniques = [
    "Sous Vide",
    "Fermentation",
    "Smoking",
    "Pickling",
    "Braising",
    "Sautéing",
    "Grilling",
    "Poaching",
    "Steaming",
    "Roasting"
]

popularity_scores = [15, 25, 20, 18, 17, 40, 50, 30, 35, 45]

# Assigning gradient-like colors for each bar
colors = ['#dcedc8', '#aed581', '#7cb342', '#4caf50', '#388e3c', 
          '#c8e6c9', '#81c784', '#66bb6a', '#43a047', '#2e7d32']

fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques))

# Create bars with gradient-like colors and 3D effect
bars = ax.barh(y_pos, popularity_scores, color=colors, edgecolor='gray', alpha=0.85, height=0.8)

# Adding a 3D effect with a shadow
for bar in bars:
    ax.add_patch(mpatches.FancyBboxPatch(
        (bar.get_x(), bar.get_y()), bar.get_width(), bar.get_height(),
        boxstyle="round,pad=0.3", ec="none", fc="black", alpha=0.1
    ))

ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques, fontsize=10, fontweight='medium')
ax.invert_yaxis()

# Titles and labels
ax.set_title('Top Culinary Techniques in World Cuisines\nBased on Global Chef Survey', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Popularity Score (%)', fontsize=12)
ax.set_ylabel('Culinary Techniques', fontsize=12)

# Annotate each bar with the popularity score
for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
            f'{popularity_scores[i]}%', va='center', color='black', fontsize=10)

# Improved grid lines and background
ax.grid(axis='x', linestyle='--', color='gray', alpha=0.6)
ax.set_facecolor('#f0f0f0')

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()