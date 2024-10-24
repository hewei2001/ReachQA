import matplotlib.pyplot as plt
import numpy as np

# Define decades with 21 elements (1800 to 2000)
decades = np.arange(1800, 2010, 10)

# Popularity scores for each genre by decade (already have 21 elements)
gothic_fiction = [30, 35, 40, 30, 20, 10, 5, 3, 1, 1, 2, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1]
realism = [10, 15, 20, 30, 50, 60, 70, 75, 65, 60, 50, 45, 40, 35, 30, 30, 25, 20, 15, 10, 10]
science_fiction = [0, 0, 0, 5, 10, 20, 30, 40, 60, 70, 80, 75, 65, 55, 50, 45, 40, 35, 30, 25, 20]
fantasy = [10, 5, 5, 10, 15, 20, 30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 85, 80, 75, 70, 65]
mystery = [20, 25, 30, 40, 45, 50, 55, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 10, 10, 5]

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stackplot
ax.stackplot(decades, gothic_fiction, realism, science_fiction, fantasy, mystery,
             labels=['Gothic Fiction', 'Realism', 'Science Fiction', 'Fantasy', 'Mystery'],
             colors=['#8B0000', '#696969', '#1E90FF', '#8A2BE2', '#FFD700'], alpha=0.8)

# Title and labels
ax.set_title("The Evolution of Literary Genres\nA Journey Through Time (1800-2010)", fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Score', fontsize=12)

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Face color for visibility
ax.set_facecolor('#f7f7f7')

# X-axis ticks
ax.set_xticks(decades)
ax.set_xticklabels([str(year) for year in decades], rotation=45)

# Annotate total scores above plots
total_popularity = np.sum([gothic_fiction, realism, science_fiction, fantasy, mystery], axis=0)
for i, year in enumerate(decades):
    ax.text(year, total_popularity[i] + 2, str(total_popularity[i]), fontsize=10, ha='center', fontweight='bold')

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()