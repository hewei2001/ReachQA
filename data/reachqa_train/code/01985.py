import matplotlib.pyplot as plt

# Data: Expanded projected global book publishing shares by genre and sub-genre in 2025 (in percentage)
genres = [
    'Fiction', 'Non-fiction', 'Science Fiction', 'Biography', 
    'Fantasy', 'Mystery', 'Romance', 'Historical', 'Self-Help', 'Thriller', 'Children'
]
percentages = [20, 15, 10, 8, 12, 8, 5, 7, 6, 5, 4]

# Sub-genres for Fiction and Fantasy with their shares
sub_genres = [
    'Classic Fiction', 'Modern Fiction', 'Epic Fantasy', 'Urban Fantasy'
]
sub_percentages = [10, 10, 8, 4]  # Combined 20% for Fiction and 12% for Fantasy

# Colors
colors = ['#fa8072', '#8fbc8f', '#dda0dd', '#ffd700', '#6495ed', '#ee82ee', '#ffa500', 
          '#98fb98', '#cd5c5c', '#4682b4', '#ffb6c1']
sub_colors = ['#ff6347', '#ff8c00', '#7b68ee', '#6a5acd']

plt.figure(figsize=(12, 8))

# Main donut chart
wedges, texts, autotexts = plt.pie(
    percentages,
    labels=genres,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%',
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    textprops=dict(color='navy', fontsize=10)
)

# Sub-genre donut chart
sub_wedges, sub_texts = plt.pie(
    sub_percentages,
    colors=sub_colors,
    radius=0.6,
    startangle=90,
    wedgeprops=dict(width=0.2, edgecolor='w')
)

# Enhance percentage labels aesthetics
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# Draw the white circle in the center for both rings
centre_circle = plt.Circle((0, 0), 0.5, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Main and sub-genre titles
plt.title("Projected Global Book Publishing by Genre (2025)\nIn-depth Analysis of Literary Segments", fontsize=14, weight='bold')

# Legend for genres and sub-genres
plt.legend(
    wedges + sub_wedges,
    genres + sub_genres,
    title="Genres and Sub-genres",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=9
)

# Tight layout adjustment
plt.tight_layout()

# Show plot
plt.show()