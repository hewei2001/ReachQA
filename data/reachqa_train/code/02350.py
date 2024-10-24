import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Define fruits and nutritional categories
fruits = ['Blueberries', 'Bananas', 'Oranges', 'Strawberries', 'Apples']
categories = ['Vitamins', 'Fiber', 'Antioxidants', 'Minerals', 'Natural Sugars']

# Nutritional scores for each fruit
nutritional_scores = {
    'Blueberries': [9, 4, 10, 6, 5],
    'Bananas': [6, 8, 4, 5, 8],
    'Oranges': [8, 5, 7, 6, 7],
    'Strawberries': [7, 6, 9, 5, 6],
    'Apples': [7, 7, 6, 7, 8]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Updated color palette
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f']
line_styles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

for idx, (fruit, color, linestyle) in enumerate(zip(fruits, colors, line_styles)):
    values = nutritional_scores[fruit]
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.25, label=fruit)
    ax.plot(angles, values, color=color, linewidth=2, linestyle=linestyle)
    ax.scatter(angles, values, color=color, s=50, zorder=3)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='navy')

# Enhance grid lines
ax.yaxis.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)
ax.spines['polar'].set_visible(False)

# Add radial axis labels
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=10)
ax.set_ylim(0, 10)

# Title with line break for clarity
plt.title("Exploring Nutritional Value: \nThe Five Fruit Diet Plan", size=18, fontweight='bold', pad=40)

# Enhanced legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Fruits', title_fontsize=12, frameon=False)

# Shadow effect
ax.add_patch(patches.Circle((0, 0), radius=10, transform=ax.transData._b, edgecolor='lightgray', facecolor='none', zorder=0))

# Layout adjustment
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Display the radar chart
plt.show()