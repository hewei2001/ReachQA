import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Centuries represented numerically for simplicity
centuries = [18, 19, 20, 21]

# Data for each genre across four centuries
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance']
publication_counts = np.array([
    [50, 80, 150, 200],  # Fiction
    [30, 60, 100, 150],  # Non-Fiction
    [0, 10, 80, 120],    # Science Fiction
    [0, 5, 50, 130],     # Fantasy
    [10, 40, 90, 110],   # Mystery
    [5, 20, 70, 160],    # Romance
])

average_page_counts = np.array([
    [200, 250, 300, 350],  # Fiction
    [150, 200, 250, 300],  # Non-Fiction
    [0, 180, 250, 320],    # Science Fiction
    [0, 160, 220, 300],    # Fantasy
    [180, 240, 260, 280],  # Mystery
    [150, 170, 230, 310],  # Romance
])

popularity_indices = np.array([
    [300, 500, 800, 1200],  # Fiction
    [250, 450, 700, 1000],  # Non-Fiction
    [0, 200, 600, 900],     # Science Fiction
    [0, 150, 400, 850],     # Fantasy
    [100, 300, 500, 700],   # Mystery
    [50, 200, 550, 1000],   # Romance
])

# Summarize data for the line plot
total_publications_per_century = publication_counts.sum(axis=0)

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# 3D Scatter plot
ax = fig.add_subplot(121, projection='3d')

colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']

for i, genre in enumerate(genres):
    ax.scatter(centuries, publication_counts[i], average_page_counts[i],
               s=popularity_indices[i], alpha=0.7, c=colors[i], edgecolors='w', label=genre)

ax.set_xlabel('Century', labelpad=10)
ax.set_ylabel('Notable Publications', labelpad=10)
ax.set_zlabel('Average Page Count', labelpad=10)
ax.set_title('Evolution of Book Genres Over the Centuries', pad=20)
ax.view_init(elev=20, azim=135)
ax.legend(title="Genres", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small', title_fontsize='medium')

# Line plot
ax2.plot(centuries, total_publications_per_century, marker='o', linestyle='-', color='b')
ax2.set_title('Total Publications Over Centuries')
ax2.set_xlabel('Century')
ax2.set_ylabel('Total Publications')
ax2.grid(True)
ax2.set_xticks(centuries)

# Automatically adjust layout
plt.tight_layout()

plt.show()