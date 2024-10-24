import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import matplotlib.colors as mcolors

# Define data for continents and genres
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
genres = ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical', 'Electronic']

# Percentage of streaming hours by genre for each continent
data_by_continent = np.array([
    [25, 15, 20, 10, 20, 10],  # Africa
    [30, 10, 25, 5, 15, 15],   # Asia
    [20, 20, 15, 10, 25, 10],  # Europe
    [25, 20, 30, 5, 10, 10],   # North America
    [15, 10, 35, 10, 5, 25],   # South America
    [20, 15, 20, 20, 15, 10],  # Australia
])

# Colors for each genre using a cohesive seaborn palette
palette = sns.color_palette("Set2", n_colors=len(genres))
colors = [mcolors.to_hex(color) for color in palette]

# Plotting
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Bar width and positions
bar_width = 0.4
_x = np.arange(len(continents))
_y = np.arange(len(genres))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Flattened data for the bars
z = np.zeros_like(x)
dx = dy = bar_width
dz = data_by_continent.T.ravel()

# Plotting 3D bars with lighting effect
ax.bar3d(x, y, z, dx, dy, dz, color=np.repeat(colors, len(continents)), edgecolor='black', alpha=0.9)

# Setting labels and title
ax.set_xticks(_x + bar_width / 2)
ax.set_xticklabels(continents, rotation=45, ha='right', fontsize=10)
ax.set_yticks(_y + bar_width / 2)
ax.set_yticklabels(genres, fontsize=10)
ax.set_zlabel('Streaming Hours (%)', fontsize=12)
ax.set_title('2023 Global Music Streaming Trends\nGenre-wise Percentage Distribution Across Continents', fontsize=15, pad=30)

# Improved legend positioning and added annotation
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=genre, markersize=10, markerfacecolor=color) 
                   for genre, color in zip(genres, colors)]
ax.legend(handles=legend_elements, title="Music Genres", loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Normalizing the z-axis to 0-40%
ax.set_zlim(0, 40)

# Adjust viewing angle for better visualization
ax.view_init(elev=30, azim=40)

# Annotate highest streaming genre in each continent
max_indices = np.argmax(data_by_continent, axis=1)
for i, (continent, index) in enumerate(zip(continents, max_indices)):
    ax.text(x[i], y[index], data_by_continent[i, index] + 1, f"{genres[index]} ({data_by_continent[i, index]}%)",
            color='black', fontsize=9, ha='center', va='bottom')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()