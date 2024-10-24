import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Cities and corresponding renewable energy percentages
cities = ['Oslo', 'San Francisco', 'Cape Town', 'Sydney', 'Tokyo']
renewable_energy_percentages = np.array([
    [70, 20, 10],  # Oslo: Solar, Wind, Hydro
    [55, 35, 10],  # San Francisco
    [35, 50, 15],  # Cape Town
    [25, 50, 25],  # Sydney
    [15, 60, 25]   # Tokyo
])

# Renewable sources
sources = ['Solar', 'Wind', 'Hydro']

# Number of cities and sources
num_cities = len(cities)
num_sources = len(sources)

# Setup the figure and 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
x_pos, y_pos = np.meshgrid(np.arange(num_cities), np.arange(num_sources), indexing='ij')

# Flatten the positions for plotting
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Values (heights) and width of bars
values = renewable_energy_percentages.flatten()
dx = dy = 0.6
dz = values

# Colors for each energy source
colors = ['#FFD700', '#32CD32', '#1E90FF']  # Solar, Wind, Hydro

# Plot bars
for i in range(num_sources):
    ax.bar3d(x_pos[i::num_sources], y_pos[i::num_sources], z_pos[i::num_sources], 
             dx, dy, dz[i::num_sources], color=colors[i], alpha=0.8, label=sources[i])

# Customizing the axes
ax.set_xlabel('Cities')
ax.set_ylabel('Energy Sources')
ax.set_zlabel('Percentage (%)')
ax.set_xticks(np.arange(num_cities))
ax.set_xticklabels(cities, rotation=45, ha='right')
ax.set_yticks(np.arange(num_sources))
ax.set_yticklabels(sources)
ax.set_zlim(0, 100)

# Adding the title and legend
ax.set_title('Renewable Energy Adoption in Major Global Cities\n', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10, title='Energy Source')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()