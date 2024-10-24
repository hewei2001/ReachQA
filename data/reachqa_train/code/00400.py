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

# Calculate cumulative popularity
cumulative_popularity = rock + pop + jazz + hip_hop + electronic

# Create the stack for the area chart
genres = np.vstack([rock, pop, jazz, hip_hop, electronic])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 9))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the stacked area chart
ax.stackplot(decades, genres, labels=['Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Electronic'],
             colors=colors, alpha=0.8)

# Add a line plot for cumulative popularity
ax.plot(decades, cumulative_popularity, color='black', linestyle='--', marker='o', label='Cumulative Popularity')

# Annotations for significant changes
ax.annotate('Rise of Hip-Hop', xy=('2000s', hip_hop[5] + rock[5] + pop[5] + jazz[5] / 2), 
            xytext=('2000s', 60), textcoords='data',
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, fontweight='bold')

# Customize the plot with title and labels
ax.set_title('The Evolution of Music Genres \n Over Decades & Cumulative Popularity', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)
ax.legend(loc='upper left', title='Genres', fontsize=10, bbox_to_anchor=(1, 1))

# Enhance readability with a grid
ax.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()