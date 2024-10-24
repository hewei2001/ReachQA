import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define skill categories
categories = ['Strength', 'Speed', 'Intelligence', 'Stamina', 'Agility']
N = len(categories)

# Superhero skill data for each universe
data = {
    'Marvel': [8, 9, 6, 7, 8],
    'DC': [9, 7, 8, 6, 9],
    'Anime': [6, 8, 9, 7, 6],
    'Fantasy': [7, 5, 7, 8, 5],
    'Sci-Fi': [5, 6, 8, 9, 7]
}

# Calculate angle for each axis
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Prepare data for bar chart - calculate average score per category
category_averages = np.mean(list(data.values()), axis=0)

# Initialize subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'polar': True, 'projection': None})

# Radar Chart
def plot_radar(ax, data, categories, angles, colors):
    for i, (universe, values) in enumerate(data.items()):
        values += values[:1]  # Ensure it forms a closed loop
        ax.plot(angles, values, color=colors[i], linewidth=2, linestyle='solid', label=universe)
        ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='grey', size=12)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
    ax.set_title('Superhero Skill Analysis', size=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 10)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Bar Chart
def plot_bar(ax, category_averages, categories):
    ax.barh(categories, category_averages, color='skyblue')
    ax.set_xlim(0, 10)
    ax.set_xlabel('Average Skill Score', fontsize=12)
    ax.set_title('Average Skill Scores Across Universes', size=15, fontweight='bold')
    ax.invert_yaxis()
    for i, v in enumerate(category_averages):
        ax.text(v + 0.1, i, f"{v:.1f}", color='black', va='center', fontsize=10)

# Define colors for radar chart universes
colors = ['#FF5733', '#33FF57', '#3357FF', '#F033FF', '#33FFF5']

# Plot both charts
plot_radar(ax1, data, categories, angles, colors)
plot_bar(ax2, category_averages, categories)

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Show plot
plt.show()