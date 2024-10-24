import matplotlib.pyplot as plt
import numpy as np

# Define the decades and genres
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010])
genres = ['Rock', 'Jazz', 'Pop', 'Hip-Hop', 'Electronic']

# Create data for the number of albums released in each genre per decade
album_releases = np.array([
    [30, 15, 10, 0, 0],   # 1950s
    [40, 25, 15, 0, 0],   # 1960s
    [80, 30, 20, 0, 0],   # 1970s
    [120, 20, 40, 10, 0], # 1980s
    [100, 10, 70, 15, 0], # 1990s
    [90, 5, 60, 50, 5],   # 2000s
    [60, 5, 70, 50, 30]   # 2010s
])

# Generate additional data for a stacked area plot
# Assuming this data represents the percentage share of each genre in total album releases
total_releases = album_releases.sum(axis=1, keepdims=True)
share_data = (album_releases / total_releases) * 100

# Set up the figure with two subplots
fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# Parameters for the 3D bar chart
num_decades = len(decades)
num_genres = len(genres)
_x = np.arange(num_decades)
_y = np.arange(num_genres)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
colors = plt.cm.viridis(np.linspace(0, 1, num_genres))
bottom = np.zeros_like(_x)

# Plot the 3D bars
for i in range(num_genres):
    dz = album_releases[:, i]
    ax1.bar3d(_x, y[i * num_decades:(i + 1) * num_decades], bottom, dx=0.5, dy=0.5, dz=dz, color=colors[i], alpha=0.8)
    
# Customize 3D axes
ax1.set_xticks(_x + 0.25)
ax1.set_xticklabels(decades)
ax1.set_yticks(np.arange(num_genres) + 0.25)
ax1.set_yticklabels(genres)
ax1.set_zlabel('Albums Released')
ax1.set_xlabel('Decades')
ax1.set_ylabel('Genres')
ax1.set_title('Albums Released by Genre and Decade', fontsize=12, weight='bold', pad=15)
ax1.view_init(elev=30, azim=120)

# Plot the stacked area chart
ax2.stackplot(decades, share_data.T, labels=genres, colors=colors, alpha=0.8)
ax2.set_title('Genre Share of Total Album Releases\nAcross Decades', fontsize=12, weight='bold')
ax2.set_xlabel('Decades')
ax2.set_ylabel('Percentage Share (%)')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()