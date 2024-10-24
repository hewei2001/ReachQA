import matplotlib.pyplot as plt

# Data construction: Scores for each genre
fiction_scores = [7, 8, 8, 8, 9, 9, 9, 10, 6, 7, 8, 7, 9, 8, 8]
mystery_scores = [6, 7, 7, 8, 9, 8, 6, 7, 6, 7, 5, 8, 7, 6, 8]
science_fiction_scores = [5, 6, 7, 6, 5, 7, 8, 4, 9, 6, 5, 6, 4, 7, 6]
fantasy_scores = [9, 10, 8, 9, 8, 8, 9, 10, 10, 9, 8, 7, 9, 9, 8]
non_fiction_scores = [6, 7, 5, 6, 8, 5, 7, 6, 5, 7, 8, 6, 6, 5, 7]

# Combine the scores into a list of lists
genre_scores = [
    fiction_scores,
    mystery_scores,
    science_fiction_scores,
    fantasy_scores,
    non_fiction_scores
]

# Genre names
genres = ['Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Non-Fiction']

# Create the box plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(genre_scores, notch=True, patch_artist=True, 
           boxprops=dict(facecolor='skyblue', color='navy'),
           whiskerprops=dict(color='navy'),
           capprops=dict(color='navy'),
           medianprops=dict(color='darkred'),
           flierprops=dict(marker='o', markerfacecolor='gray', markersize=6, linestyle='none', markeredgecolor='black'))

# Set title and labels
ax.set_title("Evolvement of Literary Genres:\nA Decade of Book Club Reviews (2013-2023)", fontsize=14, fontweight='bold')
ax.set_ylabel('Review Scores', fontsize=12)
ax.set_xticklabels(genres, fontsize=11)

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add annotations for context
ax.annotate('Consistent favorites', xy=(1, 9), xytext=(1.5, 9.5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkgreen')
ax.annotate('Diverse opinions', xy=(3, 4), xytext=(3.5, 3.5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkred')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()