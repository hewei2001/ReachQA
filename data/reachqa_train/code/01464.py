import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the skills
skills = ['Potion Brewing', 'Spell Casting', 'Magical Creatures Care', 'Herbology', 'Alchemy', 'Divination']

# Skill scores for each category
novices_scores = [60, 50, 55, 65, 58, 62]
adepts_scores = [70, 75, 68, 72, 80, 78]
masters_scores = [85, 88, 90, 87, 92, 95]

# Combine data into a list of lists
data = [novices_scores, adepts_scores, masters_scores]

# Number of variables
num_skills = len(skills)

# Set up radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
angles = [n / float(num_skills) * 2 * pi for n in range(num_skills)]
angles += angles[:1]  # Close the plot

# Plot each student category
for scores, category, color in zip(data, ['Novices', 'Adepts', 'Masters'], ['#FF9999', '#66B3FF', '#99FF99']):
    scores += scores[:1]  # Close the plot
    ax.fill(angles, scores, color=color, alpha=0.25, label=category)
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=color)

# Customize the radar chart
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Set labels for each skill
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=10)

# Set the range for each axis
ax.set_ylim(0, 100)

# Add grid lines and labels
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)), fontsize=8)

# Add title and legend
plt.title('Student Skills Development in\nFantasy School of Enchantment', size=15, color='navy', y=1.1, ha='center')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Student Level")

# Automatically adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()