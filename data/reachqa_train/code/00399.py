import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1950s to the 2020s
decades = np.array(["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"])

# Artificial data representing genre popularity as a percentage over the decades
rock = np.array([30, 35, 40, 45, 35, 20, 15, 10])
pop = np.array([20, 25, 30, 40, 30, 25, 20, 15])
jazz = np.array([25, 20, 15, 10, 5, 3, 2, 1])
hip_hop = np.array([0, 0, 5, 15, 25, 30, 35, 30])
electronic = np.array([0, 0, 0, 5, 5, 20, 28, 44])

# Create the stack for the area chart
genres = np.vstack([rock, pop, jazz, hip_hop, electronic])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the stacked area chart
ax.stackplot(decades, genres, labels=['Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Electronic'],
             colors=colors, alpha=0.8)

# Customize the plot with title and labels
ax.set_title('The Evolution of Music Genres Over Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)
ax.legend(loc='upper left', title='Genres', fontsize=10)

# Enhance readability with a grid
ax.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()