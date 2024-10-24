import matplotlib.pyplot as plt
import numpy as np

# Data for coffee ratings across different cafés in Java Island
# These are fictional customer ratings out of 10 for various coffee blends

# Blends offered
coffee_blends = ['Sumatran Bliss', 'Javanese Delight', 'Bali Blue Moon', 'Sulawesi Serenity', 'Papua Paradise']

# Ratings data (created to reflect variation in customer ratings across blends)
ratings_data = [
    [7.8, 8.0, 8.2, 8.5, 7.9, 8.1, 8.3, 7.8, 8.0, 8.2],  # Sumatran Bliss
    [6.5, 6.7, 6.8, 6.4, 6.6, 6.7, 6.9, 6.5, 6.8, 6.9],  # Javanese Delight
    [9.1, 9.0, 8.9, 9.2, 9.1, 9.3, 9.2, 9.0, 9.1, 9.2],  # Bali Blue Moon
    [8.0, 7.8, 7.9, 8.1, 8.3, 8.2, 8.0, 8.1, 7.9, 8.2],  # Sulawesi Serenity
    [7.2, 7.1, 7.4, 7.0, 7.3, 7.5, 7.2, 7.1, 7.3, 7.4]   # Papua Paradise
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a box plot
box = ax.boxplot(ratings_data, patch_artist=True, notch=True, vert=True, showmeans=True)

# Set colors for each box
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot
ax.set_title('Gourmet Coffee Ratings in Cafés Across Java Island', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Coffee Blend', fontsize=12)
ax.set_ylabel('Customer Rating (out of 10)', fontsize=12)
ax.set_xticks(np.arange(1, len(coffee_blends) + 1))
ax.set_xticklabels(coffee_blends, rotation=45, ha='right')

# Customize medians and means
for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

# Create a custom legend
median_legend = plt.Line2D([0], [0], color='black', lw=2, label='Median')
mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Mean')
ax.legend(handles=[median_legend, mean_legend], loc='upper right')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()