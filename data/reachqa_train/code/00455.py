import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define genres and decades
genres = ['Mystery', 'Science Fiction', 'Romance', 'Historical Fiction', 'Fantasy']
decades = ['1960s', '1970s', '1980s', '1990s', '2000s']

# Create data representing the popularity in terms of fictional book sales (in millions)
popularity = np.array([
    [15, 20, 25, 30, 35],  # Mystery
    [10, 15, 20, 25, 30],  # Science Fiction
    [30, 35, 40, 45, 50],  # Romance
    [12, 17, 22, 27, 32],  # Historical Fiction
    [5, 10, 15, 20, 25]    # Fantasy
])

# Calculate cumulative sales for stacked effect
cumulative_popularity = np.cumsum(popularity, axis=0)

# Prepare the indices for the bar positions
xpos, ypos = np.meshgrid(np.arange(len(decades)), np.arange(len(genres)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Setup the figure and 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D stacked bar chart
colors = plt.cm.tab20(np.linspace(0, 1, len(genres)))
for i in range(len(genres)):
    ax.bar3d(
        xpos[ypos == i], ypos[ypos == i], zpos[ypos == i],
        dx=0.4, dy=0.4, dz=popularity[i],
        color=colors[i], alpha=0.8, label=genres[i]
    )
    zpos[ypos == i] += popularity[i]

# Set the labels and ticks
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, rotation=30, ha='right')
ax.set_yticks(np.arange(len(genres)))
ax.set_yticklabels(genres)
ax.set_zlabel('Book Sales (Millions)', fontsize=10)

# Set title
ax.set_title("Global Literary Genres:\nEvolution of Popularity Over Decades",
             fontsize=14, weight='bold', loc='center')

# Customize plot appearance
ax.view_init(elev=30, azim=240)
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_edgecolor('w')
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', which='both')

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.1, 1), title='Genres')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()