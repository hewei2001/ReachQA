import matplotlib.pyplot as plt
import numpy as np

# Data for each age group
children_books = [11, 12, 15, 9, 10, 14, 11, 13, 14, 10, 16]
teens_books = [5, 7, 8, 6, 10, 7, 9, 11, 6, 5, 12]
adults_books = [12, 15, 14, 17, 19, 18, 21, 14, 16, 15, 18]
middle_aged_books = [9, 10, 11, 8, 12, 7, 11, 13, 12, 14, 10]
seniors_books = [5, 4, 6, 5, 7, 8, 6, 5, 7, 5, 6]

data = [children_books, teens_books, adults_books, middle_aged_books, seniors_books]
age_groups = ['Children (6-12)', 'Teens (13-19)', 'Adults (20-35)', 'Middle-aged (36-55)', 'Seniors (56+)']

# Initialize the figure
fig, ax = plt.subplots(figsize=(14, 9))

# Create horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True, labels=age_groups, notch=True, whis=1.5)

# Use a more nuanced color palette
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

# Color customization
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Highlight median values with annotations
medians = [np.median(group) for group in data]
for i, median in enumerate(medians):
    ax.annotate(f'{median}', xy=(median, i + 1), xytext=(5, -15), 
                textcoords='offset points', ha='center', va='center', color='white',
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='dimgray'))

# Enhance grid readability
ax.grid(True, linestyle='--', alpha=0.6, axis='x')

# Titles and labels
ax.set_title('Annual Book Reading Competition 2023\nDistribution of Books Read by Age Group', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Books Read', fontsize=12)
ax.set_ylabel('Age Group', fontsize=12)

# Set aspect for a cleaner layout
plt.gca().set_aspect('auto', adjustable='box')

# Ensure all text is visible
plt.tight_layout()

# Additional plot for trends (line plot)
ax2 = ax.twinx() # Creating a secondary axis
book_trend = [np.mean(group) for group in data]
ax2.plot(book_trend, np.arange(1, len(data)+1), 'o-', color='indianred', linewidth=2, label='Average Trend')
ax2.set_yticks([]) # Hide secondary y-axis tick labels

# Add legend for secondary plot
ax2.legend(loc='upper left', fontsize=10)

plt.show()