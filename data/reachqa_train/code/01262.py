import matplotlib.pyplot as plt
import squarify  # for creating the treemap

# Define genres and their respective revenues (in billions)
genres = [
    'Action', 'Adventure', 'Comedy', 'Drama', 'Horror',
    'Science Fiction', 'Fantasy', 'Romantic Comedy', 'Animation', 'Thriller'
]
revenues = [120, 85, 60, 50, 45, 65, 70, 30, 55, 40]  # in billions of dollars

# Colors for each genre
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Calculate the proportional sizes for the treemap
sizes = squarify.normalize_sizes(revenues, 800, 400)

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=sizes, label=[f'{genre}\n${rev}B' for genre, rev in zip(genres, revenues)], color=colors, alpha=0.8, ax=ax, text_kwargs={'fontsize': 10})

# Title and aesthetics
ax.set_title('Global Film Industry Revenue Breakdown:\nA Decade of Genres (2011-2020)', fontsize=16, fontweight='bold', pad=10)
ax.axis('off')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()