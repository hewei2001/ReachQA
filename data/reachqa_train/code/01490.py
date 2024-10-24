import matplotlib.pyplot as plt
import numpy as np

# Ingredient diversity data for each cuisine
cuisines = ['Italian', 'Japanese', 'Mexican', 'Indian', 'French', 'Chinese', 'Mediterranean']
ingredient_data = [
    [12, 15, 11, 14, 13, 18, 16, 15, 17, 14, 20, 22],  # Italian
    [8, 10, 9, 11, 12, 8, 10, 9, 11, 10, 14, 13],      # Japanese
    [20, 22, 19, 21, 23, 22, 25, 19, 20, 21, 29, 30],  # Mexican
    [25, 28, 26, 27, 29, 30, 28, 27, 26, 31, 33, 32],  # Indian
    [15, 17, 16, 18, 19, 16, 15, 14, 17, 18, 22, 21],  # French
    [10, 11, 12, 13, 14, 10, 15, 16, 13, 14, 18, 17],  # Chinese
    [18, 20, 17, 19, 21, 23, 22, 24, 25, 21, 27, 28]   # Mediterranean
]

# Assume additional factor - Average Cost for ingredients (arbitrary values)
avg_cost = [4.5, 6.2, 5.3, 7.1, 5.9, 6.8, 5.0]

# Create the plot
fig, ax = plt.subplots(figsize=(16, 9))

# Horizontal box plot
bp = ax.boxplot(ingredient_data, vert=False, patch_artist=True, notch=True, showmeans=True,
                meanline=True, meanprops=dict(linestyle='-', linewidth=2.5, color='blue'))

# Customizing colors for each box
colors = ['#FFD700', '#8B008B', '#FF6347', '#FF4500', '#4682B4', '#32CD32', '#FF69B4']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.6)

# Enhance medians, whiskers, and caps
for whisker in bp['whiskers']:
    whisker.set(color='darkred', linewidth=2, linestyle="--")
for cap in bp['caps']:
    cap.set(color='darkred', linewidth=2)
for median in bp['medians']:
    median.set(color='black', linewidth=3)

# Add a scatter plot for average cost overlaid on the box plots
for i, cost in enumerate(avg_cost):
    ax.scatter(cost*5, i+1, color='black', s=100, label='Avg Cost' if i == 0 else "")

# Adding title and labels
ax.set_title('Culinary Ingredient Diversity and Cost Analysis\nAcross Global Cuisines',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Distinct Ingredients', fontsize=13)
ax.set_ylabel('Cuisine Types', fontsize=13)
ax.set_yticklabels(cuisines, fontsize=12)

# Adding legend for average cost
ax.legend(loc='upper right', fontsize=12)

# Grid and limits
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(5, 35)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()