import matplotlib.pyplot as plt
import numpy as np

# Culinary dishes and their ratings
ratings_data = {
    'Risotto (Italy)': [7.5, 8.0, 7.8, 8.5, 8.2, 7.9, 8.0],
    'Sushi (Japan)': [9.0, 8.8, 9.2, 9.1, 9.0, 9.1, 8.9],
    'Tacos (Mexico)': [8.0, 7.8, 8.3, 8.1, 8.4, 8.2, 8.0],
    'Curry (India)': [8.5, 8.3, 8.6, 8.7, 8.2, 8.4, 8.3],
    'Ratatouille (France)': [7.8, 8.0, 7.9, 8.2, 8.3, 8.1, 7.9]
}

# List of dish names and their ratings
dishes = list(ratings_data.keys())
ratings = list(ratings_data.values())

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(10, 7))
box = ax.boxplot(ratings, vert=False, patch_artist=True, labels=dishes, notch=True, whis=1.5)

# Colors for the boxes
colors = ['lightcoral', 'lightblue', 'lightgreen', 'khaki', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Title and axis labels
ax.set_title('Culinary Ratings Across International Dishes', fontsize=14, fontweight='bold', pad=20, loc='center')
ax.set_xlabel('Ratings (Scale: 1-10)', fontsize=12)
ax.set_ylabel('Dishes', fontsize=12)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotating the median values
for i, dish in enumerate(dishes, 1):
    median_value = np.median(ratings[i-1])
    ax.text(median_value, i, f'{median_value:.1f}', verticalalignment='center', 
            fontweight='bold', color='black', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Adjust layout for better spacing and clarity
plt.tight_layout()

# Display the plot
plt.show()