import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data: Number of books read per year by young adults in different regions
fantasy_books = [18, 15, 20, 22]     # Urban, Suburban, Rural, Coastal
mystery_books = [14, 18, 12, 16]     # Urban, Suburban, Rural, Coastal
scifi_books = [20, 12, 15, 18]       # Urban, Suburban, Rural, Coastal
romance_books = [10, 16, 8, 14]      # Urban, Suburban, Rural, Coastal

# Group data for horizontal box plot
book_genres = [fantasy_books, mystery_books, scifi_books, romance_books]
genre_labels = ['Fantasy', 'Mystery', 'Science Fiction', 'Romance']
regions = ['Urban', 'Suburban', 'Rural', 'Coastal']

# Colors for each genre
colors = sns.color_palette("coolwarm", len(book_genres))

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 9))

# Box plot with customized appearances
box = ax.boxplot(book_genres, vert=False, patch_artist=True, labels=genre_labels,
                 notch=True, flierprops=dict(markerfacecolor='red', marker='o', markersize=8, alpha=0.5))

# Apply gradient colors to each genre box
for i, patch in enumerate(box['boxes']):
    patch.set_facecolor(colors[i])
    patch.set_alpha(0.7)

# Customize whiskers, medians, and caps
for whisker in box['whiskers']:
    whisker.set(color='black', linestyle='--', linewidth=1.5)
for median in box['medians']:
    median.set(color='darkblue', linewidth=2)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)

# Overlay jittered individual data points
for i, genre in enumerate(book_genres):
    y_positions = np.random.normal(i + 1, 0.02, size=len(genre))
    ax.scatter(genre, y_positions, alpha=0.5, color=colors[i], edgecolor='black', s=100, label=f"{genre_labels[i]}")

# Adding details to the plot
ax.set_title('Exploring Young Adult Reading Preferences:\nA Regional Analysis of Popular Genres in 2023',
             fontsize=14, weight='bold')
ax.set_xlabel('Number of Books Read per Year', fontsize=12)
ax.set_ylabel('Book Genres', fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Annotations for additional information
for i, genre in enumerate(book_genres):
    for j, val in enumerate(genre):
        ax.annotate(f'{val} ({regions[j]})', (val, i + 1), textcoords='offset points',
                    xytext=(5, -12), ha='center', fontsize=9, color='black')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Subtle background texture
ax.set_facecolor('#f7f7f7')

# Improved legend for the scatter plot
handles, _ = ax.get_legend_handles_labels()
by_label = dict(zip(genre_labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right', fontsize=10, frameon=True)

# Display the plot
plt.show()