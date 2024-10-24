import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# Define the skills and scores
skills = ['Potion Brewing', 'Spell Casting', 'Magical Creatures Care', 'Herbology', 'Alchemy', 'Divination']
novices_scores = [60, 50, 55, 65, 58, 62]
adepts_scores = [70, 75, 68, 72, 80, 78]
masters_scores = [85, 88, 90, 87, 92, 95]

data = [novices_scores, adepts_scores, masters_scores]
categories = ['Novices', 'Adepts', 'Masters']
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Number of variables
num_skills = len(skills)

# Setup radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
angles = [n / float(num_skills) * 2 * pi for n in range(num_skills)]
angles += angles[:1]

# Add background pattern
ax.set_facecolor('#f7f7f9')

# Plot each student category with a gradient fill
for scores, category, color in zip(data, categories, colors):
    scores += scores[:1]
    ax.fill(angles, scores, color=color, alpha=0.3, edgecolor=color)
    ax.plot(angles, scores, linewidth=2, linestyle='-', color=color, label=f'{category} (Avg: {int(np.mean(scores))})')
    
    # Annotate the highest score for each category
    max_idx = scores.index(max(scores))
    ax.annotate(f'{max(scores[:-1])}', xy=(angles[max_idx], scores[max_idx]),
                xytext=(angles[max_idx] + pi/16, scores[max_idx] + 3),
                ha='center', va='center', fontsize=9, color='black',
                arrowprops=dict(facecolor=color, shrink=0.05, lw=0.5))

# Customize radar chart appearance
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Set skill labels with icons
ax.set_xticks(angles[:-1])
ax.set_xticklabels([f'⚗️ {skill}' for skill in skills], fontsize=11, ha='center')

# Set range and style for grid lines
ax.set_ylim(0, 100)
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)), fontsize=8)

# Title and legend adjustments
plt.title('Student Skills Development in\nFantasy School of Enchantment', size=17, color='navy', y=1.1)
legend = plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Student Level", fontsize=10, title_fontsize=11)
legend.set_frame_on(True)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()