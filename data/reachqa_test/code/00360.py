import matplotlib.pyplot as plt
import numpy as np

decades = ['1970s', '1980s', '1990s', '2000s', '2010s']
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']

# Popularity scores (higher is more popular)
popularity_matrix = np.array([
    [8, 5, 7, 3, 6, 2, 4],  # 1970s
    [7, 6, 8, 4, 5, 3, 2],  # 1980s
    [6, 7, 9, 5, 4, 3, 2],  # 1990s
    [8, 9, 7, 6, 5, 4, 3],  # 2000s
    [9, 8, 7, 6, 5, 4, 3]   # 2010s
])

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(popularity_matrix, cmap='YlGnBu', aspect='auto', interpolation='nearest')

ax.set_xticks(np.arange(len(genres)))
ax.set_yticks(np.arange(len(decades)))
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(decades, fontsize=10)

ax.set_title("Movie Genre Popularity by Decade\n"
             "Higher values indicate more popular genres",
             fontsize=14, fontweight='bold')

fig.colorbar(im, shrink=0.5, pad=0.02, label='Popularity Score')

# Add a grid to separate decades
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

# Add annotations for each cell
for i in range(len(decades)):
    for j in range(len(genres)):
        ax.text(j, i, str(popularity_matrix[i, j]), ha='center', va='center', color='white')

plt.tight_layout()
plt.show()