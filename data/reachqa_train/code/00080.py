import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define categories for the domains
categories = ['Web Dev', 'Data Science', 'Mobile Dev', 'Embedded Systems', 'Game Dev']
N = len(categories)

# Proficiency data for each programming language
values = {
    'Python': [8, 10, 5, 5, 6],
    'JavaScript': [10, 5, 7, 3, 6],
    'Java': [6, 6, 9, 7, 6],
    'C++': [4, 7, 7, 10, 9],
    'Swift': [5, 3, 10, 6, 7]
}

# Define the angles for the radar chart
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

# Define custom color palette
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

# Plot each language
for (language, proficiency), color in zip(values.items(), colors):
    data = proficiency + proficiency[:1]  # Complete the loop
    ax.plot(angles, data, linewidth=2, linestyle='-', label=language, color=color, marker='o')
    ax.fill(angles, data, alpha=0.25, color=color)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue')

# Customize grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Set radial limits
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', fontsize=10)

# Title and legend
plt.title('Programming Language Proficiency Radar\nComparative Analysis Across Domains - 2023', size=15, color='navy', pad=40)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=True, framealpha=0.5)

# Annotate key proficiency points
for language, proficiency in values.items():
    for i, (angle, score) in enumerate(zip(angles, proficiency + proficiency[:1])):
        if score == max(proficiency) or score == min(proficiency):
            ax.text(angle, score + 0.5, f"{score}", color='black', fontsize=9, ha='center')

# Display the plot
plt.tight_layout()
plt.show()