import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Popularity scores for each genre
science_fiction_popularity = [70, 72, 75, 73, 78, 80, 81, 85, 83, 88, 90]
romance_popularity = [60, 65, 68, 70, 72, 76, 78, 77, 75, 79, 82]
mystery_popularity = [55, 60, 63, 65, 67, 70, 72, 74, 78, 80, 83]
historical_fiction_popularity = [50, 55, 58, 60, 62, 65, 68, 70, 72, 74, 77]
non_fiction_popularity = [65, 68, 70, 72, 74, 77, 79, 82, 84, 86, 88]

# Combine the data into a list for boxplot
data = [
    science_fiction_popularity,
    romance_popularity,
    mystery_popularity,
    historical_fiction_popularity,
    non_fiction_popularity
]

# Genre labels
genres = ['Science Fiction', 'Romance', 'Mystery', 'Historical Fiction', 'Non-Fiction']

# Set color palette
colors = sns.color_palette("pastel", len(genres))

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create vertical box plot
box = ax.boxplot(data, patch_artist=True, vert=True, labels=genres, notch=True, medianprops=dict(color="black"))

# Add colors to the boxes and plot mean points
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

# Add mean markers
means = [np.mean(d) for d in data]
ax.plot(range(1, len(genres)+1), means, linestyle='None', marker='o', color='darkred', label='Mean')

# Plot individual data points
for i, y in enumerate(data):
    x = np.random.normal(i + 1, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.6, color=colors[i])

# Title and labels
ax.set_title("The Evolution of Literary Genres in\nDigital Libraries (2013-2023)", fontsize=16, fontweight='bold')
ax.set_xlabel("Genres", fontsize=12)
ax.set_ylabel("Popularity Score", fontsize=12)

# Customize grid and style
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_yticks(np.arange(50, 101, 5))
ax.legend()

# Automatically adjust the layout to prevent overlapping
plt.xticks(rotation=15, ha='right')
plt.tight_layout()

# Display the plot
plt.show()