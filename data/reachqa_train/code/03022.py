import matplotlib.pyplot as plt
import numpy as np

# Synthetic manuscript review times in weeks for different genres
fiction = [4, 5, 6, 8, 10, 12, 6, 7, 9, 11, 7, 8, 9, 7, 6, 8, 10]
non_fiction = [5, 6, 8, 9, 11, 13, 10, 11, 7, 9, 10, 12, 11, 13]
mystery = [3, 4, 6, 7, 10, 12, 3, 4, 5, 9, 6, 7, 8, 10, 11, 9]
sci_fi = [4, 5, 7, 8, 11, 12, 8, 6, 9, 10, 7, 11, 9, 8]
fantasy = [6, 7, 9, 11, 14, 15, 10, 12, 8, 9, 13, 12, 14, 13]
historical_fiction = [7, 9, 10, 12, 13, 15, 8, 11, 9, 10, 11, 13]
thriller = [5, 6, 8, 7, 9, 11, 6, 8, 5, 7, 9, 10, 8, 9]
romance = [6, 8, 9, 10, 12, 14, 9, 8, 10, 11, 10, 9, 11]

data = [fiction, non_fiction, mystery, sci_fi, fantasy, historical_fiction, thriller, romance]
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Historical Fiction', 'Thriller', 'Romance']

plt.figure(figsize=(14, 10))

# Create the violin plot
violin = plt.violinplot(data, vert=False, showmeans=False, showmedians=True)

# Add the horizontal boxplot on top of the violin plot
box = plt.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5,
                  boxprops=dict(facecolor='white', color='black', alpha=0.7),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  medianprops=dict(color='red', linewidth=1.5),
                  flierprops=dict(marker='o', color='green', alpha=0.5))

colors = ['#add8e6', '#ffcccb', '#c3e6cb', '#fdd835', '#9575cd', '#ff8a65', '#64b5f6', '#dce775']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
plt.title('Publishing House Insights:\nManuscript Review Time Distribution Across Genres', fontsize=16, fontweight='bold')
plt.xlabel('Review Time (weeks)', fontsize=12)
plt.yticks(range(1, len(genres) + 1), genres, fontsize=10)

# Annotate with mean values for additional context
for i, genre in enumerate(data):
    mean_val = np.mean(genre)
    plt.text(mean_val + 0.2, i + 1, f'Mean: {mean_val:.1f}', verticalalignment='center', fontsize=9, color='darkblue')

# Grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()