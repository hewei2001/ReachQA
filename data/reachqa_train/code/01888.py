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

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Parameters for plotting
num_decades = len(decades)
num_genres = len(genres)
_x = np.arange(num_decades)
_y = np.arange(num_genres)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Bar parameters
colors = plt.cm.viridis(np.linspace(0, 1, num_genres))
dx = dy = 0.5

# Plot the stacked bars
for i in range(num_genres):
    z = np.zeros(num_decades)
    dz = album_releases[:, i]
    ax.bar3d(_x, np.full(num_decades, i), z, dx, dy, dz, color=colors[i], alpha=0.8, label=genres[i])

# Customize axes
ax.set_xticks(_x)
ax.set_xticklabels(decades)
ax.set_yticks(np.arange(num_genres))
ax.set_yticklabels(genres)
ax.set_zlabel('Albums Released')
ax.set_xlabel('Decades')
ax.set_ylabel('Genres')
ax.set_title('Evolution of Musical Genres Across Decades\n(1950s to 2010s)', fontsize=14, weight='bold', pad=20)

# Adjust view angle for better visibility
ax.view_init(elev=30, azim=120)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1.0), fontsize=10, title='Genres')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()